# BattleShip Atlantic 

BattleShip Atlantic is a Python terminal mini game which runs on Heroku. It is based of the popular board game battleships - Battleship is a strategy type guessing game. It is played on ruled grids on which player's fleet of warships are marked. The locations of the fleets are concealed. 

As the game was developed in Python for the use in a terminal, 
it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

Users compete against the Computer to try and sink each others battleships, The first to destroy all battleships is the winner. 
#
There are 5 different type of ships to SINK,
- **DESTROYER** (takes 6 spaces on the map)
- **GREYHOUND** (takes 5 spaces on the map)
- **DICKY** (takes 4 spaces on the map)
- **SUBMARINE** (takes 3 spaces on the map) 
- **ESCORT** (takes 2 spaces on the map).
#
The player gets to places their ***5 ships*** on the map & the ***computer randomly*** chooses where he wants to put all his ships, Then the game begins. 

Live link found here - <a href="https://battleship-atlantic.onrender.com/" target="_blank">Battleship Atlantic</a>

#

<img width="442" alt="Battleship Atlantic" src="https://user-images.githubusercontent.com/92300013/157437496-4c74d947-7e99-42e4-b7f2-04f3a37cc192.png">

#

## How To Play 
- The player places their 5 ships on the map.
- When all ships have been placed on the map the battle begins
- The player guesses the co-ordinates of the computers ships & the computer guesses where the player placed their ships.
- The first to destroy all ships wins the game.

<img width="730" alt="Instructions" src="https://user-images.githubusercontent.com/92300013/157858098-4e194d89-084d-4f68-9f9d-dedc5c4f6ebb.png">

# Features 

## Existing features 

* The welcome message 
  * The user is met with a colour coded sections of ASCII art (Battleships Atlantic) with a ship. 
  * When the users starts the game, a welcome message is diplayed.
  * A breif desciption of the game includes different types of ship, map size, total number of hits needed to win (20) and the key maker.
  * It also contains the instructions in how to play the game.

<img width="729" alt="Welcome" src="https://user-images.githubusercontent.com/92300013/157857979-d5b9c00b-265b-4ad1-be8e-a272001bea9e.png">

<img width="340" alt="Different ships" src="https://user-images.githubusercontent.com/92300013/157858163-a91aa939-ef7e-4836-a63a-323954410974.png">

<img width="208" alt="Keys" src="https://user-images.githubusercontent.com/92300013/157444803-407e8a58-dcb5-4686-8e11-b33f4757219c.png">

#
* The Map
  * Once instructions are shown, the player's map is created, which is displayed in the terminal. The user is prompted to place each ship in turn from smallest to largest (2-6), the ship size is shown in the terminal.
  * Orientation, row followed by column inputs are requested for the ship location, Horizontal or Vertical postioning followed by row and column input.All having validation checks on them. Overlap and fit checks are ran on the input location for the ships.
  * Once  all of the inputs are entered and valid the ship is placed on the players map, their map is then printed to remember where placed ship for reference when placing the next. The computers ships are randomly placed on their map before the player places their ships are.
  
<img width="317" alt="Start Game map" src="https://user-images.githubusercontent.com/92300013/157447022-2f1b44b3-819d-4928-b67e-d38357bf291e.png">

<img width="307" alt="Place Ship size 2" src="https://user-images.githubusercontent.com/92300013/157657591-3436f35b-84c9-41f8-b93a-4a6619e42123.png">

<img width="325" alt="place ship size 5" src="https://user-images.githubusercontent.com/92300013/157657717-72c1b8af-37b2-46b0-b23c-a82acda0366c.png">

* The Guess Map
  * Once the ships have been placed on each map the game play begins.
  * The player always goes first, their guess map is printed out to them for reference.
  * Once a valid input is entered the result of their attack is printed out. The computers guess is printed out to the user with the computers map of where the player hit for reference to see where there shot landed. Validation checks prevent the user repeating guessed spots on the map.
 
 <img width="185" alt="guess miss" src="https://user-images.githubusercontent.com/92300013/157658651-92b974ac-0c82-4e79-9dbc-098c60a79c21.png">

 <img width="347" alt="guess ship" src="https://user-images.githubusercontent.com/92300013/157658703-ba946e23-0667-4994-b989-8f0e4bd8b791.png">

 <img width="223" alt="Hit message" src="https://user-images.githubusercontent.com/92300013/157674858-a50f5123-c185-4d64-8021-491a0824fd11.png">

 <img width="309" alt="Hit X Message" src="https://user-images.githubusercontent.com/92300013/158357717-d79c9329-13c4-4c94-b1b2-f4e1a87b5170.png">

 <img width="569" alt="Win game message" src="https://user-images.githubusercontent.com/92300013/158187014-a2235b21-abc3-4890-b1c4-101584840701.png">

* Ship Display "∆"
  * Ships that haven't been hit are displayed on the player's board as the at sign "∆".
  * Letters are used for the columns and numbers for the rows, this allows for easy differentiation when inputting coordinates. Just like in the battleship game. 
  * The KEYS that have been used give a good level of contrast.
  "∆" to represent ships, 
  "-" for a miss,
  "X" for a hit.

# Features left to implement
- There are no features left to implement from the initial scope of my project. I do have a few ideas on what I could do to improve the game. 

- A bigger map with more ships. Have different levels to play on - easy , medium , hard
Make a play again button. 

- I would have a different layout for the maps, rather them side by side.

- I would like to have only one guess map for eveytime you guess. Instead of the terminal printing a new one with your guess. Just use the same guess map. 

# Validator Testing
- HTMl - Not for this project scope.

- CSS - Not for this project scope.

- JS - Not for this project scope.

- Python - No major errors were found when passing through the <a href="http://pep8online.com/checkresult" target="_blank">PEP8</a> Validator tool

- Lighthouse - Not for this project scope.

# Deployment
The site was deployed via Heroku, and the live link can be found here - <a href="https://battleships-atlantic.herokuapp.com/" target="_blank">Battleship Atlantic</a>

## Project Deployment
To deploy the project through Heroku I followed these steps:

1. Sign up / Log in to <a href="https://id.heroku.com/login" target="_blank">Heroku</a>
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

# Bugs
## Solved 
- I had a problem with the way my game would start. It didnt start in the right order until I went back to make changes to the order of the code. 

- no Bugs remaining 

# Credits 

When researching on how to use colour in the terminal I came across an article in <a href="https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println" target="_blank"> Stackoverflow </a> which showed me how to implement colours in the terminal and to reset them back. 

Ascii art - The logo Battleship atlanic was design here <a href="http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20" target="_blank"> ASCII ART </a> and the Ship design came from <a href="https://www.asciiart.eu/vehicles/boats" target="_blank"> ASCII ART BOAT </a>