import json
import logging

from flask import Flask, make_response, request
from flask_swagger_ui import get_swaggerui_blueprint

import ps_challenge.config
from ps_challenge.controller import (
    get_user_achievement_level,
    get_all_users_achievement_levels,
)
from ps_challenge.exceptions import UserDataNotFoundError


logging.basicConfig(level=ps_challenge.config.log_level)

app = Flask(__name__)

SWAGGER_JSON = json.load(open(ps_challenge.config.swagger_json_path, "r"))
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    "/docs",
    "/swagger.json",
    config={"spec": SWAGGER_JSON},
)
app.register_blueprint(SWAGGERUI_BLUEPRINT)


@app.get("/users")
def get_all_users_levels():
    """GET endpoint to return all users with their achievement level calculated."""
    try:
        app.logger.info("Get all users")
        return get_all_users_achievement_levels(request.args.get("level", None))
    except UserDataNotFoundError as err:
        resp = make_response(
            {"message": err.msg, "status_code": err.status_code}, err.status_code
        )
        return resp


@app.get("/users/<int:user_id>")
def get_user_level(user_id):
    """GET endpoint to return a user with their achievement level calculated."""
    try:
        app.logger.info("Get user with ID %s", user_id)
        return get_user_achievement_level(user_id)
    except UserDataNotFoundError as err:
        resp = make_response(
            {"message": err.msg, "status_code": err.status_code}, err.status_code
        )
        return resp
