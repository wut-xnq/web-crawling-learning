import urllib.request
import urllib.parse
# （1）下载豆瓣电影前10页的数据
# （1）请求对象的定制
#   (2) 获取相应的数据
#   (3) 下载数据
def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

    data = {
        "start":(page - 1) * 20,
        "limit":20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    # print(url)
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    request = urllib.request.Request(url = url,headers=headers)
    return request

def get_content(request):
    response = response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open("douban_" + str(page) + ".json","w",encoding="utf-8") as fp:
        fp.write(content)
# 程序的入口
if __name__ == '__main__':
    start_page = int(input("请输入起始的页码:"))
    end_page = int(input("请输入介绍的页面:"))

    for page in range(start_page,end_page+1):
#       每一页都有自己请求对象的定制,并获取相应的数据
        request = create_request(page)
        content = get_content(request)
#       下载
        down_load(page,content)

# 快捷键：ctrl + shift + alt + L