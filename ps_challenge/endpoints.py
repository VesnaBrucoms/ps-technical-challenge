from flask import Flask

from ps_challenge.controller import get_user_achievement_level

app = Flask(__name__)


@app.route("/")
def get_all_users():
    return {}


@app.get("/users")
def get_all_users_levels():
    return {}


@app.get("/users/<int:user_id>")
def get_user_level(user_id):
    return get_user_achievement_level(user_id)
