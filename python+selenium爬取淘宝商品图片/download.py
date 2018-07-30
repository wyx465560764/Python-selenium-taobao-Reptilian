
import urllib
from urllib import request
import os
def download(url,path=(os.path.abspath('.')+'/爬虫结果/')):
    # 截取文件名
    fileName = url.split("/")[-1:][0]
    #文件参数
    conn=urllib.request.urlopen(url)
    sub = conn.headers['Content-Type'].split("/")[-1:][0]
    print('后缀:',sub)
    conn.close()
    if fileName.find(".") == -1:
        fileName = fileName+sub
    print(fileName)
    print("downloading with urllib")
    urllib.request.urlretrieve(url,path+fileName)