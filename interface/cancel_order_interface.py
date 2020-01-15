"""
取消订单接口
"""
# 导入登录,发送方法(send_method)
from interface.login_interface import LoginInterface
from common.sendmethod import SendMethod
from interface.pending_payment_interface import PendingPaymentInterface


class CancelOrder(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/cancel"

    def cancel_order_interface(self, user_data):
        """
        取消订单接口测试
        :param user_data: 传入用户名密码
        :return:
        """
        session = LoginInterface().get_session(user_data)   # 获取 session(uid,sid)
        goods_id = PendingPaymentInterface().get_order_id(user_data)
        data = {
            "session": session,
            "order_id": goods_id}
        return SendMethod.send_post(url=self.url,data=data)


if __name__ == '__main__':
    data = {"name": "user11", "password": "123456"}
    print(CancelOrder().cancel_order_interface(data))