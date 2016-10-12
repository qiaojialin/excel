import xlrd
import xlwt


def clean_excel():
    data = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\dataset.xlsx")

    table = data.sheet_by_name("loan")

    row_num = table.nrows
    col_num = table.ncols
    result = genMatrix(row_num, col_num)

    for r in range(row_num):
        if r == 0:
            result[0] = table.row_values(0)
            continue
        for c in range(col_num):
            cell_value = table.row(r)[c].value

            if c == 0:
                result[r][c] = cell_value

            if c == 1:
                result[r][c] = cell_value

            if c == 2:
                result[r][c] = cell_value

            if c == 3:
                result[r][c] = cell_value

            # 处理duration列
            if c == 4:
                a = int(cell_value)
                if a < 0:
                    a = -a
                elif a % 12 != 0:
                    amont = table.row(r)[c-1].value
                    time = table.row(r)[c+1].value
                    a = int(amont) / int(time)
                result[r][c] = a

            if c == 5:
                result[r][c] = cell_value

            if c == 6:
                result[r][c] = cell_value

            if c == 7:
                result[r][c] = cell_value

    write_data(result, "loan")


def write_data(data, name):
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
    path = r"C:\Users\Administrator\Desktop\\" + name + ".xls" # 默认路径
    file.save(path)
    return True


def genMatrix(rows,cols):
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    return matrix


if __name__ == '__main__':
    clean_excel()
