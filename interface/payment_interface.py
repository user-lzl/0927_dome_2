"""
付款接口方法
"""
from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface    # 登录
from interface.pending_payment_interface import PendingPaymentInterface


class PaymentInterface(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/pay"

    def payment_interface(self, user_data):
        """
        付款接口: 需要:付款的商品id
        这里固定选择第一个商品
        :param user_data: 传入登录数据
        :return: 返回付款接口返回值
        """
        # 实例化登录 
        session = LoginInterface().get_session(user_data)  # 获得session(登录的uid,sid)
        order_id = PendingPaymentInterface().get_order_id(user_data)  # 获得单个商品id
        data = {
            "session": session,
            "order_id":order_id }
        return SendMethod.send_post(url=self.url,data=data)


if __name__ == '__main__':
    data = {"name": "user11", "password": "123456"}
    print(PaymentInterface().payment_interface(data))