"""
测试待发货接口
"""
# 导入登录
from interface.login_interface import LoginInterface
from common.sendmethod import SendMethod


class ToBeShipped(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"

    def to_be_shipped(self, user_data):
        """
        待发货接口测试
        :param user_data:传入登录数据(用户名密码)
        :return:
        """
        session  = LoginInterface().get_session(user_data)
        data = {
            "session": session,
            "type": "await_ship",
            "pagination": {
                "count": 10,
                "page": 1  }}
        return SendMethod.send_post(url=self.url,data=data)


if __name__ == '__main__':
    data = {"name": "user11", "password": "123456"}
    print(ToBeShipped().to_be_shipped(user_data=data))