import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\account.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\account.csv")

    #获取外键列
    ex_data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\district.csv")
    size = len(ex_data)
    external_key = set()
    for r in range(size):
        if r == 0:
            continue
        external_key.add(ex_data[r][0])

    frequency = {"POPLATEK MESICNE", "POPLATEK TYDNE", "POPLATEK PO OBRATU"}

    row_num = len(data)
    col_num = len(data[0])
    result = utils.gen_matrix(row_num, col_num)

    id = set()

    for r in range(row_num):
        if r == 0:
            result[0] = data[0]
            continue
        for c in range(col_num):
            cell_value = data[r][c]

            # 处理account_id列
            if c == 0:
                if not utils.is_number(cell_value):
                    print("错误id：", r, c, cell_value)
                    continue
                if str == "":
                    print("空的id：", r, c, cell_value)
                    continue
                if cell_value in id:
                    print("重复id：", r, c, cell_value)
                id.add(cell_value)
                #     result[r][c] = cell_value
                # else:
                #     result[r][c] = cell_value
            if c == 1:
                if cell_value not in external_key:
                    print("外键不存在：", r, c, cell_value)
            if c == 2:
                if cell_value not in frequency:
                    print("错误frequency：", r, c, cell_value)
            if c == 3:
                if not utils.is_date(cell_value):
                    print("错误date：", r, c, cell_value)


if __name__ == '__main__':
    clean_csv()


