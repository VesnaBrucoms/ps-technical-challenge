none_completed_counts = [1, 2, 3, 4, 5]
bronze_completed_counts = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 15]
silver_completed_counts = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
gold_completed_counts = [
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
    17,
]
platinum_completed_counts = [
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
    20,
]


def generate_mock_achievement_json(user, game, completed_count):
    return {
        "user": user,
        "game": game,
        "totalCompletedAchievements": completed_count,
    }


def generate_mock_achievement_list_json(user, games, completed_counts):
    return_list = []
    for i in range(0, len(games)):
        return_list.append(
            generate_mock_achievement_json(user, games[i], completed_counts[i])
        )
    return return_list


def generate_mock_percent_json(game_id, total, completed):
    percentage = completed / total
    return {"gameId": game_id, "completedPercentage": percentage}


def generate_mock_percent_list_json(user, games, completed_counts):
    return_list = []
    for i in range(0, len(games)):
        return_list.append(
            generate_mock_percent_json(
                user, games[i]["totalAvailableAchievements"], completed_counts[i]
            )
        )
    return return_list
