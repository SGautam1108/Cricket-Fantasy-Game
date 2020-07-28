from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        StatsWindow.setObjectName("StatsWindow")
        StatsWindow.resize(594, 531)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StatsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StatsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.statsNameOut = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statsNameOut.sizePolicy().hasHeightForWidth())
        self.statsNameOut.setSizePolicy(sizePolicy)
        self.statsNameOut.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate Std 32 AB")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.statsNameOut.setFont(font)
        self.statsNameOut.setAlignment(QtCore.Qt.AlignCenter)
        self.statsNameOut.setObjectName("statsNameOut")
        self.horizontalLayout_9.addWidget(self.statsNameOut)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statsMatchLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsMatchLabel.setFont(font)
        self.statsMatchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsMatchLabel.setObjectName("statsMatchLabel")
        self.horizontalLayout.addWidget(self.statsMatchLabel)
        self.statsOut1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut1.setFont(font)
        self.statsOut1.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut1.setObjectName("statsOut1")
        self.horizontalLayout.addWidget(self.statsOut1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statsRunsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsRunsLabel.setFont(font)
        self.statsRunsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsRunsLabel.setObjectName("statsRunsLabel")
        self.horizontalLayout_2.addWidget(self.statsRunsLabel)
        self.statsOut2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut2.setFont(font)
        self.statsOut2.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut2.setObjectName("statsOut2")
        self.horizontalLayout_2.addWidget(self.statsOut2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statsHundLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsHundLabel.setFont(font)
        self.statsHundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsHundLabel.setObjectName("statsHundLabel")
        self.horizontalLayout_3.addWidget(self.statsHundLabel)
        self.statsOut3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut3.setFont(font)
        self.statsOut3.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut3.setObjectName("statsOut3")
        self.horizontalLayout_3.addWidget(self.statsOut3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.statsFiftLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsFiftLabel.setFont(font)
        self.statsFiftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsFiftLabel.setObjectName("statsFiftLabel")
        self.horizontalLayout_4.addWidget(self.statsFiftLabel)
        self.statsOut4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut4.setFont(font)
        self.statsOut4.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut4.setObjectName("statsOut4")
        self.horizontalLayout_4.addWidget(self.statsOut4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.statsOverLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsOverLabel.setFont(font)
        self.statsOverLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOverLabel.setObjectName("statsOverLabel")
        self.horizontalLayout_10.addWidget(self.statsOverLabel)
        self.statsOut5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setItalic(True)
        self.statsOut5.setFont(font)
        self.statsOut5.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut5.setObjectName("statsOut5")
        self.horizontalLayout_10.addWidget(self.statsOut5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.statsWickLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsWickLabel.setFont(font)
        self.statsWickLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsWickLabel.setObjectName("statsWickLabel")
        self.horizontalLayout_11.addWidget(self.statsWickLabel)
        self.statsOut6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        self.statsOut6.setFont(font)
        self.statsOut6.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut6.setObjectName("statsOut6")
        self.horizontalLayout_11.addWidget(self.statsOut6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.stats4wLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stats4wLabel.setFont(font)
        self.stats4wLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stats4wLabel.setObjectName("stats4wLabel")
        self.horizontalLayout_12.addWidget(self.stats4wLabel)
        self.statsOut7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setItalic(True)
        self.statsOut7.setFont(font)
        self.statsOut7.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut7.setObjectName("statsOut7")
        self.horizontalLayout_12.addWidget(self.statsOut7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.stats5wLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stats5wLabel.setFont(font)
        self.stats5wLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stats5wLabel.setObjectName("stats5wLabel")
        self.horizontalLayout_13.addWidget(self.stats5wLabel)
        self.statsOut8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setItalic(True)
        self.statsOut8.setFont(font)
        self.statsOut8.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut8.setObjectName("statsOut8")
        self.horizontalLayout_13.addWidget(self.statsOut8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.statsValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsValueLabel.setFont(font)
        self.statsValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsValueLabel.setObjectName("statsValueLabel")
        self.horizontalLayout_5.addWidget(self.statsValueLabel)
        self.statsOut9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut9.setFont(font)
        self.statsOut9.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut9.setObjectName("statsOut9")
        self.horizontalLayout_5.addWidget(self.statsOut9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.statsCategLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.statsCategLabel.setFont(font)
        self.statsCategLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statsCategLabel.setObjectName("statsCategLabel")
        self.horizontalLayout_6.addWidget(self.statsCategLabel)
        self.statsOut10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Savor")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.statsOut10.setFont(font)
        self.statsOut10.setAlignment(QtCore.Qt.AlignCenter)
        self.statsOut10.setObjectName("statsOut10")
        self.horizontalLayout_6.addWidget(self.statsOut10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        StatsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        StatsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatsWindow)
        self.statusbar.setObjectName("statusbar")
        StatsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatsWindow)

    def retranslateUi(self, StatsWindow):
        _translate = QtCore.QCoreApplication.translate
        StatsWindow.setWindowTitle(_translate("StatsWindow", "Player Stats"))
        self.statsNameOut.setText(_translate("StatsWindow", "Player"))
        self.statsMatchLabel.setText(_translate("StatsWindow", "Matches Played"))
        self.statsOut1.setText(_translate("StatsWindow", "###"))
        self.statsRunsLabel.setText(_translate("StatsWindow", "Runs Scored"))
        self.statsOut2.setText(_translate("StatsWindow", "###"))
        self.statsHundLabel.setText(_translate("StatsWindow", "100s"))
        self.statsOut3.setText(_translate("StatsWindow", "###"))
        self.statsFiftLabel.setText(_translate("StatsWindow", "50s"))
        self.statsOut4.setText(_translate("StatsWindow", "###"))
        self.statsOverLabel.setText(_translate("StatsWindow", "Overs Bowled"))
        self.statsOut5.setText(_translate("StatsWindow", "###"))
        self.statsWickLabel.setText(_translate("StatsWindow", "Wickets Taken"))
        self.statsOut6.setText(_translate("StatsWindow", "###"))
        self.stats4wLabel.setText(_translate("StatsWindow", "4w\'s"))
        self.statsOut7.setText(_translate("StatsWindow", "###"))
        self.stats5wLabel.setText(_translate("StatsWindow", "5w\'s"))
        self.statsOut8.setText(_translate("StatsWindow", "###"))
        self.statsValueLabel.setText(_translate("StatsWindow", "Player Value"))
        self.statsOut9.setText(_translate("StatsWindow", "###"))
        self.statsCategLabel.setText(_translate("StatsWindow", "Category"))
        self.statsOut10.setText(_translate("StatsWindow", "###"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsWindow = QtWidgets.QMainWindow()
    ui = Ui_StatsWindow()
    ui.setupUi(StatsWindow)
    StatsWindow.show()
    sys.exit(app.exec_())