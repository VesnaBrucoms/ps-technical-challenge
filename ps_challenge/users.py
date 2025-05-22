import requests

from ps_challenge.exceptions import UserDataNotFoundError

url = "http://127.0.0.1:8080/"


def get_all_users():
    r = requests.get(url + "users")
    if r.status_code != 200:
        raise UserDataNotFoundError(
            "An error occured when getting all users", r.status_code
        )
    return r.json()


def get_user_library(user_id):
    r = requests.get(url + "users/" + str(user_id) + "/library")
    if r.status_code == 404:
        raise UserDataNotFoundError(
            "User with ID {} could not be found".format(user_id), r.status_code
        )
    elif r.status_code != 200:
        raise UserDataNotFoundError(
            "An error occured when getting all users", r.status_code
        )
    return r.json()


def get_game_achievements(user_id, game_id):
    r = requests.get(url + "users/" + str(user_id) + "/achievements/" + str(game_id))
    if r.status_code == 404:
        raise UserDataNotFoundError(
            "User with ID {} or game with ID {} could not be found".format(
                user_id, game_id
            ),
            r.status_code,
        )
    elif r.status_code != 200:
        raise UserDataNotFoundError(
            "An error occured when getting all users", r.status_code
        )
    return r.json()
