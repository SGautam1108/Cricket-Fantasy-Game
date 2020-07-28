# Cricket-Fantasy-Game
## **Introduction-**

Cricket Fantasy is a virtual game where you can create your own team of real cricket players and score points based on their performance in the upcoming matches. The ultimate aim is to achieve as much score as possible while restraining to the limits on points available to select the players.

## **About the Project-**

The Cricket-Fantasy-Game combines knowledge of Python at its core with PyQt5 as GUI builder and SQL for querying the database of players, matches and teams.
This project helps you to relive the experience of being a Cricket Fan as well understand the effective combination of GUI, Python and SQL.

## How to Play?!-
1.	**Initial Steps-**
    *	First and foremost, complete all the requirements as mentioned in Instruction Manual
    *	Run Main.py to play the game
    *	A Window pops up with the Cricket Fantasy Logo
    *	Since no team has been created, all information is marked ### and buttons disabled
    *	Follow the next steps
2.	**Create a team-**
    *	Go to Menu->CREATE Team or CTRL + N to create a new team
    *	Enter team name in the dialog box that appears
    *	Team name appears on the Main Window 
    *	Total points to select team members are 1100. Each player has a specific value to him and SO, USE THE POINT WISELY!!
3.	**Select team players-**
    *	Select a category -> Batsmen, Bowler, All-Rounder or Wicket-Keeper, to select players from. The first box gets filled with the players of that category.
    *	To select, simply double click the player’s name and it will get added to box 2 i.e. ‘Team players’ list. Points are also deducted based on the value of the player bought.
    *	If somehow you don’t adhere to the game logic (as mentioned in next section), an information dialog will appear. So free your mind from that task!!
    *	To remove the player, simply double click again in your list and the player is added back to the ‘Available Players’ list.
4.	**See Stats-**
    *	While selecting, you can refer to the ‘See Stats’ button.
    *	This opens a dialog box. Select the player, from drop down menu, whose stats you wish to see.
    *	Another window opens and the stats are shown along with info of the player value and category.
5.	**Save Team-**
    *	Menu->SAVE Team or CTRL + S helps your way through.
    *	If the team already exists, a prompt asks if you wish to overwrite. If not, then another prompt asks you to rename your team.
    *	If saved, ‘Operation Successful’ dialog box appears. Congratulations!!
6.	**Open Team-**
    *	The team you created will remain in the foreground. But if you wish to restart the program or have another team previously saved…  go to Menu->OPEN Team or press CTRL + O.
    *	A prompt gives a drop-down menu for you to select a team to open.
    *	The Team name and players are populated in the Main Window along with values.
    *	If you wish, you can edit it and save again by overwriting.
7.	**Evaluating Team-**
    *	Go to Menu->EVALUATE Team or CTRL + E.
    *	An Evaluation Window pops up.
    *	First, select your team from drop down menu
    *	Next, select match you wish to evaluate the performance on.
    *	This will populate the first box with team players and second box with points each player has earned.
    *	Finally, click Calculate Score and total points are shown
    *	Congratulations! Hope your team did well there. If you want to improve, go back and edit your team, and re-evaluate!!
8.	**Quit the App-**
    *	Go to Menu->Quit
    *	If you haven’t saved your team, a prompt asks for you to save it. So, no fear of losing your progress!!

## Rules of the Game-
* ### Rules regarding game logic-
    *	Total players must be 11. No more, no less
    *	Batsmen in a team may be 3 or 4.
    *	Bowlers must be greater than equal 2 and less than equal 4.
    *	Number of all-rounders must lie in range 2 to 4 as well.
    *	Only one wicket-keeper is allowed and each team must have one! (Obvio)
* ### Rules regarding evaluating players-
    * #### 1.	Batting-
        *	1 point for every 2 runs scored
        *	2 points for each four
        *	4 points for every over the boundary shot (six)
        *	5 points for every half-century in the game
        *	10 additional points for every century. Note – a complete century will not be considered for half-centuries.
        *	2 points for Strike Rate (Runs/Balls faced) over 80
        *	10 additional points for strike rate above 100
    * #### 2.	Bowling-
        *	4 points for each wicket taken
        *	2 points for each maiden over
        *	5 points for 4 wickets (4w) in an inning
        *	10 points for 5 wickets (5w) in an inning
        *	10 points if Economy (Runs given/ over) less than 2
        *	7 points if economy less than 3.5
        *	4 points if economy less than 5
    * #### 3.	Fielding-
        *	5 points each for catches, stumpings and run-outs


## Internal Working-

* #### 1.	**Python and PyQt5-**
    Python is at the core of the application. It combines together PyQt5 and MySQL. Various functions have been created to deal with each logic and click listeners from PyQt5 Widgets separately. 
    PyQt5 creates three windows- Main, Evaluate and Stats using Python Classes and using modules QtGui, QtWidgets etc. from PyQt5 module.
    Main.py contains the main logic while logic connected to Evaluate and Stats Windows are in their respective files.
* #### 2.	**MySQL-**
    MySQL DBMS has been used along with ‘mysql-connector-python’ module to create tables and request data from queries in Python.
    Following tables were used-
    1.	**Stats-** This is the main table with data for each player including ‘player_id’, ‘name’, ‘value’, category and other stats. Primary key is ‘player_id’.
    2.	**Teams-** This table contains information about the teams created by users along with total points used.
    3.	**Match1-5-** Each table contains performance of players in 5 different matches. ‘player_id’ acts as a foreign key to link player data from stats entity.

#### Note-
The application can be run using SQLite as well. Instead of importing ‘mysql.connector’, simply import ‘sqlite3’. Also, now we don’t require to pass information about host, user or password. Just the database.
To create the database, create a schema in ‘SQLiteStudio’ and then run all the queries in ‘cricketfantasy.sql’. This will create a new database with ‘.db’ extension. Simply, use this!!
