"""
付款接口:需要商品订单id
"""
# 导入unittest
import unittest
from common.getkeyword import get_keyword
from interface.payment_interface import PaymentInterface
from common.operation_data import OperationFile
import ddt
user_data = OperationFile("userdata.csv").get_data_to_dict()


@ddt.ddt
class TestPaymentInterface(unittest.TestCase):
    @ddt.data(*user_data)
    def test_payment_interface(self,data):
        self.user_data = {"name": str(data["username"]),
                          "password": str(data["password"])}
        self.payment = PaymentInterface() # 实例化付款
        result = self.payment.payment_interface(self.user_data)
        print(result)
        """断言"""
        # 获取succeed
        succeed = get_keyword(result, "succeed")
        self.assertTrue(succeed, msg="失败")


if __name__ == '__main__':
    unittest.main()
