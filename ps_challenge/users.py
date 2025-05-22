import requests

url = "http://127.0.0.1:8080/"


def get_all_users():
    r = requests.get(url + "users")
    raise NotImplementedError


def get_user_library(user_id):
    r = requests.get(url + "users/" + str(user_id) + "/library")
    raise NotImplementedError


def get_game_achievements(user_id, game_id):
    r = requests.get(url + "users/" + str(user_id) + "/achievements/" + str(game_id))
    raise NotImplementedError
