import urllib.request

# url = "https://blog.csdn.net/m0_74412436/article/details/1418560281"
url = "https://www.goudan111.com"
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
try:
    request = urllib.request.Request(url = url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError:
    print("系统正在升级......")

except urllib.error.URLError:
    print("我都说了 系统正在升级")