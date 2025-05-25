from unittest import TestCase
from unittest.mock import patch

from ps_challenge.controller import (
    get_all_users_achievement_levels,
    get_user_achievement_level,
    _get_user_completed_percentages,
    _calculate_achievement_level,
)
from ps_challenge.exceptions import UserDataNotFoundError
from test.mock_data.mock_achievements import (
    generate_mock_achievement_list_json,
    generate_mock_percent_list_json,
    bronze_completed_counts,
    silver_completed_counts,
    gold_completed_counts,
    platinum_completed_counts,
)
from test.mock_data.mock_libraries import (
    none_lib,
    bronze_lib,
    silver_lib,
    gold_lib,
    platinum_lib,
)
from test.mock_data.mock_users import all_users


class TestController(TestCase):

    @patch("ps_challenge.controller.get_user_achievement_level")
    @patch("ps_challenge.controller.get_all_users")
    def test_get_all_users_achievement_levels(self, get_all_mock, get_level_mock):
        get_all_mock.return_value = all_users
        get_level_mock.return_value = {
            "user": all_users[1],
            "overallAchievementLevel": "Bronze",
        }
        expected_json = [
            {
                "user": {
                    "id": 2,
                    "name": "Bronze Tester",
                    "email": "btester@email.com",
                },
                "overallAchievementLevel": "Bronze",
            }
        ] * 5

        result = get_all_users_achievement_levels(None)

        self.assertListEqual(result, expected_json)
        self.assertEqual(get_all_mock.call_count, 1)
        self.assertEqual(get_level_mock.call_count, 5)

    @patch("ps_challenge.controller._calculate_achievement_level")
    @patch("ps_challenge.controller._get_user_completed_percentages")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_none(
        self, get_lib_mock, get_perc_mock, get_level_mock
    ):
        user_id = 1
        get_lib_mock.return_value = none_lib
        expected_json = {
            "user": {
                "id": user_id,
                "name": "None Tester",
                "email": "ntester@email.com",
            },
            "overallAchievementLevel": "None",
        }
        result = get_user_achievement_level(user_id)

        self.assertDictEqual(result, expected_json)
        self.assertEqual(get_perc_mock.call_count, 0)
        self.assertEqual(get_level_mock.call_count, 0)

    @patch("ps_challenge.controller._calculate_achievement_level")
    @patch("ps_challenge.controller._get_user_completed_percentages")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level(
        self, get_lib_mock, get_perc_mock, get_level_mock
    ):
        get_lib_mock.return_value = bronze_lib
        get_perc_mock.side_effect = generate_mock_percent_list_json(
            bronze_lib["user"], bronze_lib["ownedGames"], bronze_completed_counts
        )
        get_level_mock.return_value = "Bronze"
        expected_json = {
            "user": {
                "id": bronze_lib["user"]["id"],
                "name": "Bronze Tester",
                "email": "btester@email.com",
            },
            "overallAchievementLevel": "Bronze",
        }

        result = get_user_achievement_level(bronze_lib["user"]["id"])

        self.assertDictEqual(result, expected_json)
        self.assertEqual(get_perc_mock.call_count, 1)
        self.assertEqual(get_level_mock.call_count, 1)

    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_404(self, get_lib_mock):
        get_lib_mock.side_effect = UserDataNotFoundError("", 404)

        with self.assertRaises(UserDataNotFoundError) as error:
            get_user_achievement_level(1)
        self.assertEqual(error.exception.status_code, 404)

    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_500(self, get_lib_mock):
        get_lib_mock.side_effect = UserDataNotFoundError("", 500)

        with self.assertRaises(UserDataNotFoundError) as error:
            get_user_achievement_level(1)
        self.assertEqual(error.exception.status_code, 500)

    @patch("ps_challenge.controller.get_game_achievements")
    def test__get_user_completed_percentages_bronze(self, get_achieve_mock):
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            bronze_lib["user"], bronze_lib["ownedGames"], bronze_completed_counts
        )
        expected_json = {
            "games": [
                {"gameId": 0, "completedPercentage": 0.05},
                {"gameId": 0, "completedPercentage": 0.1},
                {"gameId": 0, "completedPercentage": 0.15},
                {"gameId": 0, "completedPercentage": 0.2},
                {"gameId": 0, "completedPercentage": 0.25},
                {"gameId": 0, "completedPercentage": 0.05},
                {"gameId": 0, "completedPercentage": 0.1},
                {"gameId": 0, "completedPercentage": 0.15},
                {"gameId": 0, "completedPercentage": 0.2},
                {"gameId": 0, "completedPercentage": 0.25},
                {"gameId": 0, "completedPercentage": 0.05},
                {"gameId": 0, "completedPercentage": 0.75},
            ],
            "is100": False,
            "isOver80": False,
            "isOver75": False,
        }

        result = _get_user_completed_percentages(
            bronze_lib["user"], bronze_lib["ownedGames"]
        )

        self.assertEqual(result, expected_json)
        self.assertEqual(get_achieve_mock.call_count, 12)

    @patch("ps_challenge.controller.get_game_achievements")
    def test__get_user_completed_percentages_silver(self, get_achieve_mock):
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            silver_lib["user"], silver_lib["ownedGames"], silver_completed_counts
        )
        expected_json = {
            "games": [
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
                {"gameId": 0, "completedPercentage": 0.8},
            ],
            "is100": False,
            "isOver80": False,
            "isOver75": True,
        }

        result = _get_user_completed_percentages(
            silver_lib["user"], silver_lib["ownedGames"]
        )

        self.assertEqual(result, expected_json)
        self.assertEqual(get_achieve_mock.call_count, 12)

    @patch("ps_challenge.controller.get_game_achievements")
    def test__get_user_completed_percentages_404(self, get_achieve_mock):
        get_achieve_mock.side_effect = UserDataNotFoundError("", 404)
        with self.assertRaises(UserDataNotFoundError) as error:
            _get_user_completed_percentages(none_lib["user"], none_lib["ownedGames"])

        self.assertEqual(error.exception.status_code, 404)
        self.assertEqual(get_achieve_mock.call_count, 1)

    def test__calculate_achievement_level_bronze(self):
        bronze_data = {
            "games": generate_mock_percent_list_json(
                bronze_lib["user"], bronze_lib["ownedGames"], bronze_completed_counts
            ),
            "is100": False,
            "isOver80": False,
            "isOver75": False,
        }
        expected_result = "Bronze"

        result = _calculate_achievement_level(bronze_data)

        self.assertEqual(result, expected_result)

    def test__calculate_achievement_level_silver(self):
        silver_data = {
            "games": generate_mock_percent_list_json(
                silver_lib["user"], silver_lib["ownedGames"], silver_completed_counts
            ),
            "is100": False,
            "isOver80": False,
            "isOver75": True,
        }
        expected_result = "Silver"

        result = _calculate_achievement_level(silver_data)

        self.assertEqual(result, expected_result)

    def test__calculate_achievement_level_gold(self):
        gold_data = {
            "games": generate_mock_percent_list_json(
                gold_lib["user"], gold_lib["ownedGames"], gold_completed_counts
            ),
            "is100": False,
            "isOver80": True,
            "isOver75": True,
        }
        expected_result = "Gold"

        result = _calculate_achievement_level(gold_data)

        self.assertEqual(result, expected_result)

    def test__calculate_achievement_level_platinum(self):
        platinum_data = {
            "games": generate_mock_percent_list_json(
                platinum_lib["user"],
                platinum_lib["ownedGames"],
                platinum_completed_counts,
            ),
            "is100": True,
            "isOver80": True,
            "isOver75": True,
        }
        expected_result = "Platinum"

        result = _calculate_achievement_level(platinum_data)

        self.assertEqual(result, expected_result)
