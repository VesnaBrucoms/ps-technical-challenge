from unittest import TestCase

from responses import add
from responses import activate
from responses import Response

from ps_challenge.users import get_user_library
from ps_challenge.users import get_game_achievements
from ps_challenge.users import get_all_users
from ps_challenge.exceptions import UserDataNotFoundError
from test.mock_data.mock_libraries import bronze_lib
from test.mock_data.mock_users import all_users

url = "http://127.0.0.1:8080/"


class TestUsers(TestCase):

    @activate
    def test_get_all_users(self):
        add(
            Response(
                method="GET",
                url=url + "users",
                json=all_users,
            )
        )

        result = get_all_users()

        self.assertEqual(all_users, result)

    @activate
    def test_get_all_users_500(self):
        add(
            Response(
                method="GET",
                url=url + "users",
                status=500,
            )
        )

        with self.assertRaises(UserDataNotFoundError) as error:
            get_all_users()
        self.assertEqual(error.exception.status_code, 500)

    @activate
    def test_get_user_library(self):
        add(
            Response(
                method="GET",
                url=url + "users/" + str(bronze_lib["user"]["id"]) + "/library",
                json=bronze_lib,
            )
        )

        result = get_user_library(bronze_lib["user"]["id"])

        self.assertDictEqual(bronze_lib, result)

    @activate
    def test_get_user_library_404(self):
        user_id = 20
        add(
            Response(
                method="GET", url=url + "users/" + str(user_id) + "/library", status=404
            )
        )

        with self.assertRaises(UserDataNotFoundError) as error:
            get_user_library(user_id)
        self.assertEqual(error.exception.status_code, 404)

    @activate
    def test_get_game_achievements(self):
        user_id = 20
        game_id = 435
        mock_json = {
            "user": {
                "id": user_id,
                "name": "John Tester",
                "email": "jtester@email.com",
            },
            "game": {"id": 0, "title": "Game 1", "totalAvailableAchievements": 20},
            "totalCompletedAchievements": 16,
        }
        add(
            Response(
                method="GET",
                url=url + "users/" + str(user_id) + "/achievements/" + str(game_id),
                json=mock_json,
            )
        )

        result = get_game_achievements(user_id, game_id)

        self.assertDictEqual(mock_json, result)

    @activate
    def test_get_game_achievements_404(self):
        user_id = 20
        game_id = 435
        add(
            Response(
                method="GET",
                url=url + "users/" + str(user_id) + "/achievements/" + str(game_id),
                status=404,
            )
        )

        with self.assertRaises(UserDataNotFoundError) as error:
            get_game_achievements(user_id, game_id)
        self.assertEqual(error.exception.status_code, 404)
