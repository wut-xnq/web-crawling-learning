# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

# post请求标志：x-requested-with: XMLHttpRequest

# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10


# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10
import urllib.request
import urllib.parse
def creat_request(page):
    base_url =  "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    data = {
         "cname": "北京",
         "pid":"",
         "pageIndex": page,
         "pageSize": "10"
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url = base_url,headers=headers,data = data)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_load(content,page):
    with open("kfc_" + str(page) +  ".json" , "w",encoding='utf-8') as fp:
        fp.write(content)
if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page,end_page+1):
        # 请求对象的定制
        request = creat_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content,page)