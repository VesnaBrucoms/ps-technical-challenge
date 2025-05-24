from ps_challenge.users import get_all_users, get_game_achievements, get_user_library


def get_all_users_achievement_levels(level_filter):
    raise NotImplementedError


def get_user_achievement_level(user_id):
    library = get_user_library(user_id)
    level = ""
    if len(library["ownedGames"]) <= 10:
        level = "None"
    else:
        pass
    return {"user": library["user"], "overallAchievmentLevel": level}


def calculate_achievement_level(users_games):
    raise NotImplementedError
