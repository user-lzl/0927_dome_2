"""
测试待发货接口
"""
# 导入unittest
import unittest
from interface.historical_order import HistoricalOrder
from common.getkeyword import get_keyword
from common.operation_data import OperationFile
import ddt
user_data = OperationFile("userdata.csv").get_data_to_dict()

@ddt.ddt
class TestToBeShipped(unittest.TestCase):
    @ddt.data(*user_data)
    def test_to_be_shipped(self,data):
        """待发货接口"""
        self.user_data = {"name": str(data["username"]),
                          "password": str(data["password"])}
        order = HistoricalOrder().historical_order_interface(self.user_data)
        print(order)
        """断言"""
        succeed = get_keyword(order, "succeed")
        self.assertTrue(succeed, msg="失败")


if __name__ == '__main__':
    unittest.main()