from setting import *
import read_csv
from read_csv import open_csv
import connect_db
from api_requests import *
import time

with open(txt_path,'a')as m:
    m.write('\n')
    m.write(time.ctime())
    m.write('\n')

for i in range(open_csv()["nrows1"]):
    url = test_url+open_csv()["sheet1"].row_values(i)[0]
    data=open_csv()["sheet1"].row_values(i)[2]
    params = open_csv()["sheet1"].row_values(i)[3]
    print(data)
    if open_csv()["sheet1"].row_values(i)[1] == 'get':
        #print("get")
        Get_url(url,data,params)
        
    else:
        #print("post")
        Post_url(url,data,params)
