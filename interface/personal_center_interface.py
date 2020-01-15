"""
1.测试个人中心接口方法
"""
from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface


class PersonalCenterInterface(object):
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/info"

    def personal_center(self, login_data):
        """
        个人中心接口
        :param login_data: a={"name": "user11", "password": "123456"} 传入用户名跟密码
        :return:
        """
        session = LoginInterface().get_session(login_data)
        pci_data = {"session": session}
        return SendMethod.send_post(url=self.url, data=pci_data)


if __name__ == '__main__':
    login_data = {"name": "user11", "password": "123456"}
    pci = PersonalCenterInterface()
    print(pci.personal_center(login_data))
