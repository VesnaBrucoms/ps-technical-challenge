import logging
import time

from ps_challenge.config import CRITERIA_THRESHOLDS
from ps_challenge.exceptions import UserDataNotFoundError
from ps_challenge.users import get_all_users, get_game_achievements, get_user_library

logger = logging.getLogger("ps_challenge.app")


def get_all_users_achievement_levels(level_filter):
    """Builds and returns a list of all users and their levels.

    Arguments:
    level_filter -- (str) Achievement level to filter for
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
            if user_level["overallAchievmentLevel"] == level_filter.capitalize():
                all_levels.append(user_level)
            else:
                logger.debug("Filtered out user with ID {}".format(user["id"]))
        else:
            all_levels.append(user_level)

    logger.debug("Completed in {} seconds".format(time.time() - start_time))
    return all_levels


def get_user_achievement_level(user_id):
    """Builds and returns a single user and their level.

    Arguments:
    user_id -- (str) The specific user's ID
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


def _get_user_completed_percentages(user_id, games):
    """Returns calculated completion percentages for each game and what thresholds have been met.

    Arguments:
    user_id -- (int) User's ID to perform the calculation for
    games -- (list) List of given user's game library
    """
    try:
        achievement_list = []
        is_100 = True
        is_over_80 = True
        is_over_75 = True
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

            if completed_percentage < 100:
                is_100 = False
            if completed_percentage <= 0.8:
                is_over_80 = False
            if completed_percentage <= 0.75:
                is_over_75 = False

        return {
            "games": achievement_list,
            "is100": is_100,
            "isOver80": is_over_80,
            "isOver75": is_over_75,
        }
    except UserDataNotFoundError as err:
        raise err


def _calculate_achievement_level(achievement_data):
    """Returns the achievement level by checking user's data against CRITERIA_THRESHOLDS.

    Arguments:
    achievement_data -- (obj) Contains calculated completion percentages and what thresholds have been met
    """
    level = ""
    for threshold in CRITERIA_THRESHOLDS:
        if (
            len(achievement_data["games"]) > threshold[0]
            and achievement_data["is100"] == threshold[1]
            and achievement_data["isOver80"] == threshold[2]
            and achievement_data["isOver75"] == threshold[3]
        ):
            level = threshold[4]

    return level
