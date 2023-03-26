
from trello import * 
from github import * 


for item in load_commits():
    
    if "doing" in item.lower():
        # move the card to doing list ...
        list_id = get_trello_list_id("Doing")
        commit_message = item.split(":")
        message = commit_message[1].strip()
        if ':' not in item:
            raise ValueError("the commit message is not a valid commit message")
        card_id = get_card_id_by_name(message)
        move_trello_card(card_id=card_id, list_id=list_id)
    
    elif "done" in item.lower():
        # move the card to doing list ...
        list_id = get_trello_list_id("Done")
        commit_message = item.split()
        card_id = get_card_id_by_name(commit_message)
        move_trello_card(card_id=card_id, list_id=list_id)



