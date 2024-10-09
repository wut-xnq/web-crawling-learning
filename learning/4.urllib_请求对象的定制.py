import urllib.request

url = "https://www.baidu.com"

# url的组成
# http/https            www.baidu.com         s           wd = 周杰伦        #
#   协议          主机          端口号         路径          参数             锚点
# http 80
# https 443
# mysql 3306
# oracle 1521
# redis 6379
# mongodb  27017

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

# 因为urlopen方法中不能存储字典，所以headers不能传递进去
# 请求对象的定制
request = urllib.request.Request(url = url,headers = headers)


response =  urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)