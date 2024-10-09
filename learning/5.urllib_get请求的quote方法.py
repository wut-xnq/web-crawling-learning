import urllib.request
import urllib.parse
url = "https://www.baidu.com/s?wd="

# 请求对象的定制 为了解决反爬的第一张种手段
headers ={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

# 将周杰伦三个字变成unicode编码的格式
# 我们需要依赖于urllib.parse
name = urllib.parse.quote("周杰伦")

url = url + name

# 请求对象的定制
request = urllib.request.Request(url = url,headers = headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取相应的内容
content = response.read().decode("utf-8")

# 打印数据
print(content)