# BattleShip Atlantic 

BattleShip Atlantic  is a Python terminal mini game which runs on Heroku. It is based on the popular board game battleships more info on the game can be found below.

As the game was developed in Python for use in the terminal, 
it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.
#
Users compete against the Computer to try and sink each others battleships, The first to destroy all battleships is the winner. 

There are 5 different type of ships to SINK,
- **DESTROYER** (takes 5 spaces on the board)
- **GREYHOUND** (takes 4 spaces on the board)
- **DICKY** (takes 3 spaces on the board)
- **SUBMARINE** (takes 3 spaces on the board) 
- **ESCORT** (takes 2 spaces on the board).
#
The player gets to places their ***5 ships*** on the map & the computer randomly chooses where he wants to put all his ships, Then the game begins. 

Live link found here - <a href="https://battleships-atlantic.herokuapp.com/" target="_blank">Battleship Atlantic</a>

#

<img width="442" alt="Battleship Atlantic" src="https://user-images.githubusercontent.com/92300013/157437496-4c74d947-7e99-42e4-b7f2-04f3a37cc192.png">

#

# Description

## How To Play 
- The player places their 5 ships on the map.
- When all ships have been placed on the board the battle begins
- The player guesses the co-ordinates of the computers ships & the computer guesses where the player placed their ships.
- The first to destroy all ships wins the game.

# Features 

## Existing features 

* The welcome message 
  * The user is met with colour coded sections of ASCII art (Battleships Atlantic) with a ship. 
  * When the users starts the game, a welcome message is diplayed.
  * A breif desciption of the game includes different types of ship, map size, total number of hits needed to win (17) and the key maker.
  * It also contains the instructions in how to play the game.

<img width="731" alt="Welcome to" src="https://user-images.githubusercontent.com/92300013/157438257-6e5522c3-9ca4-4663-b9d6-823981edc0e2.png">

<img width="321" alt="Different Ships" src="https://user-images.githubusercontent.com/92300013/157444602-0aa63ab4-d804-4f67-b3e0-d3d50e61f532.png">

<img width="208" alt="Keys" src="https://user-images.githubusercontent.com/92300013/157444803-407e8a58-dcb5-4686-8e11-b33f4757219c.png">

#
  
<img width="317" alt="Start Game map" src="https://user-images.githubusercontent.com/92300013/157447022-2f1b44b3-819d-4928-b67e-d38357bf291e.png">

# Validator Testing
- HTMl - Not within project scope.

- CSS - Not within project scope.

- JS - Not within project scope.

- Python - No errors were found when passing through the PEP8 Validator tool

- Lighthouse - Not within project scope.

# Deployment
The site was deployed via Heroku, and the live link can be found here - <a href="https://battleships-atlantic.herokuapp.com/" target="_blank">Battleship Atlantic</a>

## Project Deployment
To deploy the project through Heroku I followed these steps:

1. Sign up / Log in to Heroku
2. From the main Heroku Dashboard page select 'New' and then 'Create New App'
3. Give the project a name - I entered Battleships and select a suitable region, then select create app. The name for the app must be unique.
4. This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
5. This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
6. In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
7. In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
8. Next select the add buildpack button below the config vars section.
9. In the pop-up window select Python as your first build pack and select save changes.
10. Then repeat the steps to add a node.js buildpack.
11. The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
12. Next navigate back to the deploy tab using the submenu at the top of the page.
13. In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
14. In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
15. Once Heroku has located the repo select connect.
16. This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
17. In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
18. This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
19. Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.
