# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 554)

        self.mwCentralWidget = QtWidgets.QWidget(MainWindow)
        self.mwCentralWidget.setObjectName("mwCentralWidget")

        self.mwStackedWidget = QtWidgets.QStackedWidget(self.mwCentralWidget)
        self.mwStackedWidget.setGeometry(QtCore.QRect(0, 0, 751, 521))
        self.mwStackedWidget.setObjectName("mwStackedWidget")

        self.graphPage = QtWidgets.QWidget()
        self.graphPage.setObjectName("graphPage")

        self.testPlot = pg.PlotWidget(self.graphPage)
        self.testPlot.setGeometry(QtCore.QRect(40, 30, 531, 471))
        self.testPlot.setObjectName("testPlot")
        # pg.setConfigOptions(antialias=True)

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        self.mwStackedWidget.addWidget(self.graphPage)

        self.setupPage = QtWidgets.QWidget()
        self.setupPage.setObjectName("setupPage")

        self.sLabelSetup = QtWidgets.QLabel(self.setupPage)
        self.sLabelSetup.setGeometry(QtCore.QRect(50, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sLabelSetup.setFont(font)
        self.sLabelSetup.setObjectName("sLabelSetup")

        self.widget = QtWidgets.QWidget(self.setupPage)
        self.widget.setGeometry(QtCore.QRect(30, 70, 321, 84))
        self.widget.setObjectName("widget")

        self.sHorizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.sHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sHorizontalLayout.setObjectName("sHorizontalLayout")

        self.sVerticalLayout_8 = QtWidgets.QVBoxLayout()
        self.sVerticalLayout_8.setObjectName("sVerticalLayout_8")

        self.sTemp_1 = QtWidgets.QCheckBox(self.widget)
        self.sTemp_1.setObjectName("sTemp_1")
        self.sTemp_1.stateChanged.connect(self.checked_1)
        self.sVerticalLayout_8.addWidget(self.sTemp_1)

        self.sTemp_2 = QtWidgets.QCheckBox(self.widget)
        self.sTemp_2.setObjectName("sTemp_2")
        self.sTemp_2.stateChanged.connect(self.checked_2)
        self.sVerticalLayout_8.addWidget(self.sTemp_2)

        self.sTemp_3 = QtWidgets.QCheckBox(self.widget)
        self.sTemp_3.setObjectName("sTemp_3")
        self.sTemp_3.stateChanged.connect(self.checked_3)
        self.sVerticalLayout_8.addWidget(self.sTemp_3)

        self.sHorizontalLayout.addLayout(self.sVerticalLayout_8)

        self.sVerticalLayout = QtWidgets.QVBoxLayout()
        self.sVerticalLayout.setObjectName("sVerticalLayout")

        self.sComboBox_Temp_1 = QtWidgets.QComboBox(self.widget)
        self.sComboBox_Temp_1.setEnabled(False)
        self.sComboBox_Temp_1.setObjectName("sComboBox_Temp_1")
        self.sComboBox_Temp_1.addItem("--",-1)
        self.sComboBox_Temp_1.addItem("T1",1)
        self.sComboBox_Temp_1.addItem("T2",2)
        self.sComboBox_Temp_1.addItem("T3",3)
        self.sVerticalLayout.addWidget(self.sComboBox_Temp_1)

        self.sComboBox_Temp_2 = QtWidgets.QComboBox(self.widget)
        self.sComboBox_Temp_2.setEnabled(False)
        self.sComboBox_Temp_2.addItem("--",-1)
        self.sComboBox_Temp_2.addItem("T1",1)
        self.sComboBox_Temp_2.addItem("T2",2)
        self.sComboBox_Temp_2.addItem("T3",3)
        self.sComboBox_Temp_2.setObjectName("sComboBox_Temp_2")
        self.sVerticalLayout.addWidget(self.sComboBox_Temp_2)

        self.sComboBox_Temp_3 = QtWidgets.QComboBox(self.widget)
        self.sComboBox_Temp_3.setEnabled(False)
        self.sComboBox_Temp_3.addItem("--",-1)
        self.sComboBox_Temp_3.addItem("T1",1)
        self.sComboBox_Temp_3.addItem("T2",2)
        self.sComboBox_Temp_3.addItem("T3",3)
        self.sComboBox_Temp_3.setObjectName("sComboBox_Temp_3")
        self.sVerticalLayout.addWidget(self.sComboBox_Temp_3)
        self.sHorizontalLayout.addLayout(self.sVerticalLayout)

        self.widget1 = QtWidgets.QWidget(self.setupPage)
        self.widget1.setGeometry(QtCore.QRect(30, 160, 321, 84))
        self.widget1.setObjectName("widget1")

        self.sHorizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.sHorizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sHorizontalLayout_2.setObjectName("sHorizontalLayout_2")

        self.sVerticalLayout_7 = QtWidgets.QVBoxLayout()
        self.sVerticalLayout_7.setObjectName("sVerticalLayout_7")

        self.sMotVal_1 = QtWidgets.QCheckBox(self.widget1)
        self.sMotVal_1.setObjectName("sMotVal_1")
        self.sVerticalLayout_7.addWidget(self.sMotVal_1)

        self.sMotVal_2 = QtWidgets.QCheckBox(self.widget1)
        self.sMotVal_2.setObjectName("sMotVal_2")
        self.sVerticalLayout_7.addWidget(self.sMotVal_2)

        self.sMotVal_3 = QtWidgets.QCheckBox(self.widget1)
        self.sMotVal_3.setObjectName("sMotVal_3")
        self.sVerticalLayout_7.addWidget(self.sMotVal_3)

        self.sHorizontalLayout_2.addLayout(self.sVerticalLayout_7)
        self.sVerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.sVerticalLayout_2.setObjectName("sVerticalLayout_2")

        self.sComboBox_MotVal_1 = QtWidgets.QComboBox(self.widget1)
        self.sComboBox_MotVal_1.setEnabled(False)
        self.sComboBox_MotVal_1.setObjectName("sComboBox_MotVal_1")
        self.sVerticalLayout_2.addWidget(self.sComboBox_MotVal_1)

        self.sComboBox_MotVal_2 = QtWidgets.QComboBox(self.widget1)
        self.sComboBox_MotVal_2.setEnabled(False)
        self.sComboBox_MotVal_2.setObjectName("sComboBox_MotVal_2")
        self.sVerticalLayout_2.addWidget(self.sComboBox_MotVal_2)

        self.sComboBox_MotVal_3 = QtWidgets.QComboBox(self.widget1)
        self.sComboBox_MotVal_3.setEnabled(False)
        self.sComboBox_MotVal_3.setObjectName("sComboBox_MotVal_3")
        self.sVerticalLayout_2.addWidget(self.sComboBox_MotVal_3)
        self.sHorizontalLayout_2.addLayout(self.sVerticalLayout_2)

        self.mwStackedWidget.addWidget(self.setupPage)

        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setObjectName("menuPage")

        self.mSplitter = QtWidgets.QSplitter(self.menuPage)
        self.mSplitter.setGeometry(QtCore.QRect(70, 90, 201, 191))
        self.mSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mSplitter.setObjectName("mSplitter")

        self.mSetupBtn = QtWidgets.QPushButton(self.mSplitter)
        self.mSetupBtn.setObjectName("mSetupBtn")
        self.mSetupBtn.clicked.connect(lambda: ui.mwStackedWidget.setCurrentIndex(1))

        self.mGraphBtn = QtWidgets.QPushButton(self.mSplitter)
        self.mGraphBtn.setObjectName("mGraphBtn")
        self.mGraphBtn.clicked.connect(lambda: ui.mwStackedWidget.setCurrentIndex(3))

        self.mRfBtn = QtWidgets.QPushButton(self.mSplitter)
        self.mRfBtn.setObjectName("mRfBtn")
        self.mRfBtn.clicked.connect(lambda: ui.mwStackedWidget.setCurrentIndex(4))

        self.mLabelMenu = QtWidgets.QLabel(self.menuPage)
        self.mLabelMenu.setGeometry(QtCore.QRect(70, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mLabelMenu.setFont(font)
        self.mLabelMenu.setObjectName("mLabelMenu")

        self.mwStackedWidget.addWidget(self.menuPage)

        self.graphSetup = QtWidgets.QWidget()
        self.graphSetup.setObjectName("graphSetup")

        self.layoutWidget = QtWidgets.QWidget(self.graphSetup)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 331, 84))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.gHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gHorizontalLayout.setObjectName("gHorizontalLayout")

        self.gVerticalLayout = QtWidgets.QVBoxLayout()
        self.gVerticalLayout.setObjectName("gVerticalLayout")

        self.gRefTemp_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.gRefTemp_1.setObjectName("gRefTemp_1")
        self.gVerticalLayout.addWidget(self.gRefTemp_1)

        self.gRefTemp_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.gRefTemp_2.setObjectName("gRefTemp_2")
        self.gVerticalLayout.addWidget(self.gRefTemp_2)

        self.gRefTemp_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.gRefTemp_3.setObjectName("gRefTemp_3")
        self.gVerticalLayout.addWidget(self.gRefTemp_3)
        self.gHorizontalLayout.addLayout(self.gVerticalLayout)

        self.gVerticalLayout_4 = QtWidgets.QVBoxLayout()
        self.gVerticalLayout_4.setObjectName("gVerticalLayout_4")

        self.gRefSpin_1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.gRefSpin_1.setEnabled(False)
        self.gRefSpin_1.setObjectName("gRefSpin_1")
        self.gVerticalLayout_4.addWidget(self.gRefSpin_1)

        self.gRefSpin_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.gRefSpin_2.setEnabled(False)
        self.gRefSpin_2.setObjectName("gRefSpin_2")
        self.gVerticalLayout_4.addWidget(self.gRefSpin_2)

        self.gRefSpin_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.gRefSpin_3.setEnabled(False)
        self.gRefSpin_3.setObjectName("gRefSpin_3")
        self.gVerticalLayout_4.addWidget(self.gRefSpin_3)

        self.gHorizontalLayout.addLayout(self.gVerticalLayout_4)

        self.gLabelSetupGraph = QtWidgets.QLabel(self.graphSetup)
        self.gLabelSetupGraph.setGeometry(QtCore.QRect(50, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.gLabelSetupGraph.setFont(font)
        self.gLabelSetupGraph.setObjectName("gLabelSetupGraph")

        self.widget2 = QtWidgets.QWidget(self.graphSetup)
        self.widget2.setGeometry(QtCore.QRect(40, 170, 331, 78))
        self.widget2.setObjectName("widget2")

        self.gHorizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.gHorizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gHorizontalLayout_2.setObjectName("gHorizontalLayout_2")

        self.gVerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.gVerticalLayout_2.setObjectName("gVerticalLayout_2")

        self.gTemp_1 = QtWidgets.QCheckBox(self.widget2)
        self.gTemp_1.setObjectName("gTemp_1")
        self.gVerticalLayout_2.addWidget(self.gTemp_1)

        self.gTemp_2 = QtWidgets.QCheckBox(self.widget2)
        self.gTemp_2.setObjectName("gTemp_2")
        self.gVerticalLayout_2.addWidget(self.gTemp_2)

        self.gTemp_3 = QtWidgets.QCheckBox(self.widget2)
        self.gTemp_3.setObjectName("gTemp_3")
        self.gVerticalLayout_2.addWidget(self.gTemp_3)

        self.gHorizontalLayout_2.addLayout(self.gVerticalLayout_2)

        self.gVerticalLayout_5 = QtWidgets.QVBoxLayout()
        self.gVerticalLayout_5.setObjectName("gVerticalLayout_5")

        self.label_gTemp_1 = QtWidgets.QLabel(self.widget2)
        self.label_gTemp_1.setObjectName("label_gTemp_1")
        self.gVerticalLayout_5.addWidget(self.label_gTemp_1)

        self.label_gTemp_2 = QtWidgets.QLabel(self.widget2)
        self.label_gTemp_2.setObjectName("label_gTemp_2")
        self.gVerticalLayout_5.addWidget(self.label_gTemp_2)

        self.label_gTemp_3 = QtWidgets.QLabel(self.widget2)
        self.label_gTemp_3.setObjectName("label_gTemp_3")
        self.gVerticalLayout_5.addWidget(self.label_gTemp_3)

        self.gHorizontalLayout_2.addLayout(self.gVerticalLayout_5)

        self.widget3 = QtWidgets.QWidget(self.graphSetup)
        self.widget3.setGeometry(QtCore.QRect(40, 260, 331, 78))
        self.widget3.setObjectName("widget3")

        self.gHorizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.gHorizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gHorizontalLayout_3.setObjectName("gHorizontalLayout_3")

        self.gVerticalLayout_3 = QtWidgets.QVBoxLayout()
        self.gVerticalLayout_3.setObjectName("gVerticalLayout_3")

        self.gMotVal_1 = QtWidgets.QCheckBox(self.widget3)
        self.gMotVal_1.setObjectName("gMotVal_1")
        self.gVerticalLayout_3.addWidget(self.gMotVal_1)

        self.gMotVal_2 = QtWidgets.QCheckBox(self.widget3)
        self.gMotVal_2.setObjectName("gMotVal_2")
        self.gVerticalLayout_3.addWidget(self.gMotVal_2)

        self.gMotVal_3 = QtWidgets.QCheckBox(self.widget3)
        self.gMotVal_3.setObjectName("gMotVal_3")
        self.gVerticalLayout_3.addWidget(self.gMotVal_3)

        self.gHorizontalLayout_3.addLayout(self.gVerticalLayout_3)

        self.gVerticalLayout_6 = QtWidgets.QVBoxLayout()
        self.gVerticalLayout_6.setObjectName("gVerticalLayout_6")

        self.label_gMotVal_1 = QtWidgets.QLabel(self.widget3)
        self.label_gMotVal_1.setObjectName("label_gMotVal_1")
        self.gVerticalLayout_6.addWidget(self.label_gMotVal_1)

        self.label_gMotVal_2 = QtWidgets.QLabel(self.widget3)
        self.label_gMotVal_2.setObjectName("label_gMotVal_2")
        self.gVerticalLayout_6.addWidget(self.label_gMotVal_2)

        self.label_gMotVal_3 = QtWidgets.QLabel(self.widget3)
        self.label_gMotVal_3.setObjectName("label_gMotVal_3")
        self.gVerticalLayout_6.addWidget(self.label_gMotVal_3)

        self.gHorizontalLayout_3.addLayout(self.gVerticalLayout_6)

        self.mwStackedWidget.addWidget(self.graphSetup)

        self.rfSetup = QtWidgets.QWidget()
        self.rfSetup.setObjectName("rfSetup")

        self.rfLabelSetup = QtWidgets.QLabel(self.rfSetup)
        self.rfLabelSetup.setGeometry(QtCore.QRect(40, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rfLabelSetup.setFont(font)
        self.rfLabelSetup.setObjectName("rfLabelSetup")

        self.rfSlaveAdress = QtWidgets.QLabel(self.rfSetup)
        self.rfSlaveAdress.setGeometry(QtCore.QRect(40, 120, 91, 16))
        self.rfSlaveAdress.setObjectName("rfSlaveAdress")

        self.widget4 = QtWidgets.QWidget(self.rfSetup)
        self.widget4.setGeometry(QtCore.QRect(40, 90, 261, 24))
        self.widget4.setObjectName("widget4")

        self.rfHorizontalLayout = QtWidgets.QHBoxLayout(self.widget4)
        self.rfHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rfHorizontalLayout.setObjectName("rfHorizontalLayout")

        self.rfLabelSlaveUnits = QtWidgets.QLabel(self.widget4)
        self.rfLabelSlaveUnits.setObjectName("rfLabelSlaveUnits")

        self.rfHorizontalLayout.addWidget(self.rfLabelSlaveUnits)

        self.rfSpinBox_slave = QtWidgets.QSpinBox(self.widget4)
        self.rfSpinBox_slave.setEnabled(True)
        self.rfSpinBox_slave.setObjectName("rfSpinBox_slave")

        self.rfHorizontalLayout.addWidget(self.rfSpinBox_slave)

        self.widget5 = QtWidgets.QWidget(self.rfSetup)
        self.widget5.setGeometry(QtCore.QRect(40, 210, 261, 24))
        self.widget5.setObjectName("widget5")

        self.rfHorizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget5)
        self.rfHorizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rfHorizontalLayout_2.setObjectName("rfHorizontalLayout_2")

        self.rfOutPower = QtWidgets.QLabel(self.widget5)
        self.rfOutPower.setObjectName("rfOutPower")

        self.rfHorizontalLayout_2.addWidget(self.rfOutPower)

        self.rfComboBox_power = QtWidgets.QComboBox(self.widget5)
        self.rfComboBox_power.setObjectName("rfComboBox_power")

        self.rfHorizontalLayout_2.addWidget(self.rfComboBox_power)

        self.mwStackedWidget.addWidget(self.rfSetup)

        self.mwUpBtn = QtWidgets.QPushButton(self.mwCentralWidget)
        self.mwUpBtn.setGeometry(QtCore.QRect(860, 180, 61, 61))
        self.mwUpBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mwUpBtn.setIcon(icon)
        self.mwUpBtn.setIconSize(QtCore.QSize(60, 60))
        self.mwUpBtn.setObjectName("upBtn")

        self.mwMenuBtn = QtWidgets.QPushButton(self.mwCentralWidget)
        self.mwMenuBtn.setGeometry(QtCore.QRect(860, 240, 61, 61))
        self.mwMenuBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/menu but.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mwMenuBtn.setIcon(icon1)
        self.mwMenuBtn.setIconSize(QtCore.QSize(60, 60))
        self.mwMenuBtn.setObjectName("mwMenuBtn")
        self.mwMenuBtn.clicked.connect(lambda: ui.mwStackedWidget.setCurrentIndex(2))

        self.mwDownBtn = QtWidgets.QPushButton(self.mwCentralWidget)
        self.mwDownBtn.setGeometry(QtCore.QRect(860, 300, 61, 61))
        self.mwDownBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mwDownBtn.setIcon(icon2)
        self.mwDownBtn.setIconSize(QtCore.QSize(60, 60))
        self.mwDownBtn.setObjectName("mwDownBtn")

        self.mwRightBtn = QtWidgets.QPushButton(self.mwCentralWidget)
        self.mwRightBtn.setGeometry(QtCore.QRect(920, 240, 61, 61))
        self.mwRightBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Arrow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mwRightBtn.setIcon(icon3)
        self.mwRightBtn.setIconSize(QtCore.QSize(60, 60))
        self.mwRightBtn.setObjectName("mwRightBtn")

        self.mwLeftBtn = QtWidgets.QPushButton(self.mwCentralWidget)
        self.mwLeftBtn.setGeometry(QtCore.QRect(800, 240, 61, 61))
        self.mwLeftBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mwLeftBtn.setIcon(icon4)
        self.mwLeftBtn.setIconSize(QtCore.QSize(60, 60))
        self.mwLeftBtn.setObjectName("mwLeftBtn")
        self.mwLeftBtn.clicked.connect(lambda: ui.mwStackedWidget.setCurrentIndex(0))

        MainWindow.setCentralWidget(self.mwCentralWidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mwStackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update(self):
        now = datetime.datetime.now()
        sec = np.array([now.second])
       #  temp = np.random.normal(size=1)
       ## test2 = np.linspace(60, 0, 60)
        self.testPlot.plot(sec, sec, pen=None, symbol = 'o')

    def checked_1(self, state):
        if state == QtCore.Qt.Checked:
            self.sComboBox_Temp_1.setEnabled(True)
        else:
            self.sComboBox_Temp_1.setEnabled(False)

    def checked_2(self, state):
        if state == QtCore.Qt.Checked:
            self.sComboBox_Temp_2.setEnabled(True)
        else:
            self.sComboBox_Temp_2.setEnabled(False)

    def checked_3(self, state):
        if state == QtCore.Qt.Checked:
            self.sComboBox_Temp_3.setEnabled(True)
        else:
            self.sComboBox_Temp_3.setEnabled(False)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sLabelSetup.setText(_translate("MainWindow", "Setup"))
        self.sTemp_1.setText(_translate("MainWindow", "Temp 1"))
        self.sTemp_2.setText(_translate("MainWindow", "Temp 2"))
        self.sTemp_3.setText(_translate("MainWindow", "Temp 3"))
        self.sMotVal_1.setText(_translate("MainWindow", "MotVal 1"))
        self.sMotVal_2.setText(_translate("MainWindow", "MotVal2"))
        self.sMotVal_3.setText(_translate("MainWindow", "MotVal3"))
        self.mSetupBtn.setText(_translate("MainWindow", "Setup"))
        self.mGraphBtn.setText(_translate("MainWindow", "Setup Graph View"))
        self.mRfBtn.setText(_translate("MainWindow", "RF Module"))
        self.mLabelMenu.setText(_translate("MainWindow", "Menu"))
        self.gRefTemp_1.setText(_translate("MainWindow", "RefTemp 1"))
        self.gRefTemp_2.setText(_translate("MainWindow", "RefTemp 2"))
        self.gRefTemp_3.setText(_translate("MainWindow", "RefTemp3"))
        self.gLabelSetupGraph.setText(_translate("MainWindow", "Setup Graph View"))
        self.gTemp_1.setText(_translate("MainWindow", "Temp 1"))
        self.gTemp_2.setText(_translate("MainWindow", "Temp 2"))
        self.gTemp_3.setText(_translate("MainWindow", "Temp 3"))
        self.label_gTemp_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_gTemp_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_gTemp_3.setText(_translate("MainWindow", "TextLabel"))
        self.gMotVal_1.setText(_translate("MainWindow", "MotVal 1"))
        self.gMotVal_2.setText(_translate("MainWindow", "MotVal2"))
        self.gMotVal_3.setText(_translate("MainWindow", "MotVal3"))
        self.label_gMotVal_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_gMotVal_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_gMotVal_3.setText(_translate("MainWindow", "TextLabel"))
        self.rfLabelSetup.setText(_translate("MainWindow", "RF Setup"))
        self.rfSlaveAdress.setText(_translate("MainWindow", "Slave address:"))
        self.rfLabelSlaveUnits.setText(_translate("MainWindow", "Slave units"))
        self.rfOutPower.setText(_translate("MainWindow", "RF output power:"))

import Arrows_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

