# urlencode 应用场景：多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男"
# data = {
#     'wd':"周杰伦",
#     "sex":"男",
#     "location":"中国台湾省"
# }
# a = urllib.parse.urlencode(data)
# print(a)

# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&locaton=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81网页源码
import urllib.request
import urllib.parse
base_url = "https://www.baidu.com/s"
data = {
    'wd': "周杰伦",
    # 注意：以下两个参数可能不会被百度搜索使用
    "sex": "男",
    "location": "中国台湾省"
}
new_data = urllib.parse.urlencode(data)
# 在URL中，问号（?）是一个特殊字符，用于分隔URL的基地址（base URL）和查询字符串（query string）。
url = base_url + "?" + new_data  # 确保这里有一个问号
# 确保 headers 中不包含非 ASCII 字符
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
try:
    response = urllib.request.urlopen(request)
    # 获取网页源码的数据
    content = response.read().decode("utf-8")
    # 打印数据
    print(content)
except UnicodeEncodeError as e:
    print(f"编码错误: {e}")
