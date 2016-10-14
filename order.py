import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\order.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\order.csv")

    account_data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\account.csv")
    size = len(account_data)
    account_id = set()
    for r in range(size):
        if r == 0:
            continue
        account_id.add(account_data[r][0])

    row_num = len(data)

    result = list(list())

    k_symbol = {"SIPO", "POJISTNE", "LEASING", "UVER", " "}

    id = set()

    for r in range(row_num):
        if r == 0:
            line = ["order_id", "account_id", "bank_to", "account_to", "amount", "k_symbol"]
            result.append(line)
            continue

        v0 = data[r][0]
        if not utils.is_number(v0):
            print("错误id：", r, 0, v0)
            continue
        if str == "":
            print("空的id：", r, 0, v0)
            continue
        if v0 in id:
            print("重复id：", r, 0, v0)
            continue
        id.add(v0)

        v1 = data[r][1]
        if v1 not in account_id:
            print("account_id不存在：", r, 1, v1)
            continue

        v2 = data[r][2]
        if not utils.is_bank(v2):
            print("错误bank_to：", r, 2, v2)
            continue

        v3 = data[r][3]
        if not utils.is_number(v3):
            print("错误account_to：", r, 3, v3)
            continue

        v4 = data[r][4]
        if not utils.is_number(v4):
            print("错误amount：", r, 4, v4)
            continue

        v5 = data[r][5]
        if v5 not in k_symbol:
            print("错误k_symbol：", r, 5, v5)
            continue
        if v5 == " ":
            v5 = ""

        line = [v0, v1, v2, v3, v4, v5]
        result.append(line)

    utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\order.csv")
    # utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\test.csv")

if __name__ == '__main__':
    clean_csv()