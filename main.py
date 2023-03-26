
from trello import * 
from github import * 

""" doing_id = get_trello_list_id("Doing")

card_id = get_card_id_by_name("find api")

list_id = get_trello_list_id("Doing") """


for item in load_commits():
    
    if "doing" in item.lower():
        # move the card to doing list ...
        list_id = get_trello_list_id("Doing")
        commit_message = item.split(":")
        if len(commit_message) == 1:
            message = commit_message[0]
        else:
            message = commit_message[1].trim()
        card_id = get_card_id_by_name(message)
        move_trello_card(card_id=card_id, list_id=list_id)
    
    elif "done" in item.lower():
        # move the card to doing list ...
        list_id = get_trello_list_id("Done")
        commit_message = item.split()
        card_id = get_card_id_by_name(commit_message)
        move_trello_card(card_id=card_id, list_id=list_id)


