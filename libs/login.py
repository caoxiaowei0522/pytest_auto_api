num_pws={'username':'1234','password':'123456'}
from common.baseAPI import BaseAPI
class Login(BaseAPI):
    def login111(self,indata):
        resp=self.request_send(data=indata)
        print(resp.text)
if __name__ == '__main__':
    Login().login111(num_pws)