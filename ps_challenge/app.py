import logging

from flask import Flask, make_response, request

from ps_challenge.controller import (
    get_user_achievement_level,
    get_all_users_achievement_levels,
)
from ps_challenge.exceptions import UserDataNotFoundError


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.get("/users")
def get_all_users_levels():
    try:
        app.logger.info("Received get for all users")
        return get_all_users_achievement_levels(request.args.get("level", None))
    except UserDataNotFoundError as err:
        resp = make_response(
            {"message": err.msg, "status_code": err.status_code}, err.status_code
        )
        return resp


@app.get("/users/<int:user_id>")
def get_user_level(user_id):
    try:
        app.logger.info("Received get for user with ID %s", user_id)
        return get_user_achievement_level(user_id)
    except UserDataNotFoundError as err:
        resp = make_response(
            {"message": err.msg, "status_code": err.status_code}, err.status_code
        )
        return resp
