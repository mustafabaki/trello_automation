import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
# Trello API credentials
TRELLO_API_KEY = os.environ["TRELLO_API_KEY"]
TRELLO_API_TOKEN = os.environ["TRELLO_API_TOKEN"]
TRELLO_BOARD_ID = os.environ["TRELLO_BOARD_ID"]


# Trello API URLs
TRELLO_API_BASE_URL = 'https://api.trello.com/1'
TRELLO_CARDS_URL = f'{TRELLO_API_BASE_URL}/boards/{TRELLO_BOARD_ID}/cards'
TRELLO_LISTS_URL = f'{TRELLO_API_BASE_URL}/boards/{TRELLO_BOARD_ID}/lists'
TRELLO_SEARCH_URL = f'{TRELLO_API_BASE_URL}/search'

def get_trello_list_id(list_name):
    # Get the ID of the Trello list with the given name
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_API_TOKEN
    }
    response = requests.get(TRELLO_LISTS_URL, params=params)
    lists = json.loads(response.text)
    for trello_list in lists:
        if trello_list['name'] == list_name:
            return trello_list['id']
    return None



def create_trello_card(list_id, card_name, card_desc=''):
    # Create a new Trello card on a list
    url = f'{TRELLO_API_BASE_URL}/cards'
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_API_TOKEN,
        'idList': list_id,
        'name': card_name,
        'desc': card_desc
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f'Error creating card: {response.text}')
    else:
        card_id = response.json()['id']
        print(f'Successfully created card {card_name} with ID {card_id} on list {list_id}')
        return card_id



def move_trello_card(card_id, list_id):
    # Move a Trello card to a new list
    url = f'{TRELLO_API_BASE_URL}/cards/{card_id}'
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_API_TOKEN,
        'idBoard': TRELLO_BOARD_ID,
        'idList': list_id
    }
    response = requests.put(url, params=params)
    if response.status_code != 200:
        print(f'Error moving card {card_id}: {response.text}')
    else:
        print(f'Successfully moved card {card_id} to list {list_id} on board {TRELLO_BOARD_ID}')


def get_card_id_by_name(card_name):
    # Search for a card by name and return its ID
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_API_TOKEN,
        'query': card_name,
        'idBoards': TRELLO_BOARD_ID,
        'modelTypes': 'cards',
        'card_fields': 'id,name'
    }
    response = requests.get(TRELLO_SEARCH_URL, params=params)
    print(response.json())
    results = response.json()['cards']
    for card in results:
        if card['name'] == card_name:
            return card['id']
    return None
