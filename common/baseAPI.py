import requests
"""
没有封装的接口代码：每一个自动化测试方法都需要加异常机制+log
基类的封装思路：
    1- 加入异常机制+log
    2- 截图操作---ui 自动化
    3- 一般模块的常用接口：
        增删改查 
    4- 代码不太可能一次性写的完整！
def request(method, url, **kwargs)
#
method, url
接口风格：
    1- 常规风格：
        1、一个模块，增删改查的4个接口的路径的不一样--自定义性比较强
        2、请求和响应数据类型不定
    2- restful风格
        1、一个模块，增删改查的4个接口的路径的一样的
        2、请求和响应数据类型一样的--json格式

一个项目的版本定下来之后：
    一个接口有10个用例：
        1- 变的是： 接口的描述、接口的用例请求参数、预期的响应
        2- 不变的是: url  请求方法
"""
from utils.handle_yml import get_yaml_data
import inspect
from config.config import HOST
class BaseAPI:#基类
    def __init__(self):#初始化方法
        #__class__.__name__ 获取类名
        print('当前类名是>>> ',self.__class__.__name__)
        #通过模块名去获取对应模块的数据
        self.data = get_yaml_data('../config/apiConfig.yml')[self.__class__.__name__]

     #--------公共的发送方法----------每一个接口方法都会调用这个去发送请求
    def request_send(self,data=None):
        methodName = inspect.stack()[1][3]#谁调用了我，他的函数名
        path,method = self.data[methodName].values()
        # 数据---需要剥离对应某一个接口的数据

        resp = requests.request(method=method,url= f'{HOST}{path}',data=data)

        print(methodName,'---',self.data[methodName])
        return resp.json()

