import logging
import requests

import ps_challenge.config
from ps_challenge.exceptions import UserDataNotFoundError

logger = logging.getLogger("ps_challenge.app")

url = ps_challenge.config.users_api_url


def get_all_users():
    """Returns a list of user objects from the configured API."""
    endpoint = url + "users"
    logger.debug("Getting all users from endpoint {}".format(endpoint))

    r = requests.get(endpoint)
    if r.status_code != 200:
        msg = "Error received from users API"
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)

    return r.json()


def get_user_library(user_id):
    """Returns a single user games library from the configured API.

    Arguments:
    user_id -- (str) Unique ID for the specific user's library
    """
    endpoint = "{}users/{}/library".format(url, user_id)
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
    """Returns a single user's completed achievements for one game from the configured API.

    Arguments:
    user_id -- (str) Unique ID for the specific user
    game_id -- (str) Unique ID for the specific game
    """
    endpoint = "{}users/{}/achievements/{}".format(url, user_id, game_id)
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
