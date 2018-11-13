# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-11-12 16:31
# * Last modified : 2018-11-12 16:31
# * Filename      : GetTodayExcel.py
# * Description   : 
# **********************************************************
import time
import xlwt
import xlrd

time = time.localtime(time.time())
y = time.tm_year
m = time.tm_mon
d = time.tm_mday

#book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#sheet=

class ExcelTaskReader(object):

    def __init__(self, name):
        self.name = name
        #self.date = date
        self.todolist = []

    def getTasks(self, cdate, finished_state = 'no'):
        #base_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/' )
        #xls_path = '/Content/{name1}/{name2}_Calendar.xls'.format(name1=self.name, name2=self.name)
        #xls_path = base_dir + xls_path
        xls_path = 'D:/GitFiles/What-To-Do-Reminder/Content/{name1}/{name2}_Calendar.xls'.format(name1=self.name, name2=self.name)
        book = xlrd.open_workbook(xls_path)
        sht = book.sheet_by_index(0)
        nrows = sht.nrows
        for i in range(1, nrows):
            #print(sht.row_values(i))
            if sht.row_values(i)[0] == cdate and sht.row_values(i)[2] == finished_state:
                self.todolist.append(sht.row_values(i))


'''
if __name__ == '__main__':
    t = ExcelTaskReader('HuJian')
    t.getTasks('2018.11.12')
    print(t.todolist)
'''
