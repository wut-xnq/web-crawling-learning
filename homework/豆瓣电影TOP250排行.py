# -*- coding: UTF-8 -*-
import sys
from bs4 import BeautifulSoup  # 网页解析 获取数据
import re  # 正则表达式 进行文字匹配
import urllib  # 制定URL 获取网页数据
import urllib.request
import xlwt  # 进行excel操作
import xlrd
import sqlite3  # 进行SQLite数据库操作


def main():
    base_url = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getdata(base_url)
    # print(datalist)
    savepath = ".\\豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    # askURL((base_url))
    # 4.读数据,显示信息
    read_excel(savepath)

findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式模式
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getdata(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串
            # print(item)  # 测试
            data = []
            item = str(item)
            link = re.findall(findlink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 留空

            rating = re.findall(findRating, item)[0]
            rating = rating.replace("</span>", "")
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")  # 留空
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格
            datalist.append(data)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    # 模拟浏览器头部信息向豆瓣服务器发送消息
    # 用户代理 表示告诉服务器 我们是什么类型的机器、浏览器（本质上是告诉浏览器我们可以接受什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    #  print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ["电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息"]
    for i in range(0, 8):
        sheet.write(0, i+1, col[i])  # 列名
    for i in range(0, 250):
        sheet.write(i + 1, 0, i + 1)  # 行名
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j + 1, data[j])
    book.save(savepath)

def read_excel(savepath):
    ls = []
    excel = xlrd.open_workbook(savepath)
    # 获取第一个sheet
    sheet = excel.sheets()[0]
    for row_index in range(sheet.nrows):
        row_data = sheet.row_values(row_index)
        ls.append(row_data)
    for line in ls[1:]:  # 跳过标题行
        # 提取line[0]
        value = str(int(line[0]))
        # 添加line[3]和line[4]
        value += " " + line[3] + " " + line[4]
        # 打印结果
        print(value)
if __name__ == "__main__":
    # 调用函数
    main()
    print("爬取完毕")
