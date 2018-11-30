# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setObjectName("pushButton_import")
        self.gridLayout_3.addWidget(self.pushButton_import, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView_many = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_many.setObjectName("tableView_many")
        self.gridLayout_2.addWidget(self.tableView_many, 0, 0, 1, 1)
        self.pushButton_many = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_many.setObjectName("pushButton_many")
        self.gridLayout_2.addWidget(self.pushButton_many, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView_single = QtWidgets.QTableView(self.groupBox)
        self.tableView_single.setObjectName("tableView_single")
        self.gridLayout.addWidget(self.tableView_single, 0, 0, 1, 1)
        self.pushButton_signle = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_signle.setObjectName("pushButton_signle")
        self.gridLayout.addWidget(self.pushButton_signle, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_import.setText(_translate("MainWindow", "导入Excel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_many.setText(_translate("MainWindow", "多人转账"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_signle.setText(_translate("MainWindow", "单人转账"))

