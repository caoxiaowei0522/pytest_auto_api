import copy
from common.baseAPI import BaseAPI
from config.config import num_pws
from utils.handle_data import get_md5_data


class Login(BaseAPI):
    def login(self,indata,getToken=False):
        indata = copy.copy(indata)#浅拷贝下数据--避免修改全局数据
        indata['password'] = get_md5_data(indata['password'])
        resp=self.request_send(data=indata)
        if getToken:  # 获取token
            return resp['data']['token']
        else:  # 获取响应数据
            return resp

if __name__ == '__main__':
    print(Login().login(num_pws,getToken=True))