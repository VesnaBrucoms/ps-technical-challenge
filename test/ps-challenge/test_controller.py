from unittest import TestCase
from unittest.mock import patch

from ps_challenge.controller import (
    get_all_users_achievement_levels,
    get_user_achievement_level,
)
from ps_challenge.exceptions import UserDataNotFoundError


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
        expected_json = {
            "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
            "overallAchievmentLevel": "None",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_bronze(self, get_lib_mock, get_achieve_mock):
        user_id = 1
        expected_json = {
            "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
            "overallAchievmentLevel": "Bronze",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_silver(self, get_lib_mock, get_achieve_mock):
        user_id = 1
        expected_json = {
            "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
            "overallAchievmentLevel": "Silver",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_gold(self, get_lib_mock, get_achieve_mock):
        user_id = 1
        expected_json = {
            "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
            "overallAchievmentLevel": "Gold",
        }
        result = get_user_achievement_level(user_id)
        self.assertDictEqual(result, expected_json)

    @patch("ps_challenge.controller.get_game_achievements")
    @patch("ps_challenge.controller.get_user_library")
    def test_get_user_achievement_level_platinum(self, get_lib_mock, get_achieve_mock):
        user_id = 1
        expected_json = {
            "user": {"id": 1, "name": "John Tester", "email": "jtester@email.com"},
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
