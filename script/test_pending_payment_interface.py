"""
test_pending_payment.py
测试待付款接口
"""
"""
.表示执行通过的用例
F表示执行失败的用例
E表示代码出错的用例"""
# 导入unittest
import unittest
from interface.pending_payment_interface import PendingPaymentInterface
from common.getkeyword import get_keyword
from common.operation_data import OperationFile
import ddt
user_data = OperationFile("userdata.csv").get_data_to_dict()


@ddt.ddt
class TestPendingPayment(unittest.TestCase):
    @ddt.data(*user_data)
    def test_pending_payment(self,data):
        """待付款接口"""
        self.pend_pay = PendingPaymentInterface()
        self.user_data = {"name": str(data["username"]),
                          "password": str(data["password"])}
        pending_list = self.pend_pay.pending_payment_interface(user_data=self.user_data)
        print(pending_list)
        """断言"""
        # 获取succeed
        succeed = get_keyword(pending_list, "succeed")
        self.assertTrue(succeed, msg="失败")


if __name__ == '__main__':
    unittest.main()