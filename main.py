
from trello import * 
from github import * 

""" doing_id = get_trello_list_id("Doing")

card_id = get_card_id_by_name("find api")

list_id = get_trello_list_id("Doing") """


for item in load_commits():
    print(item)