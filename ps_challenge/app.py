import json
import logging

from flask import Flask, make_response, request, send_file
from flask_swagger_ui import get_swaggerui_blueprint

from ps_challenge.controller import (
    get_user_achievement_level,
    get_all_users_achievement_levels,
)
from ps_challenge.exceptions import UserDataNotFoundError


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


SWAGGER_JSON = json.load(open("static/swagger.json", "r"))

swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs",
    "/swagger.json",
    config={"spec": SWAGGER_JSON},
)

app.register_blueprint(swaggerui_blueprint)


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
