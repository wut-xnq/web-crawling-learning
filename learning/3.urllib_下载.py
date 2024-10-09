import urllib.request

# 下载网页
url_page = "https://s.diyifanwen.com/down/down.asp?url=https://www.diyifanwen.com/yanjianggao/jingxuanyanjianggao/7984914.html&obid=fanwen"

# url 代表的是下载路径 filename 代表的是文件名字
urllib.request.urlretrieve(url_page,"baidu.html")

# 下载图片
url_img = "https://tse1-mm.cn.bing.net/th/id/OIP-C.kx9cEIe4LN2Sa8MZCA9JFgHaFj?w=260&h=187&c=7&r=0&o=5&dpr=1.5&pid=1.7"
urllib.request.urlretrieve(url = url_img,filename = "lisa.jpg")

# 下载视频
url_video = "http://vod.v.jstv.com/video/2022/9/10/20229101662793010859_65_1591.mp4"

urllib.request.urlretrieve(url = url_video,filename = "new_video.mp4")
#