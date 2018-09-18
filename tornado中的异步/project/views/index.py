import tornado.web
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient   #异步的http请求客户端
import time
import json
from tornado.websocket import WebSocketHandler

class StaticHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticHandler,self).__init__(*args,**kwargs)
        self.xsrf_token


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')


class ChatHandler(WebSocketHandler):
    users = [] #存储每一个人的信息

    #连接建立后被调用
    def open(self):   #客户端建立链接后调用open
        #链接上后在进行存储用户信息
        self.users.append(self)   #self 为每个连接服务器的客户端的对象
        # print(self.users)
        for user in self.users:
            print(self.request.remote_ip)
            user.write_message('u[{}]登陆了'.format(self.request.remote_ip))  #主动向客户端发送message消息，message可以是字符串或者字典，


    def on_message(self, message):  #客户端发送消息过来时服务器调用on_message
        for user in self.users:
            user.write_message(u'{}说：{}'.format(self.request.remote_ip,message))   #write_message的消息会被前端ws.onmessage方法接收



    def on_close(self):    #客户端断开链接调用on_close
        self.users.remove(self)
        for user in self.users:
            print(user)
            user.write_message('u[{}]退出登陆了'.format(self.request.remote_ip))





    def check_origin(self, origin):  #判断源origin，对于符合条件的请求源允许链接
        return True






'''
class Student1Handler(RequestHandler):
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




class Student2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'

        # 创建客户端
        client = AsyncHTTPClient()

        res = yield client.fetch(url)

        if res.error:
            self.send_error(500)
        else:
            data = res.body
            self.write(data)


class Student3Handler(RequestHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)

    #将耗时操作写在此函数当中
    @tornado.gen.coroutine
    def getData(self):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'

        client = AsyncHTTPClient()
        res = yield client.fetch(url)

        if res.error:
            ret = {'ret':0}
        else:
            ret = res.body

        raise tornado.gen.Return(ret)   #相当于那个send
'''

