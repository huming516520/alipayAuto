import xlrd
import xlwt

class annaerExcel:
    def __init__(self, path):
        print(path)
        # 打开文件
        self.workbook = xlrd.open_workbook( path )



    def getAccounts(self):
        accounts=[]
        sheet = self.workbook.sheet_by_index( 0 )  # 通过sheet索引获得sheet对象
        if sheet.cell_value( 0, 4) != '姓名'or sheet.cell_value( 0, 5) != '支付宝' or sheet.cell_value( 0, 6) != '提现金额':

            return accounts

        for i in range(1,sheet.nrows):
            name = sheet.cell_value( i, 4 )
            account = (str)(sheet.cell_value( i, 5 ))
            amount = sheet.cell_value( i, 6 )
            if account.find('+') != -1:             #去除+
                account = account.split('+')[0]
            if account.find('.0') != -1:             #去除+
                account = account.split('.0')[0]
            repeat = False
            for item in accounts:
                if item[1] == account:  #账号相同，合并金额
                    accounts.append( (name, account, round(float(amount) + float(item[2]), 2)) )
                    accounts.remove(item)
                    repeat = True
                    continue
            if repeat == False:
                accounts.append((name, account, amount))

        return accounts

