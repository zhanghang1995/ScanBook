# from flask import Flask
#引入文字识别的OCR
from aip import AipOcr
import json
from search_file import eachFile,writeFile


#定义常量
APP_ID= "10970720";
API_KEY= "fiTSqUdjCL2hRx1zogqIBQj6";
SECERT_KEY = "zkXgFdDvmowz9a3AmGyYNS7UxNaDZ2BT";
#初始化ApiOcr对象
apiocr = AipOcr(APP_ID,API_KEY,SECERT_KEY)
#返回结果json
result_data = None
#配置AipOcr
# #建立连接的超时时间
# apiocr.setConnectionTimeoutInMillis(2000)
# #建立打开的链接传输数据的超时间
# apiocr.setSocketTimeoutInMillis(2000)

#读取图片
def get_file_content(filpath):
    with open(filpath,'rb') as fp:
        return fp.read()

#定义参数变量
options = {
    'detect_direction':'true',
    'language_type':'CHN_ENG',
}

if __name__ == '__main__':
    #获取得到的图片
    # print("\r请输入文件的名称 ")
    # print("\r请输入文件保存地址 ")
    # file = input()
    # savefile = input()
    file = "c:/users/administrator/desktop/print/"
    savefile = "c:/users/administrator/desktop/save/result.txt"
    list3 = eachFile(file)

    #调用通用文字识别的接口
    for eachlist in list3:
        result  = apiocr.basicGeneral(get_file_content(eachlist),options)
        json_data = json.dumps(result)
        result_data = json.loads(json_data)

    #将返回的结果保存在指定的文件中
        writeFile(savefile,result_data)


#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
