from libs.login import  Login
import xlrd
import pytest, allure

"""
测试文件执行条件：
    1- 该业务层代码封装ok
    2- 需要自动化测试用例----数据驱动-使用指定文件类型做
        功能用例：人去执行
            1- excel
            2- word
            3- xmind
            4- yaml
            5- 数据库
        自动化用例选型：靠代码或者工具
            1- excel
            2- yaml

"""
from libs.login import Login
from utils.handle_data import get_md5_data
from utils.handle_path import report_path
from common.baseAPI import ApiAssert
import os


@allure.epic('外卖项目')
@allure.feature('登录模块')
class TestLogin:
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('登录模块', 'Login', '标题', '请求参数', '响应预期结果'))
    @allure.title("{title}")
    def test_login(self, title, inBody, expData):
        res = Login().login(inBody)
        # 断言:1-局部关键信息相等  2- 包含关系 in
        ApiAssert.define_api_assert(res['msg'], '=', expData['msg'])


# SHIFT+tab  往前缩进 ，tab  往后缩进
if __name__ == '__main__':
    # 输出 打印信息 -s
    # --clean-alluredir   清空json上一次运行的数据文件
    pytest.main(['test_login.py', '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')