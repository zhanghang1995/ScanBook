#-*- coding:UTF-8 -*-

import os

#遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    list2 = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s'%(filepath,allDir))
        # child1 = child.encode('utf-8')
        list2.append(child)
        # print(child)
    return list2
#解决中文显示乱码的问题

#读去文件的内容并打印
def readFile(filename):
    fopen = open(filename,'r')
    for eachline in fopen:
        print("输入的内容为：",eachline)
    fopen.close()


#输入多行文字，写入到指定的文件并保存在指定的文件夹中

def writeFile(filename,data):
    string_data = ""
    fopen = open(filename,'a')
    print(data['log_id'])
    print(data['direction'])
    print(data['words_result_num'])
    # print(result_data['words_result'])
    for data in data['words_result']:
        string_data = data['words']

        fopen.writelines("%s%s" % (string_data, os.linesep))
    # while True:
    #     aline = input()
    #     if aline !=".":
    #         fopen.write("%s%s"%(aline,os.linesep))
    #     else:
    #         print("文件已保存")
    #         break

# if __name__ =="__main__":
#     filePath = ""
#     filePathI = ""
#     fileroot="C:/Users/Administrator/Desktop/print"
#     eachFile(fileroot)


