"""
1.测试登录接口方法
2.获取session方法

"""
from common.sendmethod import SendMethod
from common.getkeyword import get_keyword


class LoginInterface:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"

    def login(self,data):
        """请求登录接口"""
        return SendMethod.send_post(url=self.url,data=data)

    def get_session(self,data):
        """获取登录后的session"""
        response = self.login(data=data)
        return get_keyword(response,"session")

if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name":"user11","password":"123456"}
    # print(login.login(data))
    session = login.login(data=login_data)
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/info"  # 个人中心请求地址
    userinfo_data = {"session":session}  # 个人中心请求参数
    print(login.get_session(login_data))




