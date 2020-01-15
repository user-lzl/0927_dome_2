"""
test_wait_collect_goods
测试待收货
"""
# 导入 unittest
import unittest
from interface.wait_collect_goods import WaitCollectGoods
from common.getkeyword import get_keyword
from common.operation_data import OperationFile
import ddt
user_data = OperationFile("userdata.csv").get_data_to_dict()


@ddt.ddt
class TestWaitCollectGoods(unittest.TestCase):
    @ddt.data(*user_data)
    def test_wait_collect_goods(self,data):
        self.user_data = {"name": str(data["username"]),
                          "password": str(data["password"])}
        self.wcg = WaitCollectGoods().wait_collect_goods(self.user_data)
        print(self.wcg)
        """断言"""
        succeed = get_keyword(self.wcg, "succeed")
        self.assertTrue(succeed, msg="失败")


if __name__ == '__main__':
    unittest.main()