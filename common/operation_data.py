"""
operation_data.py
读写文件  csv/Excel表格
使用pandas
"""
import os
import xlrd
import pandas
import random
from xlutils.copy import copy


class OperationFile:
    def __init__(self,filename:str):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\data"  # 相当于"../data"
        self.filepath = os.path.join(base_path, filename)  # 文件路径
        if filename.split(".")[-1] == "csv":
            self.file = pandas.read_csv(os.path.join(base_path,filename))  # 读取csv格式的文件
        else:
            self.file = pandas.read_excel(os.path.join(base_path,filename))

    def get_data_to_list(self):
        """
        将数据读取成列表嵌套列表格式
        :return:
        """
        return self.file.values.tolist()

    def get_data_to_dict(self):
        """
        将数据读取成列表嵌套字典格式
        :return:
        """
        return [self.file.loc[i].to_dict() for i in self.file.index.values]

    def write_data_to_excel(self,data:list):
        """
        更新表格
        1.读取表格元数据
        2.将新数据插入在第一行位置
        3.将源数据追加在第一行之后
        """
        # 读取源数据
        old_data = self.get_data_to_list()
        # 添加新数据在第一行
        self.file.loc[0] = data  # 指定插入行行号
        # 将老数据追在在第一行之后
        for i in range(1,len(old_data)+1):
            self.file.loc[i] = old_data[i-1]
        self.file.to_excel(self.filepath,index=None)  # 保存数据

    def write_data_col(self):
        """更新某一列数据"""
        filepath = self.filepath
        table = xlrd.open_workbook(filepath)  # 打开表
        new_table = copy(table)  # 复制数据出来
        new_sheet = new_table.get_sheet(0)
        for i in range(1, 6):  # 预计更新的数据个数,忽略首行
            num = random.randint(1000000, 9999999)  # 随机生成货号
            new_sheet.write(i, 21, num)  # 将货号写入excel表中对应的列中,i:表示行,22:代表货号所在列
        new_table.save(filepath)  # 保存跟新后的记录

    def read_data(self):
        self.write_data_col()
        return self.get_data_to_dict()

if __name__ == '__main__':
    oper = OperationFile("userdata.xls")
    data = oper.get_data_to_list()
    # data = oper.get_data_to_dict()
    print(data)