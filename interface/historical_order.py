"""
测试历史订单接口
"""
# 导入登录 发送方法(send_method)
from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface


class HistoricalOrder(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"

    def historical_order_interface(self, user_data):
        session = LoginInterface().get_session(user_data)
        data = {
            "session": session,
            "type": "finished",
            "pagination": {
                "count": 10,
                "page": 1}}
        return SendMethod.send_post(url=self.url, data=data)


if __name__ == '__main__':
    data = {"name": "user11", "password": "123456"}
    print(HistoricalOrder().historical_order_interface(data))