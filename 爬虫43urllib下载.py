import urllib.request
#urllib 下载爬取到的图片以及音乐等

#下载网页
#url_page='http://www.baidu.com'
#urlretrieve()中的参数两个,一个是下载地址,一个是保存下的文件名, 其中第一个参数url代表了下载的路径 其中第二个参数filename代表文件的名字
#在python中可以直接写变量的名字在参数中或者直接写变量的值在参数中
#意思就是如下所展示 在第一个参数处写url=url_page 或者在第一个参数处直接写url_page
#urllib.request.urlretrieve(url_page,'baidu.html')

#下载图片 图片一般采用jpg的格式
#url_image='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fblog%2F202008%2F12%2F20200812063353_pqdcs.thumb.1000_0.jpg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1657680452&t=79c3057d219d749fe3ddec4671a4ab93.jpg'
#urllib.request.urlretrieve(url_image,'lisa_image')
#下载视频 视频一般采用MP4的格式保存 所以后缀要写上文件的格式 
url_video='https://www.bilibili.com/video/BV1Pg41197un?t=2.5'


