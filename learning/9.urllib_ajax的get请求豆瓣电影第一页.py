# get请求
# 获取豆瓣电影的第一页的数据 并且保存起来
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

# (1)请求对象的定制
request = urllib.request.Request(url = url,headers = headers)

# (2)获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

# (3)数据下载到本地
# open方法默认情况下使用的是gbk编码，如果我们想保存汉字，那么必须要改编码为utf-8
with open('douban_movie.json', 'w', encoding='utf-8') as fp:
    fp.write(content)



