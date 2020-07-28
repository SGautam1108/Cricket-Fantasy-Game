from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector 
conn1 = mysql.connector.connect(host='localhost', user='root', passwd = 'Pass@1234', database ='cricketfantasy')

class Ui_EvaluateWindow(object):
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(851, 687)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EvaluateWindow.setWindowIcon(icon)
        EvaluateWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.evaluatePerfLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Std 30 AB")
        font.setPointSize(11)
        self.evaluatePerfLabel.setFont(font)
        self.evaluatePerfLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.evaluatePerfLabel.setObjectName("evaluatePerfLabel")
        self.verticalLayout.addWidget(self.evaluatePerfLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.evaluateComboSelectTeam = QtWidgets.QComboBox(self.centralwidget)
        self.evaluateComboSelectTeam.setObjectName("evaluateComboSelectTeam")
        self.horizontalLayout.addWidget(self.evaluateComboSelectTeam)
        self.evaluateComboSelectMatch = QtWidgets.QComboBox(self.centralwidget)
        self.evaluateComboSelectMatch.setObjectName("evaluateComboSelectMatch")
        self.horizontalLayout.addWidget(self.evaluateComboSelectMatch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.evaluatePlayersLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.evaluatePlayersLabel.setFont(font)
        self.evaluatePlayersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.evaluatePlayersLabel.setObjectName("evaluatePlayersLabel")
        self.horizontalLayout_3.addWidget(self.evaluatePlayersLabel)
        spacerItem = QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.evaluatePointsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.evaluatePointsLabel.setFont(font)
        self.evaluatePointsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.evaluatePointsLabel.setObjectName("evaluatePointsLabel")
        self.horizontalLayout_3.addWidget(self.evaluatePointsLabel)
        self.evaluatePointsOutput = QtWidgets.QLabel(self.centralwidget)
        self.evaluatePointsOutput.setObjectName("evaluatePointsOutput")
        self.horizontalLayout_3.addWidget(self.evaluatePointsOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.evaluatePlayersList = QtWidgets.QListWidget(self.centralwidget)
        self.evaluatePlayersList.setObjectName("evaluatePlayersList")
        self.horizontalLayout_2.addWidget(self.evaluatePlayersList)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.evaluatePlayerPtsList = QtWidgets.QListWidget(self.centralwidget)
        self.evaluatePlayerPtsList.setObjectName("evaluatePlayerPtsList")
        self.horizontalLayout_2.addWidget(self.evaluatePlayerPtsList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.evaluateCalcBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evaluateCalcBtn.sizePolicy().hasHeightForWidth())
        self.evaluateCalcBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.evaluateCalcBtn.setFont(font)
        self.evaluateCalcBtn.setObjectName("evaluateCalcBtn")
        self.horizontalLayout_6.addWidget(self.evaluateCalcBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EvaluateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        EvaluateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

        # set button as disabled at start
        self.evaluateCalcBtn.setEnabled(False)

        # list out items for team combo and matches combo
        self.teamsShow()
        self.matchesShow()

        # trigger for selections
        self.evaluateComboSelectTeam.activated.connect(self.showPlayers)
        self.evaluateComboSelectMatch.activated.connect(self.showPts)

        # trigger for calculate score
        self.evaluateCalcBtn.clicked.connect(self.calculateTotal)


    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "Evaluate Team"))
        self.evaluatePerfLabel.setText(_translate("EvaluateWindow", "Evaluate Performance of your Fantasy team"))
        self.evaluatePlayersLabel.setText(_translate("EvaluateWindow", "Players"))
        self.evaluatePointsLabel.setText(_translate("EvaluateWindow", "Points-"))
        self.evaluatePointsOutput.setText(_translate("EvaluateWindow", "00"))
        self.evaluateCalcBtn.setText(_translate("EvaluateWindow", "Calculate Score"))

    def teamsShow(self):
        cur = conn1.cursor()
        queryTeam = 'Select name from teams;'
        cur.execute(queryTeam)
        data = cur.fetchall()
        teams = [i[0] for i in data]
        self.evaluateComboSelectTeam.addItems(teams)

    def matchesShow(self):
        match = 'Match'
        for i in range(1, 6):
            self.evaluateComboSelectMatch.addItem(match + str(i))

    def showPlayers(self):
        self.evaluatePlayersList.clear()
        self.evaluatePlayerPtsList.clear()
        self.evaluateCalcBtn.setEnabled(False)
        
        teamName = self.evaluateComboSelectTeam.currentText()
        cur = conn1.cursor()
        queryPlayers = 'Select players from teams where name = %s;'
        cur.execute(queryPlayers, (teamName,))

        data = cur.fetchone()
        players = data[0].split(',')

        self.evaluatePlayersList.addItems(players)

    def showPts(self):
        self.evaluatePlayerPtsList.clear()
        matchName = self.evaluateComboSelectMatch.currentText().lower()
        players = [self.evaluatePlayersList.item(i).text() for i in range(self.evaluatePlayersList.count())]

        for player in players:
            pts = self.calculatePts(matchName, player)
            self.evaluatePlayerPtsList.addItem(str(pts))
        
        self.evaluateCalcBtn.setEnabled(True)


    def calculatePts(self, matchName, playerName):
        cur = conn1.cursor()
        query = "Select {0}.*, stats.ctg from {0}, stats where {0}.player_id = stats.player_id and stats.name = '{1}';".format(matchName, playerName)
        cur.execute(query)

        pts = 0

        # format- id, scored, faced, fours, sixes, bowled, maiden, runs_given, wkts, catched, stumping, runout, ctg
        data = cur.fetchone()
        ctg = data[-1]

        # if bowler or all-rounder, pts for bowling
        if ctg == 'BWL' or ctg == 'AR':
            overs = data[5]/6  # float
            maiden = data[6]
            runs = data[7]
            wkts = data[8]

            econ = runs/overs
            if econ >= 3.5 and econ < 5:
                pts += 4
            elif econ >= 2:
                pts += 7
            else:
                pts += 10

            pts += 2 * maiden
            pts += 4 * wkts

            # 5w's and 4w's
            fours_left = (wkts % 5) // 4
            pts += 10 * (wkts//5)
            pts += 5 * (fours_left)
            
        #if batsmen, wicket keeper or 
        if ctg == 'BAT' or ctg == 'AR' or ctg == 'WK':
            score = data[1]
            faced = data[2]
            fours = data[3]
            sixes = data[4]

            strike = (score/faced) * 100
            if strike >= 100:
                pts += 10  # Additional
            if strike >= 80:
                pts += 2

            pts += (score // 2)
            pts += 4*sixes
            pts += 2*fours

            half_cent = (score % 100) // 50

            pts += 5 * (half_cent)
            pts += 10 * (score // 100)

        # common
        catch = data[-4]
        stump = data[-3]
        ro = data[-2]

        pts += 5 * (catch + stump + ro)

        return pts

    def calculateTotal(self):
        ttl = 0

        for i in range(self.evaluatePlayerPtsList.count()):
            ttl += int(self.evaluatePlayerPtsList.item(i).text())
        
        self.evaluatePointsOutput.setText(str(ttl))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())

    conn1.close()