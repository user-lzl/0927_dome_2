"""
测试取消订单接口
"""
# 导入unittest
import unittest
from interface.cancel_order_interface import CancelOrder
from common.getkeyword import get_keyword
from common.operation_data import OperationFile
import ddt
user_data = OperationFile("userdata.csv").get_data_to_dict()

@ddt.ddt
class TestCancelOrder(unittest.TestCase):
    @ddt.data(*user_data)
    def test_cancel_order_interface(self,data):
        """取消订单"""
        self.user_data = {"name": str(data["username"]),
                          "password": str(data["password"])}
        order = CancelOrder().cancel_order_interface(self.user_data)
        print(order)
        """断言"""
        succeed = get_keyword(order, "succeed")
        self.assertTrue(succeed, msg="失败")


if __name__ == '__main__':
    unittest.main()