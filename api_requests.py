import os
from setting import *
import requests

#print(txt_path)

def Get_url(url,a,b):
    try:
        response = requests.get(url,data=a,params=b)
        
        if response.status_code != 200:
            print("!=200")
            with open(txt_path,'a')as f:
                f.write(url+"     "+str(response.status_code)+"massage"+str(response.text))
                f.write('\n')
        else:
            print("200")
            print(str(url),"pass")
        return None
    except:
        pass


def Post_url(url,a,b):
    try:
        
        response = requests.post(url,data=a,params = b)

        if response.status_code != 200:
            print("!=200")
            with open(txt_path,'a')as f:
                f.write(url+"     "+str(response.status_code)+"massage"+str(response.text))
                f.write('\n')
        else:
            print("200")
            print(str(url),"pass")
        return None
    except:
        pass
