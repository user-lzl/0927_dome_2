"""
goods_to_be_received
订单:待收货接口
"""
# 导入 登录,发送方法(send_method)
from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface


class WaitCollectGoods(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"

    def wait_collect_goods(self,user_data):
        """
        待收货接口
        :param user_data: 登录数据(用户名密码,字典格式)
        :return:
        """
        session = LoginInterface().get_session(user_data)
        data = {
            "session": session,
            "type": "shipped",
            "pagination": {
                "count": 10,
                "page": 1}}
        return SendMethod.send_post(url=self.url,data=data)


if __name__ == '__main__':
    data = {"name": "user11", "password": "123456"}
    print(GoodsToBeReceived().goods_to_be_received(data))