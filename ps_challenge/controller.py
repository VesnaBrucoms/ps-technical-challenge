from ps_challenge.exceptions import UserDataNotFoundError
from ps_challenge.users import get_all_users, get_game_achievements, get_user_library


def get_all_users_achievement_levels(level_filter):
    raise NotImplementedError


def get_user_achievement_level(user_id):
    library = get_user_library(user_id)
    level = ""
    if len(library["ownedGames"]) <= 10:
        level = "None"
    else:
        percentages = get_user_completed_percentages(
            library["user"]["id"], library["ownedGames"]
        )
        level = calculate_achievement_level(percentages)

    return {"user": library["user"], "overallAchievmentLevel": level}


def get_user_completed_percentages(user_id, games):
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


def calculate_achievement_level(achievement_data):
    game_count = len(achievement_data)
    ((50, 100), (25, 80), (10, 75), (10, 0))
    return ""
