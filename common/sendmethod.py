"""
封装sendmethod.py
根据ECShop的接口特点,封装对应的方法:
请求方式:POST
请求参数类型:urlenc  oded格式
"""
import requests
import json


class SendMethod:
    @staticmethod
    def send_post(url=None,data=None):
        # 对请求参数格式化
        ruqest_data = {
            "json":json.dumps(data)
        }
        response = requests.post(url=url,data=ruqest_data)
        return response.json()  # 接口返回值为json格式

if __name__ == '__main__':
    import json
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    data = {"name":"user11","password":"123456"}
    res = SendMethod.send_post(url=url,data=data)
    print(res)