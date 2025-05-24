none_completed_counts = [1, 2, 3, 4, 5]
bronze_completed_counts = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
silver_completed_counts = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
gold_completed_counts = [
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
    16,
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
