import xlwt
import re
import time

def write_excel(data, name):
    """写入数据,data为符合条件的数据列表，name表示指定的哪三个列，以此命名"""
    file = xlwt.Workbook()
    table = file.add_sheet(name, cell_overwrite_ok=True)
    l = 0  # 表示行
    for line in data:
        c = 0  # 表示一行下的列数
        for col in line:
            table.write(l, c, line[c])
            c += 1
        l += 1
    path = r"C:\Users\Administrator\Desktop\clean\\" + name + ".xls" # 默认路径
    file.save(path)
    return True


def gen_matrix(rows, cols):
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    return matrix


def is_number(str):
    pattern = re.compile(r"^[0-9]*$")
    match = pattern.match(str)
    if match:
        return True
    else:
        return False

def is_birth(str):
    pattern = re.compile(r"^\d{6}")
    match = pattern.match(str)
    if match:
        return True
    else:
        return False

def is_date(str):
    pattern = re.compile(r"^\d{4}/\d{1,2}/\d{1,2} \d:\d{2}")
    match = pattern.match(str)
    if match:
        return True
    else:
        return False


def read_csv(path):
    import re

    datas = list(list())
    for line in open(path):
        splits = line.split(',')
        data = list()
        for split in splits:
            split = re.sub(r'\n', '', split)
            data.append(split)
        datas.append(data)
    return datas


def write_csv(items, path):
    import csv
    with open(path, 'w', newline='') as data:
        writer = csv.writer(data)
        for item in items:
            writer.writerow(item)


def is_valid_date(str):
  try:
    time.strptime(str, "%Y-%m-%d")
    return True
  except:
    return False