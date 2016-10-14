import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\loan.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\loan.csv")

    account_data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\account.csv")
    size = len(account_data)
    account_id = set()
    for r in range(size):
        if r == 0:
            continue
        account_id.add(account_data[r][0])

    row_num = len(data)

    status = {"A", "B", "C", "D"}
    result = list(list())

    id = set()

    for r in range(row_num):
        if r == 0:
            result.append(data[0])
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
        if not utils.is_date(v2):
            print("错误date：", r, 2, v2)
            continue

        v3 = data[r][3]
        if not utils.is_number(v3):
            print("错误amount：", r, 3, v3)
            continue

        v4 = data[r][4]
        if not utils.is_number(v4):
            if v4 == "-60":
                v4 = "60"
            else:
                print("错误duration：", r, 4, v4)
                continue
        if int(v4) % 12 != 0:
            if v4 == "22":
                v4 = "24"
            else:
                print("错误duration：", r, 4, v4)
                continue

        v5 = data[r][5]
        if not utils.is_number(v5):
            print("错误payments：", r, 5, v5)
            continue

        v6 = data[r][6]
        if v6 not in status:
            print("错误status：", r, 6, v6)
            continue

        #payduration
        v7 = data[r][7]
        if not utils.is_number(v7):
            print("错误payduration：", r, 7, v7)
            continue

        if int(v7) >= int(v4):
            print("错误payduration >= payments：", data[r][7], ">=", data[r][4])
            continue

        if int(v5) * int(v4) != int(v3):
            print("错误duration * payments != amount", data[r][4], "*", data[r][5], "!=", data[r][3])
            continue

        line = [v0, v1, v2, v3, v4, v5, v6, v7]
        result.append(line)

    utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\loan.csv")
    # utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\test.csv")

if __name__ == '__main__':
    clean_csv()