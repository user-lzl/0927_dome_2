"""
1.待付款接口方法
"""
from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface
from common.getkeyword import get_keyword
from common.getkeyword import get_keywords


class PendingPaymentInterface(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"

    def pending_payment_interface(self, user_data):
        """待付款接口"""
        session = LoginInterface().get_session(user_data)
        data = {"session": session,
                "type": "await_pay",
                "pagination": {
                    "count": 10,
                    "page": 1}}
        return SendMethod.send_post(url=self.url, data=data)

    def get_order_id(self,user_data):
        """获取单个订单id : 第一个"""
        goods_id = self.pending_payment_interface(user_data=user_data)
        return get_keyword(goods_id,"order_id")

    def get_order_ids(self,user_data):
        """获取全部订单id"""
        goods_id = self.pending_payment_interface(user_data=user_data)
        return get_keywords(goods_id,"order_id")

if __name__ == '__main__':
    ppi = PendingPaymentInterface()
    data = {"name": "user11", "password": "123456"}
    print(ppi.get_order_id(data))