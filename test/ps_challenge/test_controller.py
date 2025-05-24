from unittest import TestCase
from unittest.mock import patch

from ps_challenge.controller import (
    get_all_users_achievement_levels,
    get_user_achievement_level,
)
from ps_challenge.exceptions import UserDataNotFoundError
from test.mock_data.mock_achievements import (
    generate_mock_achievement_list_json,
    none_completed_counts,
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


class TestController(TestCase):

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    @patch("ps_challenge.controller.get_all_users")
    def test_get_all_users_achievement_levels(
        self, get_all_mock, get_lib_mock, get_achieve_mock
    ):
        expected_json = [
            {
                "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
                "overallAchievmentLevel": "Bronze",
            },
            {
                "user": {"id": 2, "name": "Bob Tester", "email": "btester@email.com"},
                "overallAchievmentLevel": "Platinum",
            },
        ]
        result = get_all_users_achievement_levels()
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_none(self, get_lib_mock, get_achieve_mock):
        user_id = 1
        get_lib_mock.return_value = none_lib
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            none_lib["user"], none_lib["ownedGames"], none_completed_counts
        )
        expected_json = {
            "user": {
                "id": user_id,
                "name": "None Tester",
                "email": "ntester@email.com",
            },
            "overallAchievmentLevel": "None",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_bronze(self, get_lib_mock, get_achieve_mock):
        user_id = 2
        get_lib_mock.return_value = bronze_lib
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            bronze_lib["user"], bronze_lib["ownedGames"], bronze_completed_counts
        )
        expected_json = {
            "user": {
                "id": user_id,
                "name": "Bronze Tester",
                "email": "btester@email.com",
            },
            "overallAchievmentLevel": "Bronze",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_silver(self, get_lib_mock, get_achieve_mock):
        user_id = 3
        get_lib_mock.return_value = silver_lib
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            silver_lib["user"], silver_lib["ownedGames"], silver_completed_counts
        )
        expected_json = {
            "user": {
                "id": user_id,
                "name": "Silver Tester",
                "email": "stester@email.com",
            },
            "overallAchievmentLevel": "Silver",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_gold(self, get_lib_mock, get_achieve_mock):
        user_id = 4
        get_lib_mock.return_value = gold_lib
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            gold_lib["user"], gold_lib["ownedGames"], gold_completed_counts
        )
        expected_json = {
            "user": {
                "id": user_id,
                "name": "Gold Tester",
                "email": "gtester@email.com",
            },
            "overallAchievmentLevel": "Gold",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_platinum(self, get_lib_mock, get_achieve_mock):
        user_id = 5
        get_lib_mock.return_value = platinum_lib
        get_achieve_mock.side_effect = generate_mock_achievement_list_json(
            platinum_lib["user"], platinum_lib["ownedGames"], platinum_completed_counts
        )
        expected_json = {
            "user": {
                "id": user_id,
                "name": "Platinum Tester",
                "email": "ptester@email.com",
            },
            "overallAchievmentLevel": "Platinum",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_404(self, get_lib_mock):
        user_id = 1
        get_lib_mock.side_effect = UserDataNotFoundError("", 404)

        with self.assertRaises(UserDataNotFoundError) as error:
            get_user_achievement_level(user_id)
        self.assertEqual(error.exception.status_code, 404)

    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_500(self, get_lib_mock):
        user_id = 1
        get_lib_mock.side_effect = UserDataNotFoundError("", 500)

        with self.assertRaises(UserDataNotFoundError) as error:
            get_user_achievement_level(user_id)
        self.assertEqual(error.exception.status_code, 500)
