from PyQt5 import QtCore, QtGui, QtWidgets

from Evaluate import Ui_EvaluateWindow as EvaluateWindow
from Stats import Ui_StatsWindow as StatsWindow

import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd = 'Pass@1234', database ='cricketfantasy')

# better to create individual cursors to prevent data override

class Ui_MainWindow(object):

    def __init__(self):
        self.bat = 0
        self.bowl = 0
        self.ar = 0
        self.wk = 0
        self.avl = 1100
        self.value = 0
        self.isSaved = False


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 746)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainYourSelectionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainYourSelectionLabel.sizePolicy().hasHeightForWidth())
        self.mainYourSelectionLabel.setSizePolicy(sizePolicy)
        self.mainYourSelectionLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.mainYourSelectionLabel.setFont(font)
        self.mainYourSelectionLabel.setObjectName("mainYourSelectionLabel")
        self.verticalLayout_3.addWidget(self.mainYourSelectionLabel)
        self.Type_HL = QtWidgets.QHBoxLayout()
        self.Type_HL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Type_HL.setObjectName("Type_HL")
        self.mainBatsmenLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainBatsmenLabel.setFont(font)
        self.mainBatsmenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainBatsmenLabel.setObjectName("mainBatsmenLabel")
        self.Type_HL.addWidget(self.mainBatsmenLabel)
        self.mainBatCount = QtWidgets.QLabel(self.centralwidget)
        self.mainBatCount.setObjectName("mainBatCount")
        self.Type_HL.addWidget(self.mainBatCount)
        self.mainBowlersLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainBowlersLabel.setFont(font)
        self.mainBowlersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainBowlersLabel.setObjectName("mainBowlersLabel")
        self.Type_HL.addWidget(self.mainBowlersLabel)
        self.mainBowCount = QtWidgets.QLabel(self.centralwidget)
        self.mainBowCount.setObjectName("mainBowCount")
        self.Type_HL.addWidget(self.mainBowCount)
        self.mainAllRoundersLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainAllRoundersLabel.setFont(font)
        self.mainAllRoundersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainAllRoundersLabel.setObjectName("mainAllRoundersLabel")
        self.Type_HL.addWidget(self.mainAllRoundersLabel)
        self.mainARCount = QtWidgets.QLabel(self.centralwidget)
        self.mainARCount.setObjectName("mainARCount")
        self.Type_HL.addWidget(self.mainARCount)
        self.mainWicketKeeperLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainWicketKeeperLabel.setFont(font)
        self.mainWicketKeeperLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainWicketKeeperLabel.setObjectName("mainWicketKeeperLabel")
        self.Type_HL.addWidget(self.mainWicketKeeperLabel)
        self.mainWKCount = QtWidgets.QLabel(self.centralwidget)
        self.mainWKCount.setObjectName("mainWKCount")
        self.Type_HL.addWidget(self.mainWKCount)
        self.verticalLayout_3.addLayout(self.Type_HL)
        self.Points_HL = QtWidgets.QHBoxLayout()
        self.Points_HL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Points_HL.setObjectName("Points_HL")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.Points_HL.addItem(spacerItem)
        self.mainPointsAvailable = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPointsAvailable.sizePolicy().hasHeightForWidth())
        self.mainPointsAvailable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainPointsAvailable.setFont(font)
        self.mainPointsAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPointsAvailable.setObjectName("mainPointsAvailable")
        self.Points_HL.addWidget(self.mainPointsAvailable)
        self.mainPtsAvailCount = QtWidgets.QLabel(self.centralwidget)
        self.mainPtsAvailCount.setObjectName("mainPtsAvailCount")
        self.Points_HL.addWidget(self.mainPtsAvailCount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Points_HL.addItem(spacerItem1)
        self.mainPointsUsed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPointsUsed.sizePolicy().hasHeightForWidth())
        self.mainPointsUsed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainPointsUsed.setFont(font)
        self.mainPointsUsed.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPointsUsed.setObjectName("mainPointsUsed")
        self.Points_HL.addWidget(self.mainPointsUsed)
        self.mainPtsUsedCount = QtWidgets.QLabel(self.centralwidget)
        self.mainPtsUsedCount.setObjectName("mainPtsUsedCount")
        self.Points_HL.addWidget(self.mainPtsUsedCount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.Points_HL.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.Points_HL)
        self.List_HL = QtWidgets.QHBoxLayout()
        self.List_HL.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.List_HL.setObjectName("List_HL")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.List_HL.addItem(spacerItem3)
        self.Entry_VL = QtWidgets.QVBoxLayout()
        self.Entry_VL.setObjectName("Entry_VL")
        self.Entry_HL = QtWidgets.QHBoxLayout()
        self.Entry_HL.setObjectName("Entry_HL")
        self.mainRadioBat = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainRadioBat.sizePolicy().hasHeightForWidth())
        self.mainRadioBat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainRadioBat.setFont(font)
        self.mainRadioBat.setObjectName("mainRadioBat")
        self.Entry_HL.addWidget(self.mainRadioBat)
        self.mainRadioBow = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainRadioBow.setFont(font)
        self.mainRadioBow.setObjectName("mainRadioBow")
        self.Entry_HL.addWidget(self.mainRadioBow)
        self.mainRadioAR = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainRadioAR.setFont(font)
        self.mainRadioAR.setObjectName("mainRadioAR")
        self.Entry_HL.addWidget(self.mainRadioAR)
        self.mainRadioWK = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainRadioWK.setFont(font)
        self.mainRadioWK.setObjectName("mainRadioWK")
        self.Entry_HL.addWidget(self.mainRadioWK)
        self.Entry_VL.addLayout(self.Entry_HL)
        self.mainAllPlayers = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainAllPlayers.sizePolicy().hasHeightForWidth())
        self.mainAllPlayers.setSizePolicy(sizePolicy)
        self.mainAllPlayers.setMinimumSize(QtCore.QSize(200, 500))
        self.mainAllPlayers.setObjectName("mainAllPlayers")
        self.Entry_VL.addWidget(self.mainAllPlayers)
        self.mainAvailPlayLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mainAvailPlayLabel.setFont(font)
        self.mainAvailPlayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainAvailPlayLabel.setObjectName("mainAvailPlayLabel")
        self.Entry_VL.addWidget(self.mainAvailPlayLabel)
        self.List_HL.addLayout(self.Entry_VL)
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.arrow.setFont(font)
        self.arrow.setObjectName("arrow")
        self.List_HL.addWidget(self.arrow)
        self.Team_VL = QtWidgets.QVBoxLayout()
        self.Team_VL.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.Team_VL.setObjectName("Team_VL")
        self.Name_HL = QtWidgets.QHBoxLayout()
        self.Name_HL.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Name_HL.setSpacing(4)
        self.Name_HL.setObjectName("Name_HL")
        self.mainTeamName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainTeamName.setFont(font)
        self.mainTeamName.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTeamName.setObjectName("mainTeamName")
        self.Name_HL.addWidget(self.mainTeamName)
        self.mainTeamNameDisp = QtWidgets.QLabel(self.centralwidget)
        self.mainTeamNameDisp.setObjectName("mainTeamNameDisp")
        self.Name_HL.addWidget(self.mainTeamNameDisp)
        self.Team_VL.addLayout(self.Name_HL)
        self.mainTeamPlayers = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainTeamPlayers.sizePolicy().hasHeightForWidth())
        self.mainTeamPlayers.setSizePolicy(sizePolicy)
        self.mainTeamPlayers.setMinimumSize(QtCore.QSize(0, 500))
        self.mainTeamPlayers.setObjectName("mainTeamPlayers")
        self.Team_VL.addWidget(self.mainTeamPlayers)
        self.mainTeamPlayLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mainTeamPlayLabel.setFont(font)
        self.mainTeamPlayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTeamPlayLabel.setObjectName("mainTeamPlayLabel")
        self.Team_VL.addWidget(self.mainTeamPlayLabel)
        self.List_HL.addLayout(self.Team_VL)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.List_HL.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.List_HL)
        self.stats_HL = QtWidgets.QHBoxLayout()
        self.stats_HL.setObjectName("stats_HL")
        self.SeeStatsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeeStatsBtn.sizePolicy().hasHeightForWidth())
        self.SeeStatsBtn.setSizePolicy(sizePolicy)
        self.SeeStatsBtn.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SeeStatsBtn.setFont(font)
        self.SeeStatsBtn.setFlat(False)
        self.SeeStatsBtn.setObjectName("SeeStatsBtn")
        self.stats_HL.addWidget(self.SeeStatsBtn)
        self.verticalLayout_3.addLayout(self.stats_HL)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Evaluate = QtWidgets.QAction(MainWindow)
        self.Evaluate.setShortcutVisibleInContextMenu(True)
        self.Evaluate.setObjectName("Evaluate")
        self.Quit = QtWidgets.QAction(MainWindow)
        self.Quit.setObjectName("Quit")
        self.menuManage_Teams.addAction(self.New)
        self.menuManage_Teams.addAction(self.Open)
        self.menuManage_Teams.addAction(self.Save)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.Evaluate)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.Quit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # disable all radiobuttons
        self.mainRadioBat.setEnabled(False)
        self.mainRadioBow.setEnabled(False)
        self.mainRadioAR.setEnabled(False)
        self.mainRadioWK.setEnabled(False)

        # Connecting triggers for Menu Actions
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)

        # triggers for radiobuttons
        self.mainRadioBat.toggled.connect(self.list_ctg)
        self.mainRadioBow.toggled.connect(self.list_ctg)
        self.mainRadioWK.toggled.connect(self.list_ctg)
        self.mainRadioAR.toggled.connect(self.list_ctg)

        # add players from ListWidget
        self.mainAllPlayers.itemDoubleClicked.connect(self.removeListPlayers)
        self.mainTeamPlayers.itemDoubleClicked.connect(self.removeTeamPlayers)
        
        # see stats button
        self.SeeStatsBtn.clicked.connect(self.seeStatsMain)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.mainYourSelectionLabel.setText(_translate("MainWindow", "Your Selections-"))
        self.mainBatsmenLabel.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.mainBatCount.setText(_translate("MainWindow", "##"))
        self.mainBowlersLabel.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.mainBowCount.setText(_translate("MainWindow", "##"))
        self.mainAllRoundersLabel.setText(_translate("MainWindow", "AllRounders(AR)"))
        self.mainARCount.setText(_translate("MainWindow", "##"))
        self.mainWicketKeeperLabel.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.mainWKCount.setText(_translate("MainWindow", "##"))
        self.mainPointsAvailable.setText(_translate("MainWindow", "Points Available"))
        self.mainPtsAvailCount.setText(_translate("MainWindow", "##"))
        self.mainPointsUsed.setText(_translate("MainWindow", "Points Used"))
        self.mainPtsUsedCount.setText(_translate("MainWindow", "##"))
        self.mainRadioBat.setText(_translate("MainWindow", "BAT"))
        self.mainRadioBow.setText(_translate("MainWindow", "BOW"))
        self.mainRadioAR.setText(_translate("MainWindow", "AR"))
        self.mainRadioWK.setText(_translate("MainWindow", "WK"))
        self.mainAvailPlayLabel.setText(_translate("MainWindow", "Available Players"))
        self.arrow.setText(_translate("MainWindow", ">>"))
        self.mainTeamName.setText(_translate("MainWindow", "Team Name"))
        self.mainTeamNameDisp.setText(_translate("MainWindow", "##"))
        self.mainTeamPlayLabel.setText(_translate("MainWindow", "Team Players"))
        self.SeeStatsBtn.setText(_translate("MainWindow", "See Stats"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.New.setText(_translate("MainWindow", "NEW Team"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Open.setText(_translate("MainWindow", "OPEN Team"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.Save.setText(_translate("MainWindow", "SAVE Team"))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Evaluate.setText(_translate("MainWindow", "EVALUATE Team"))
        self.Evaluate.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.Quit.setText(_translate("MainWindow", "Quit"))

    # Initialize all the variables
    def initStart(self):
        self.isSaved = False
        self.bat, self.bowl, self.ar, self.wk, self.avl, self.value = 0, 0, 0, 0, 1100, 0
        self.mainRadioBat.setEnabled(True)
        self.mainRadioBow.setEnabled(True)
        self.mainRadioAR.setEnabled(True)
        self.mainRadioWK.setEnabled(True)


    # Menu Function
    def menu(self, action):
        inputTxt = action.text()

        if inputTxt == 'NEW Team':
            self.createTeamMain()
        elif inputTxt == 'OPEN Team':
            self.openTeamMain()
        elif inputTxt == 'SAVE Team':
            self.saveTeamMain()
        elif inputTxt == 'EVALUATE Team':
            self.evaluateTeamMain()
        elif inputTxt == 'Quit':
            self.exit()
    
    # Functions for each create, evaluate and open
    def createTeamMain(self):
        ans, ok = QtWidgets.QInputDialog.getText(MainWindow, "Create Team", "Enter name of team:")
        
        if ans and ok:
            self.initStart()
            self.mainAllPlayers.clear()
            self.mainTeamPlayers.clear()
            self.setValues()
            self.mainTeamNameDisp.setText(ans)

    
    def openTeamMain(self):
        cur = conn.cursor()
        queryTeam = 'Select name from teams;'
        cur.execute(queryTeam)
        data = cur.fetchall()
        teams = [i[0] for i in data]

        if len(teams) == 0:
            self.showMsg('No saved teams', 'Info')
        else:
            teamAns, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Open Team", "Choose a team to open", teams, 0, False)
            
            if teamAns and ok:
                self.initStart()
                self.isSaved = True
                self.mainAllPlayers.clear()
                self.mainTeamPlayers.clear()
                queryPlayers = 'Select players, team_value from teams where name = %s;'
                cur.execute(queryPlayers, (teamAns,))

                teamData = cur.fetchone()
                teamPlayers = teamData[0].split(',')
                self.value = teamData[1]
                self.avl -= self.value

                for name in teamPlayers:
                    queryCateg = "Select ctg from stats where name = %s;"
                    cur.execute(queryCateg, (name,))
                    ctg = cur.fetchone()[0]
                    
                    if ctg == 'BAT':
                        self.bat += 1
                    elif ctg == 'BWL':
                        self.bowl += 1
                    elif ctg == 'WK':
                        self.wk += 1
                    elif ctg == 'AR':
                        self.ar += 1
                
                self.mainTeamPlayers.addItems(teamPlayers)
                self.mainTeamNameDisp.setText(teamAns)
                self.setValues()

    
    def evaluateTeamMain(self):
        self.evaluateTeamUi()
    

    def saveTeamMain(self):

        if self.criteriaSave():
            cur = conn.cursor()
            queryTeam = 'Select name from teams;'
            cur.execute(queryTeam)
            data = cur.fetchall()
            teams = [i[0] for i in data]
        
            teamName = self.mainTeamNameDisp.text()
            teamValue = int(self.mainPtsUsedCount.text())
            teamPlayers = [self.mainTeamPlayers.item(i).text() for i in range(self.mainTeamPlayers.count())]
            teamPlayers = ','.join(teamPlayers)

            query = "Insert into teams values (%s, %s, %s);"
            inputData = (teamName, teamPlayers, teamValue,)

            wantToSave = True

            if teamName in teams:
                btnReply = self.showQn(f'Do You Want to update the existing team {teamName}', 'Update Team')

                if btnReply == QtWidgets.QMessageBox.Yes:
                    query = "Update teams set players = %s , team_value = %s where name = %s;"
                    inputData = (teamPlayers, teamValue, teamName,)
                else:
                    teamName, ok = QtWidgets.QInputDialog.getText(MainWindow, "Rename Team", "Enter new name of the team:")
                    inputData = (teamName, teamPlayers, teamValue,)  # with new Team Name
                    if not ok:
                        wantToSave = False

            if wantToSave:
                try:
                    cur.execute(query, inputData)
                    conn.commit()
                    self.isSaved = True
                    self.showMsg(f'Team {teamName} saved successfully ;)', 'Saved')
                    self.mainTeamNameDisp.setText(teamName)
                except Exception as e:
                    conn.rollback()
                    self.showMsg( 'Saving operation unsuccessful :/', 'Error')
                    raise(e)
        
    def seeStatsMain(self):
        cur = conn.cursor()
        queryPlayers = 'Select name from stats;'
        cur.execute(queryPlayers)
        data = cur.fetchall()
        players = [i[0] for i in data]

        playerAns, ok = QtWidgets.QInputDialog.getItem(MainWindow, "View Stat", "Choose a Player to View Stat", players, 0, False)

        if playerAns and ok:
            self.statsTeamUi(playerAns)

    # Function to call to show QMainWindow for evaluate and stats
    def evaluateTeamUi(self):
        self.evaluateTeam = QtWidgets.QMainWindow()
        self.evaluateUi = EvaluateWindow()
        self.evaluateUi.setupUi(self.evaluateTeam)
        self.evaluateTeam.show()
    
    def statsTeamUi(self, playerName):
        self.statsTeam = QtWidgets.QMainWindow()
        self.statsUi = StatsWindow()
        self.statsUi.setupUi(self.statsTeam)
        self.statsTeam.show()

        self.statsUi.statsNameOut.setText(playerName)

        cur = conn.cursor()
        queryStats = 'Select * from stats where name = %s;'
        cur.execute(queryStats, (playerName,))
        data = cur.fetchone()

        self.statsUi.statsNameOut.setText(playerName)
        self.statsUi.statsOut1.setText(str(data[2]))
        self.statsUi.statsOut2.setText(str(data[3]))
        self.statsUi.statsOut3.setText(str(data[4]))
        self.statsUi.statsOut4.setText(str(data[5]))
        self.statsUi.statsOut5.setText(str(data[6]))
        self.statsUi.statsOut6.setText(str(data[7]))
        self.statsUi.statsOut7.setText(str(data[8]))
        self.statsUi.statsOut8.setText(str(data[9]))
        self.statsUi.statsOut9.setText(str(data[10]))
        self.statsUi.statsOut10.setText(str(data[11]))


    # function to populate AllPlayers list based on radiobutton
    def list_ctg(self):
        self.mainAllPlayers.clear()
        curr = conn.cursor()

        ctg = ''
        if self.mainRadioBat.isChecked(): ctg = 'BAT'
        elif self.mainRadioBow.isChecked(): ctg = 'BWL'
        elif self.mainRadioWK.isChecked(): ctg = 'WK'
        else: ctg = 'AR'

        query_bat = "Select name from stats where ctg = %s;"
        curr.execute(query_bat, (ctg,))
        batsmen = [i[0] for i in curr.fetchall()]

        players_exist_team = [self.mainTeamPlayers.item(i).text() for i in range(self.mainTeamPlayers.count())]

        for i in batsmen:
            if i not in players_exist_team:
                self.mainAllPlayers.addItem(i)
    

    # criteria for game logic
    def criteria(self, value):

        isCorrect = True
        moreThan = ''
        msg = ''
        title = 'Criteria Violated'

        if self.bat + self.bowl + self.ar + self.wk > 11:
            msg = 'Players can\'t exceed count of 11. We don\'t require extras!'
            isCorrect = False
        elif self.avl - value < 0:
            msg = 'Player value exceeds total Points Available :/'
            isCorrect = False
        elif self.bat > 4:
            moreThan = '4 Batsmen'
            isCorrect = False
        elif self.bowl > 4:
            moreThan = '4 Bowlers'
            isCorrect = False
        elif self.ar > 4:
            moreThan = '4 All Rounders'
            isCorrect = False
        elif self.wk > 1:
            moreThan = '1 Wicket keeper'
            isCorrect = False

        if moreThan:
            msg = f'Cannot have more than {moreThan}!'
        
        if not isCorrect:
            self.showMsg(msg, title)
        
        return isCorrect

    def criteriaSave(self):

        isCorrect = True
        msg = ''
        title = 'Game Logic Failed'

        ttlPlayers = self.bat + self.bowl + self.ar + self.wk

        if self.wk != 1:
            msg = 'Must have one Wicket Keeper'
            isCorrect = False
        elif self.bat < 3:
            msg = 'Must have atleast 3 Batsmen'
            isCorrect = False
        elif self.bowl < 2:
            msg = 'Must have atleast 2 Bowlers'
            isCorrect = False
        elif self.ar < 2:
            msg = 'Must have atleast 2 All Rounders'
            isCorrect = False
        elif ttlPlayers != 11:
            msg = 'Total players must be 11'
            isCorrect = False
        
        if not isCorrect:
            self.showMsg(msg, title)
        
        return isCorrect


    # functions to edit QListWidgets of All Players and Team Players
    def removeListPlayers(self, item):
        playerName = item.text()
        cur = conn.cursor()
        queryPlayer = "Select ctg, player_value from stats where name = %s;"
        cur.execute(queryPlayer, (playerName,))
        data = cur.fetchone()
        ctg = str(data[0])
        playerValue = int(data[1])
        
        isCorrect = True

        if ctg == 'BAT': 
            self.bat += 1
            if not self.criteria(playerValue):
                isCorrect = False
                self.bat -= 1
        elif ctg == 'BWL': 
            self.bowl += 1
            if not self.criteria(playerValue):
                isCorrect = False
                self.bowl -= 1
        elif ctg == 'AR': 
            self.ar += 1
            if not self.criteria(playerValue):
                isCorrect = False
                self.ar -= 1
        elif ctg == 'WK': 
            self.wk += 1
            if not self.criteria(playerValue):
                isCorrect = False
                self.wk -= 1
            
        if isCorrect:
            self.isSaved = False
            self.value += playerValue
            self.avl -= playerValue
            self.setValues()
            self.mainAllPlayers.takeItem(self.mainAllPlayers.row(item))
            self.mainTeamPlayers.addItem(playerName)
            
    
    def removeTeamPlayers(self, item):
        playerName = item.text()
        cur = conn.cursor()
        queryPlayer = "Select ctg, player_value from stats where name = %s;"
        cur.execute(queryPlayer, (playerName,))
        data = cur.fetchone()
        ctg = str(data[0])
        playerValue = int(data[1])
        
        toBeAdded = False  # based on radioButton selected, to be added and displayed or not

        if ctg == 'BAT': 
            self.bat -= 1
            if self.mainRadioBat.isChecked():
                toBeAdded = True
        elif ctg == 'BWL': 
            self.bowl -= 1
            if self.mainRadioBow.isChecked():
                toBeAdded = True
        elif ctg == 'AR': 
            self.ar -= 1
            if self.mainRadioAR.isChecked():
                toBeAdded = True
        elif ctg == 'WK': 
            self.wk -= 1
            if self.mainRadioWK.isChecked():
                toBeAdded = True
        
        self.isSaved = False
        self.value -= playerValue
        self.avl += playerValue
        self.setValues()
        self.mainTeamPlayers.takeItem(self.mainTeamPlayers.row(item))
        if toBeAdded == True: self.mainAllPlayers.addItem(playerName)

    
    # function to set all values to new
    def setValues(self):
        self.mainPtsUsedCount.setText(str(self.value))
        self.mainPtsAvailCount.setText(str(self.avl))
        self.mainBatCount.setText(str(self.bat))
        self.mainBowCount.setText(str(self.bowl))
        self.mainARCount.setText(str(self.ar))
        self.mainWKCount.setText(str(self.wk))

    # show message box
    def showMsg(self, msg, title):
        QtWidgets.QMessageBox.information(MainWindow, title, msg, QtWidgets.QMessageBox.Ok)
    
    def showQn(self, msg, title):
        btnReply = QtWidgets.QMessageBox.question(MainWindow, title, msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        return btnReply

    # asking to save before quit
    def exit(self):
        if not self.isSaved and self.bat + self.bowl + self.ar + self.wk != 0:
            btnReply = self.showQn('Do you want to save', 'Save Team')

            if btnReply == QtWidgets.QMessageBox.Yes:
                self.saveTeamMain()
        else:
            self.showMsg('Hope you enjoyed!', 'Exit')
            sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # close sql connection
    conn.close()