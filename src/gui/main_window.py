from gui.mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from src.lib import annaerExcel
from src.lib import alipay

class MainWindow(QMainWindow, Ui_MainWindow):
    manyAccounts =[('姓名','支付宝','金额','操作')]
    signAccounts =[('姓名','支付宝','金额','操作')]
    zfb=None
    def __init__(self):
        super( MainWindow, self ).__init__()
        self.setupUi( self )
        self.setAttribute( Qt.WA_QuitOnClose )

        self.pushButton_import.clicked.connect( self.openFile )

    def openFile(self):
        path = QFileDialog.getOpenFileName( self, "open file dialog", "", "excel(*.xls)" )
        if path[0] != '':
            self.excel=annaerExcel.annaerExcel(path[0])
            accounts = self.excel.getAccounts()#.insert(0, ('姓名', '支付宝', '金额'))
            for obj in accounts:
                self.manyAccounts.append((obj[0],obj[1],obj[2], '未填写'))
            self.SetTableViewFromList(self.tableView_many, self.manyAccounts)

    def fillMany(self):
        if self.zfb == None:
            self.zfb=alipay.alipay()

        for i in  range(0.17):
            if self.zfb.addPointer() == False:
                return

        #for i in range(1, len(manyAccounts)):




    def SetTableViewFromList(self, tableView, list):
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
                try:
                    # print()
                    value = float( model.data( model.index( len( list ), i ) ) ) + float( orders[i] )
                except Exception as e:
                    print( e )
                else:
                    model.setItem( len( list ), i, QtGui.QStandardItem( str( round( value, 2 ) ) ) )
        model.setItem( len( list ), 0, QtGui.QStandardItem( "合计" ) )
        tableView.setModel( model )