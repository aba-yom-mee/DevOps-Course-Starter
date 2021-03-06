import requests
import os
from dotenv import load_dotenv
from requests.api import request
load_dotenv(".env")

api_key =os.getenv('TRELLO_API_KEY')
api_token =os.getenv('TRELLO_API_TOKEN')
idList=os.getenv('TODO_idList')

host = "https://api.trello.com/1"

def make_trello_auth(url):
    """ Attempting to make a trello connection with key and token. """
    trello_url =f"{url}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
    return(trello_url)

def get_cards_url_with_auth():
    trello_host = "https://api.trello.com/1/cards"
    card_url =f"{trello_host}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
    return(card_url)


def get_items():
    """ Simple attempt to get all cards from Trello. """
    request_url = make_trello_auth(f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards")
    response = requests.get(request_url)
    todos = response.json()
    for card in todos:
        print(card['name'], card['desc'])
    return todos


def get_done_items():
    """ Simple attempt to get all done cards from Trello. """
    params = {"key":  os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.get(
        f"https://api.trello.com/1/lists/{os.getenv('DONE_idList')}/cards", params=params)

    dones = response.json()
    for card in dones:
        print(card['name'], card['desc'])
    return dones


def get_doing_items():
    """ Simple attempt to get all done cards from Trello. """
    params = {"key":  os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.get(
        f"https://api.trello.com/1/lists/{os.getenv('DOING_idList')}/cards", params=params)

    doings = response.json()
    for card in doings:
        print(card['name'], card['desc'])
    return doings


def get_todo_items():
    """ Simple attempt to get all done cards from Trello. """
    params = {"key":  os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.get(
        f"https://api.trello.com/1/lists/{os.getenv('TODO_idList')}/cards", params=params)

    todos = response.json()
    for card in todos:
        print(card['name'], card['desc'])
    return todos


def add_new_item(name, desc):
    create_new_card = {'idList': os.getenv(
        'TODO_idList'), 'name': name, 'desc': desc}
    response = requests.post(get_cards_url_with_auth(), params=create_new_card)
    return response


def update_item(id):
    params = {"key": os.getenv('TRELLO_API_KEY'), "token": os.getenv(
        'TRELLO_API_TOKEN'), "idList": os.getenv('DONE_idList')}
    response = requests.put(
        f"https://api.trello.com/1/cards/{id}", params=params)
    return response


def delete_item(id):
    params = {"key": os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.delete(
        f"https://api.trello.com/1/cards/{id}", params=params)
    return response

def create_a_board(name):
    params = {"key": os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN'), "name": name}
    response = requests.post(
        f"https://api.trello.com/1/boards", params=params)
    return response.json()["id"]
             

def delete_a_board(id):
    params = {"key": os.getenv('TRELLO_API_KEY'),
              "token": os.getenv('TRELLO_API_TOKEN'),}
    response = requests.delete(
        f"https://api.trello.com/1/boards/{id}", params=params)
    return response
