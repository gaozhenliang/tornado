import tornado.web
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient   #异步的http请求客户端
import time
import json

class StaticHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticHandler,self).__init__(*args,**kwargs)
        self.xsrf_token


class StudentHandler(RequestHandler):
    def on_response(self,response):
        if response.error:
            self.send_error(500)
        else:
            data = response.body
            # data = json.loads(response.body)
            print('data is {}'.format(type(data)))
            self.write(data)
        self.finish()   #由于不关闭通信通道所以当数据返回来时，需手动关闭通道

    @tornado.web.asynchronous  #不关闭通信的通道
    def get(self, *args, **kwargs):
        #获取所有学生的信息
        # time.sleep(20)

        url='http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        #创建客户端
        client = AsyncHTTPClient()
        client.fetch(url,self.on_response)   #对这个网址发起请求(这个服务器的handler向这个网址发起网络请求)



class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')
