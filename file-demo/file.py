"""
Date:
LastEditors: liang
Author: liang
LastEditTime: 2022/9/21

IDE: PyCharm
"""


def fileHandle():
    file_input = open("input.txt", "r")
    file_output = open("公司名称.txt", "w")

    province_name_list = []
    company_name_list = []

    lines = file_input.readlines()
    for line in lines:
        line_list = line.strip().split("：")
        if len(line_list) > 1:
            province_name_list.append(line_list[0])

        line_list = line.strip().strip("、").split("、")  # 去掉换行符和末尾不要的字符
        if len(line_list) > 1:
            company_name_list.append(line_list)

    for i in range(0, 19):
        province_name = province_name_list[i]

        company_name = company_name_list[i]
        for company in company_name:
            output_str = province_name + company + "有限责任公司" + "\n"
            file_output.write(output_str)

        file_output.write("\n")

    file_input.close()
    file_output.close()


def main():
    fileHandle()


if __name__ == '__main__':
    main()
