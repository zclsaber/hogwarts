import re
import csv
from collections import Counter
import pandas as pd


def get_latency(input_file, output_file):
    with open(input_file, encoding='utf-8') as f:
        content = f.read()
    #
    # # log = '''2023-06-17 19:25:33,071 [INFO] 拨测结果： {'Query': '94-test-cmb.cmchina.com.', 'TTL': '3600', 'RR': 'A', 'Answer': '1.1.1.94'}, 解析时延 解析时延：   2.99 ms'''
    #
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).*解析时延：\s*([\d.]+) ms'
    matches = re.findall(pattern, content, re.MULTILINE)
    # # print(matches)
    #
    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["时间", "时延"])
    #
        for match in matches:
            date_time = match[0]
            latency = match[1]
            # print(date_time)
            # print(latency)
            writer.writerow([date_time, latency])

# 获取出现次数最多的前xx%数据
def get_top_percent_values(filename, sheet_name, column_index, percent, asc='count'):
    # 读取Excel文件并提取待处理的列数据
    df = pd.read_excel(filename, sheet_name=sheet_name, header=None)
    values = df.iloc[:, column_index].tolist()

    # 统计每个数值出现的次数
    counter = pd.Series(values).value_counts().reset_index()
    counter.columns = ['Value', 'Count']

    # 按照出现的值大小进行降序排序
    if asc == 'value':
        sorted_counts = counter.sort_values('Value', ascending=False)
    else:
        sorted_counts = counter.sort_values('Count', ascending=False)

    total_values = len(values)
    threshold = int(total_values * percent)  # 计算90%的阈值
    # print(threshold)

    accumulated_count = 0
    result = []
    # 遍历排序后的统计结果，累计数值个数，直到达到或超过阈值
    for index, row in sorted_counts.iterrows():
        value = row['Value']
        count = row['Count']
        result.append((value, count))
        accumulated_count += count
        if accumulated_count >= threshold:
            break

    return result

# 获取PXX的数据（排序后前xx%的数据）
def get_pxx_data_from_excel(filename, column_index, percentage):
    # 读取Excel文件
    df = pd.read_excel(filename)

    # 获取指定列的数据
    column_data = df.iloc[:, column_index]

    # 计算Pxx数据
    pxx_data = column_data.quantile(percentage)

    return pxx_data

# 计算加权平均
def weighted_average(data_list):
    sum_product = 0
    total_weight = 0

    for data in data_list:
        value, weight = data
        sum_product += value * weight
        total_weight += weight

    if total_weight == 0:
        return 0  # 避免除以0的情况

    weighted_avg = sum_product / total_weight
    return weighted_avg

def calculate_result(files: list, sheet_name='Sheet1', column_index=1, percent=0.9):
    '''
    :param files: 传入一个包含解析时延数据的文件列表
    :param sheet_name: 替换成实际的工作表名，默认 Sheet1
    :param column_index: 替换成要处理的列索引，默认为 1，第二列
    :param percent: 替换成所需的百分比，默认0.9，意思取P90数据
    :return:
    '''
    for file in files:
        file_ext = r'C:\Users\fu\Downloads\\' + file
        result = get_top_percent_values(file_ext, sheet_name, column_index, 1, asc='value')
        print(f"{file.split('.')[0]} 的前{percent:.2%} 解析时延情况（时延，次数）: {result} ")
        wa = weighted_average(result)
        print(f"{file.split('.')[0]} 的加权平均解析时延为 {wa:.3}")
        p90 = get_pxx_data_from_excel(file_ext, 1, percent)
        print(f"{file.split('.')[0]} 的P{int(percent*100)} 数据: {p90}")
        print("\n")

input = r"C:\Users\fu\PycharmProjects\pythonProject\common_tools\cmb_stability.log"
input2 = r"C:\Users\fu\Downloads\cmb_stability.log"
output = r"C:\Users\fu\Downloads\cmb_latency_20230830_1.csv"

files = ['第一轮-70%.xlsx', '第一轮-80%.xlsx', '第一轮-90%.xlsx', '第一轮-95%.xlsx', '第二轮-80%.xlsx',
         '第二轮-90%.xlsx', '第二轮-95%.xlsx', '第三轮-80%.xlsx', '第三轮-90%.xlsx', '第三轮-95%.xlsx']
files1 = ['第四轮-80%.xlsx', '第四轮-90%.xlsx', '第四轮-95%.xlsx']
files2 = ['6-30-80%.xlsx', '6-30-90%.xlsx', '6-30-95%.xlsx', '7-3-80%.xlsx', '7-3-90%.xlsx', '7-3-95%.xlsx']
files3 = ['706-80%.xlsx', '706-90%.xlsx', '706-95%.xlsx', '710-80%.xlsx', '710-90%.xlsx', '710-95%.xlsx',
          '712-70%.xlsx', '712-80%.xlsx', '712-90%.xlsx', '712-95%.xlsx']
files4 = ['721-70%.xlsx', '721-80%.xlsx', '721-90%.xlsx', '721-95%.xlsx', '724-70%.xlsx', '724-80%.xlsx',
          '724-90%.xlsx', '724-95%.xlsx', '727-70%.xlsx', '727-80%.xlsx', '727-90%.xlsx', '727-95%.xlsx',
          '730-70%.xlsx', '730-80%.xlsx', '730-90%.xlsx', '730-95%.xlsx', '802-70%.xlsx', '802-80%.xlsx',
          '802-90%.xlsx', '802-95%.xlsx']
files5 = ['804-70%.xlsx', '807-70%.xlsx', '807-80%.xlsx',
          '807-90%.xlsx', '807-95%.xlsx', '810-70%.xlsx', '810-80%.xlsx', '810-90%.xlsx', '810-95%.xlsx',
          '813-70%.xlsx', '813-80%.xlsx', '813-90%.xlsx', '813-95%.xlsx', '816-70%.xlsx', '816-80%.xlsx',
          '816-90%.xlsx', '816-95%.xlsx', '819-70%.xlsx', '819-80%.xlsx', '819-90%.xlsx', '819-95%.xlsx',
          '822-70%.xlsx', '822-80%.xlsx', '822-90%.xlsx', '822-95%.xlsx', '824-70%.xlsx', '824-80%.xlsx',
          '824-90%.xlsx', '824-95%.xlsx']

# get_latency(input2, output)
calculate_result(files5)