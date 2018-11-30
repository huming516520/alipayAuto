from gui.mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from src.lib import annaerExcel
from src.lib import alipay
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    manyAccounts =[('姓名','支付宝','金额','操作')]
    signAccounts =[('姓名','支付宝','金额','操作')]
    zfb=None
    def __init__(self):
        super( MainWindow, self ).__init__()
        self.setupUi( self )
        self.setAttribute( Qt.WA_QuitOnClose )
        self.pushButton_import.clicked.connect( self.openFile )
        self.pushButton_many.clicked.connect(self.fillMany)
        self.zfb = alipay.alipay()

    def openFile(self):
        path = QFileDialog.getOpenFileName( self, "open file dialog", "", "excel(*.xls)" )
        if path[0] != '':
            self.excel=annaerExcel.annaerExcel(path[0])
            accounts = self.excel.getAccounts()#.insert(0, ('姓名', '支付宝', '金额'))
            for obj in accounts:
                self.manyAccounts.append((obj[0],obj[1],obj[2], '未填写'))
            self.SetTableViewFromList(self.tableView_many, self.manyAccounts)

    def fillMany(self):
        i = 0
        if len(self.manyAccounts) <= 1:
            self.zfb.fillManyTransfer( ('刘雨', '18183567857', 10.02,), 0 )
            return

        accounts=[]

        for account in self.manyAccounts:
            if account[3] == '未填写':
                accounts.append(account)

        if len(self.manyAccounts) < 20:
            maxIndex = len(self.manyAccounts)

        else:
            maxIndex = 20
        i = 0
        for j in range(0, maxIndex):
            if self.zfb.fillManyTransfer( accounts[i], i ):
                index = self.manyAccounts.index(accounts[i])
                self.manyAccounts.remove(accounts[i])
                temp = (accounts[i][0], accounts[i][1], accounts[i][2], '已填写')
                self.manyAccounts.insert(index, temp)
                i = i + 1
            else:
                self.manyAccounts.remove(accounts[i])
                self.signAccounts.append(accounts[i])
        self.SetTableViewFromList( self.tableView_many, self.manyAccounts )
        self.SetTableViewFromList( self.tableView_single, self.signAccounts )






    def SetTableViewFromList(self, tableView, listView):
        list = []#listView

        for obj in listView:
            list.append(obj)
        model = QtGui.QStandardItemModel( tableView )
        # 设置表格属性：
        # print(list)
        model.setRowCount( len( list ) )
        model.setColumnCount( len( list[0] ) )
        # 设置表头
        for i in range( len( list[0] ) ):
            model.setHeaderData( i, Qt.Horizontal, (list[0][i]) )
        tableView.setModel( model )

        list.remove( list[0] )
        if len( list ) == 0:
            return

        for i in range( len( list[0] ) ):
            model.setItem( len( list ), i, QtGui.QStandardItem( str( 0 ) ) )

        for j in range( len( list ) ):
            orders = list[j]
            for i in range( len( orders ) ):
                model.setItem( j, i, QtGui.QStandardItem( str( orders[i] ) ) )
        tableView.setModel( model )