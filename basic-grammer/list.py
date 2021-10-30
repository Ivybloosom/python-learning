""" 
Date: 
LastEditors: liang
Author: liang
LastEditTime: 2021/10/30 1:15 下午

IDE: PyCharm
"""


def list_sort():
    user_list_dict = [
        {"name": "zhaoliang", "age": 15},
        {"name": "zhangsan", "age": 13}
    ]
    user_list_dict.sort(key=lambda x: x['age'])
    print(user_list_dict)


def main():
    list_sort()


if __name__ == '__main__':
    main()
