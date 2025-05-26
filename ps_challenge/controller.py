import logging
import time
from typing import TypeAlias

from ps_challenge.config import CRITERIA_THRESHOLDS
from ps_challenge.exceptions import UserDataNotFoundError
from ps_challenge.users import get_all_users, get_game_achievements, get_user_library


UserLevel: TypeAlias = dict
GameCompletionRate: TypeAlias = dict

logger = logging.getLogger("ps_challenge.app")


def get_all_users_achievement_levels(level_filter: str | None) -> list[UserLevel]:
    """Builds and returns a list of all users and their levels.

    This is a naive implementation that does not handle large datasets well. See the [design docs
    page](../docs/design/future-changes.md#Async) for more info on what could be improved here.

    Arguments:
    level_filter -- Achievement level to filter for
    """
    if level_filter is not None:
        logger.debug("Filtering to users with level {}".format(level_filter))
    else:
        logger.debug("No filtering")
    start_time = time.time()

    all_users = get_all_users()
    all_levels = []
    for user in all_users:
        user_level = get_user_achievement_level(user["id"])
        if level_filter is not None:
            if user_level["overallAchievementLevel"] == level_filter.capitalize():
                all_levels.append(user_level)
            else:
                logger.debug("Filtered out user with ID {}".format(user["id"]))
        else:
            all_levels.append(user_level)

    logger.debug("Completed in {} seconds".format(time.time() - start_time))
    return all_levels


def get_user_achievement_level(user_id: str) -> UserLevel:
    """Builds and returns a single user and their level.

    Arguments:
    user_id -- The specific user's ID
    """
    library = get_user_library(user_id)
    level = ""
    if len(library["ownedGames"]) <= 10:
        level = "None"
    else:
        percentages = _get_user_completed_percentages(
            library["user"]["id"], library["ownedGames"]
        )
        level = _calculate_achievement_level(percentages)

    logger.debug("User %s level set to %s", user_id, level)
    return {"user": library["user"], "overallAchievementLevel": level}


def _get_user_completed_percentages(
    user_id: str, games: list
) -> list[GameCompletionRate]:
    """Returns calculated completion percentages for each game and what thresholds have been met.

    Arguments:
    user_id -- User's ID to perform the calculation for
    games -- List of given user's game library
    """
    try:
        achievement_list = []
        for game in games:
            completed_count = get_game_achievements(user_id, game["id"])[
                "totalCompletedAchievements"
            ]
            completed_percentage = completed_count / game["totalAvailableAchievements"]
            achievement_list.append(
                {
                    "gameId": game["id"],
                    "completedPercentage": completed_percentage,
                }
            )

        return achievement_list
    except UserDataNotFoundError as err:
        raise err


def _calculate_achievement_level(achievement_data: list[GameCompletionRate]) -> str:
    """Returns the achievement level by checking user's data against CRITERIA_THRESHOLDS.

    Arguments:
    achievement_data -- Contains calculated completion percentages and what thresholds have been met
    """
    is_100 = True
    is_over_80 = True
    is_over_75 = True
    for game_data in achievement_data:
        if game_data["completedPercentage"] < CRITERIA_THRESHOLDS[0].percentage:
            is_100 = False
        if game_data["completedPercentage"] <= CRITERIA_THRESHOLDS[1].percentage:
            is_over_80 = False
        if game_data["completedPercentage"] <= CRITERIA_THRESHOLDS[2].percentage:
            is_over_75 = False

    level = ""
    for threshold in CRITERIA_THRESHOLDS:
        if (
            len(achievement_data) > threshold.games
            and is_100 == threshold.over_100
            and is_over_80 == threshold.over_80
            and is_over_75 == threshold.over_75
        ):
            level = threshold.name
            break

    return level
