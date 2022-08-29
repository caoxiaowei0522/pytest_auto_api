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
import inspect
from config.config import HOST
import os
import requests
from utils.handle_yml import get_yaml_data
class BaseAPI:
        def __init__(self):
            self.data = get_yaml_data('../config/apiConfig.yml')[self.__class__.__name__]
            print(self.data)
        def request_send(self, data=None):
            method_name = inspect.stack()[1][3]  # 谁调用了我，他的函数名
            print(method_name)
            path, method = self.data[method_name].values()
            print(path,method)
            resp = requests.request(method=method, url=f'{HOST}{path}', data=data)
            print(resp.request)

            print(method_name, '---', self.data[method_name])
            return resp




