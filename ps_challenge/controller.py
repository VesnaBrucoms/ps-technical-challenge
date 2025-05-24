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
        full_achievement_data = get_user_completed_achievements(
            library["user"]["id"], library["ownedGames"]
        )
        level = calculate_achievement_level(full_achievement_data)

    return {"user": library["user"], "overallAchievmentLevel": level}


def get_user_completed_achievements(user_id, games):
    try:
        achievement_list = []
        for game in games:
            completed_count = get_game_achievements(user_id, game["id"])[
                "totalCompletedAchievements"
            ]
            achievement_list.append(
                {
                    "gameId": game["id"],
                    "totalAchievements": game["totalAvailableAchievements"],
                    "completedAchievements": completed_count,
                }
            )
        return achievement_list
    except UserDataNotFoundError as err:
        raise err


def calculate_achievement_level(achievement_data):
    return ""
