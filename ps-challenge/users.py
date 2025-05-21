import requests


def get_all_users():
    r = requests.get("http://127.0.0.1:8080/users")
    print(r.content)


def get_user_library(user_id):
    r = requests.get("http://127.0.0.1:8080/users/" + user_id + "/library")
    print(r.content)


def get_game_achievements(user_id, game_id):
    r = requests.get(
        "http://127.0.0.1:8080/users/" + user_id + "/achievements/" + game_id
    )
    print(r.content)
