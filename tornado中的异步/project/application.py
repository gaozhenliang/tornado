import os
import config
import tornado.web
from views import index
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/students',index.StudentHandler),
            (r'/home',index.HomeHandler),
            (r'/(.*)$',index.StaticHandler,
            {'path':os.path.join(config.BASE_DIRS,'static/html'),'default_filename':'index.html'}
             )
        ]
        super(Application,self).__init__(handlers,**config.settings)