# trello_automation
 The repo contains codes for automation of cards in a Trello board.


 You can automate your board on Trello by only pushing commits to GitHub using this repository. 

 For example, if you have a card item on Trello with name "change the title" and push commit with name "doing: change the title", it will automatically move that specific card to the Doing list on your Trello board. If the commit message is "done: change the title", then this card will be automatically moved to Done list. 

 For this purpose, you will need your Trello API key, token and board id as well as your GitHub username and the repository that this action will be executed on. You should set these variables in repository's secrets section. The secret names have to match with the ones in the code. Please refer to the variable names in `trello.py` and `github.py` for this purpose. 

Also, do not forget to copy the file `.github\workflows\main.yml` under `.github\workflows`. 


After setting everything correctly, the action will be triggered everytime you push on GitHub, the cards will be automatically moving.

This code assumes that you have already created the cards in To Do list on board and the board only has To Do, Doing and Done lists.

Don't hesitate to clone and customize it according to your needs!
 