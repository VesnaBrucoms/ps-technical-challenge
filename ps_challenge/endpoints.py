import controller
from app import app


@app.get("users/")
def get_all_users():
    return {}


@app.get("users/{user_id}")
def get_user(user_id):
    return controller.get_user_achievement_level(user_id)
