import logging
import requests

import ps_challenge.config
from ps_challenge.exceptions import UserDataNotFoundError

logger = logging.getLogger("ps_challenge.app")

url = ps_challenge.config.users_api_url


def get_all_users():
    endpoint = url + "users"
    logger.debug("Getting all users from endpoint {}".format(endpoint))

    r = requests.get(endpoint)
    if r.status_code != 200:
        msg = "Error received from users API"
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)

    return r.json()


def get_user_library(user_id):
    endpoint = url + "users/" + str(user_id) + "/library"
    logger.debug("Getting user library from endpoint {}".format(endpoint))

    r = requests.get(endpoint)
    if r.status_code == 404:
        msg = "Not found error from users API ID {}".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)
    elif r.status_code != 200:
        msg = "Error received from users API with ID {}".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)

    return r.json()


def get_game_achievements(user_id, game_id):
    endpoint = url + "users/" + str(user_id) + "/achievements/" + str(game_id)
    logger.debug(
        "Getting user game completed achievements from endpoint {}".format(endpoint)
    )

    r = requests.get(endpoint)
    if r.status_code == 404:
        msg = "Not found error from users API with user ID {} and game ID {}".format(
            user_id, game_id
        )
        raise UserDataNotFoundError(msg, r.status_code)
    elif r.status_code != 200:
        msg = "Error received from users API with user ID {} and game ID {}".format(
            user_id, game_id
        )
        raise UserDataNotFoundError(msg, r.status_code)

    return r.json()
