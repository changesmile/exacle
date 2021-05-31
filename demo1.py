import sys
import numpy as np


def openFile():
    with open("D:\\demo.txt", "r", encoding='utf-8') as f:  # 打开指定地址的txt文件
        for line_l in f.readlines():  # 循环读取每一行的数据
            line_chaifen = line_l.split()  # 将读取的数据进行空格区分，并存入数据
            yield line_chaifen[:4]  # yield相当于return，返回当前数组数据并只取前X个


f = openFile()
cmp_time = ("2021-03-07", "2021-03-02", "2021-03-03", "2021-03-04")
# 定义一个比较时间的数组
cmp_ip = []
# 定义一个IP数组
top_num = 0
# 定义一个日期、IP的下标
sum_live = np.zeros(2)
# 定义一个全是0的数组用于记录活跃人数


def CmpIp(ip):
    if len(cmp_ip) == 0:
        cmp_ip.append(ip)
        sum_live[top_num] = sum_live[top_num] + 1   # IP数组为空直接添加进IP数组
        return
    if ip not in cmp_ip:   # 如果IP不在IP数组里头，则添加IP数组
        cmp_ip.append(ip)
        sum_live[top_num] = sum_live[top_num] + 1  # 活跃人数+1


while True:
    try:
        line = next(f)  # line指向yield中返回的数据
        line_time = line[0]
        line_ip = line[2]
        line_user = line[3]
        # print(line_time + "    " + line_ip)
        if cmp_time[top_num] == line_time:          # 时间相同进入该判断
            CmpIp(line_ip)
        elif cmp_time[top_num + 1] == line_time:    # 时间不同，下标下移
            top_num = top_num + 1
            cmp_ip.clear()  # 清空数组
            CmpIp(line_ip)
        else:
            top_num = top_num + 1
            cmp_ip.clear()  # 清空数组
    except StopIteration:
        print(sum_live)     # yield取到最后指向空值时，终止循环
        sys.exit()