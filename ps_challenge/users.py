import logging
import requests

from ps_challenge.exceptions import UserDataNotFoundError

logger = logging.getLogger("ps_challenge.app")

url = "http://127.0.0.1:8080/"


def get_all_users():
    r = requests.get(url + "users")
    if r.status_code != 200:
        msg = "An error occured when getting all users"
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)
    return r.json()


def get_user_library(user_id):
    r = requests.get(url + "users/" + str(user_id) + "/library")
    if r.status_code == 404:
        msg = "Getting user library with ID {} could not be found".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)
    elif r.status_code != 200:
        msg = "Getting user library with ID {} encountered an error".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)
    return r.json()


def get_game_achievements(user_id, game_id):
    r = requests.get(url + "users/" + str(user_id) + "/achievements/" + str(game_id))
    if r.status_code == 404:
        msg = "Getting user achievements with ID {} or game with ID {} could not be found".format(
            user_id, game_id
        )
        raise UserDataNotFoundError(msg, r.status_code)
    elif r.status_code != 200:
        msg = "Getting user achievements with ID {} or game with ID {} encountered an error".format(
            user_id, game_id
        )
        raise UserDataNotFoundError(msg, r.status_code)
    return r.json()
