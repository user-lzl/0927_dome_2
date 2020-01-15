"""
测试待发货接口
"""
# 导入unittest
import unittest
from interface.to_be_shipped_interface import ToBeShipped
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
        self.shipped = ToBeShipped()
        result = self.shipped.to_be_shipped(self.user_data)
        print(result)
        """断言"""
        succeed = get_keyword(result, "succeed")
        self.assertTrue(succeed, msg="失败")

if __name__ == '__main__':
    unittest.main()