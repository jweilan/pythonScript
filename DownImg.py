# -*- coding:utf-8 -*-
import re
import requests
import os

# 正则抓图片规则
rule = '"objURL":"(.*?)",';
# 保存的跟文件目录
mkName = "downImg/"


def dowmloadPic(html, keyword):
    pic_url = re.findall(rule, html, re.S)
    i = 1
    path = mkName+keyword;
    if os.path.exists(path) == False:
        os.mkdir(path)

    print(pic_url)
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        dir = path+'/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url,verify=False)
    dowmloadPic(result.text, word)


# python中对文件、文件夹的操作需要涉及到os模块和shutil模块。

# 创建文件：
# os.mknod(“test.txt”) 创建空文件 
# open(“test.txt”,w) 直接打开一个文件，如果文件不存在则创建文件

# 创建目录：
# os.mkdir(“file”) 创建目录

# 复制文件：
# shutil.copyfile(“oldfile”,”newfile”) oldfile和newfile都只能是文件 
# shutil.copy(“oldfile”,”newfile”) oldfile只能是文件夹，newfile可以是文件，也可以是目标目录

# 复制文件夹：
# shutil.copytree(“olddir”,”newdir”) olddir和newdir都只能是目录，且newdir必须不存在

# 重命名文件（目录）
# os.rename(“oldname”,”newname”) 文件或目录都是使用这条命令

# 移动文件（目录）
# shutil.move(“oldpos”,”newpos”)

# 删除文件
# os.remove(“file”)

# 删除目录
# os.rmdir(“dir”) 只能删除空目录 
# shutil.rmtree(“dir”) 空目录、有内容的目录都可以删

# 转换目录
# os.chdir(“path”) 换路径

# 判断目标
# os.path.exists(“goal”) 判断目标是否存在 
# os.path.isdir(“goal”) 判断目标是否目录 
# os.path.isfile(“goal”) 判断目标是否文件