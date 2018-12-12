import xlrd
import sys
from setting import *
sys.setrecursionlimit(1000000) 
def open_csv():
    names = locals()
    

    workbook = xlrd.open_workbook(excel_path)
    count = len(workbook.sheets())
    
    for i in range(count):
        names["sheet%s"%i] = workbook.sheets()[i]
        names["nrows%s"%i] = names["sheet%s"%i].nrows
        #open_csv()["nrows0"]
    return names
    
#open_csv()
#print(open_csv()["sheet1"].row_values(1)[3])

