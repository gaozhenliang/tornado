import os
BASE_DIRS = os.path.dirname(__file__)

#参数
options = {
    'port':9001
}

#数据库配置
mysql = {
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'itc123',
    'dbName':'test'
}

#配置
settings = {
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'debug':True
}