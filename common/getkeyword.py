"""
getkeyword.py
获取返回值中的某一个字段,用于接口间的关联
实际上就是对字典一个操作,通过字典的键查找对应的值
通过jsonpath库获取字段值
安装jsonpath
    pip install jsonpath
使用jsonpath
    jsonpath.jsonpath(数据源,"$..关键字")
"""
import jsonpath


def get_keyword(data: dict, keyword):
    """
    通过关键字获取对应的值,如果关键字对应的值由多个,那么只获取第一个
    :param keyword:字典关键字
    :param data:数据源
    :return:
    """
    try:
        return jsonpath.jsonpath(data, f"$..{keyword}")[0]
    except Exception as e:
        print(f"获取关键字失败:{e}")


def get_keywords(data: dict, keyword):
    """
    通过关键字获取对应的所有值
    :param keyword:字典关键字
    :param data:数据源
    :return:
    """
    return jsonpath.jsonpath(data, f"$..{keyword}")


if __name__ == '__main__':
    response_data = {
        "count": 8,
        "next": None,
        "previous": None,
        "results": [{"dep_id": "T02",
                     "dep_name": "新东方学院_2",
                     "master_name": "贾伟_2",
                     "slogan": "学测试到蓝翔"},

                    {"dep_id": "T03",
                     "dep_name": "C++/学院",
                     "master_name": "C++-Master",
                     "slogan": "Here is Slogan"}, ]}
    print(get_keyword(response_data, "dep_id"))
    print(get_keywords(response_data, "dep_id"))
