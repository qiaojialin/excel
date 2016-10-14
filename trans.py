import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\trans.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\trans.csv")

    account_data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\account.csv")
    size = len(account_data)
    account_id = set()
    for r in range(size):
        if r == 0:
            continue
        account_id.add(account_data[r][0])

    row_num = len(data)

    result = list(list())

    type = {"VYDAJ", "PRIJEM"}
    operation = {"VYBER KARTOU", "VKLAD", "PREVOD Z UCTU", "VYBER", "PREVOD NA UCET"}
    k_symbol = {"SIPO", "POJISTNE", "SLUZBY", "UVER", "UROK", "SANKC.UROK", "DUCHOD", "", " "}

    id = set()

    for r in range(row_num):
        if r == 0:
            #去掉最后一个account字段
            line = list(data[0])
            line.pop()
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
        if not utils.is_full_date(v2):
            print("错误date：", r, 2, v2)
            continue

        v3 = data[r][3]
        if v3 not in type:
            print("错误type：", r, 3, v3)
            continue

        v4 = data[r][4]
        if v4 not in operation:
            print("错误operation：", r, 4, v4)
            continue

        v5 = data[r][5]
        if not utils.is_number(v5):
            print("错误amount：", r, 5, v5)
            continue

        #balance
        v6 = data[r][6]
        try:
            int(v6)
        except:
            print("错误balance：", r, 6, v6)
            continue

        v7 = data[r][7]
        if v7 not in k_symbol:
            print("错误k_symbol：", r, 7, v7)
            continue

        v8 = data[r][8]
        if not utils.is_bank(v8):
            print("错误bank：", r, 8, v8)
            continue

        line = [v0, v1, v2, v3, v4, v5, v6, v7, v8]
        result.append(line)

    utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\trans.csv")
    # utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\test.csv")

if __name__ == '__main__':
    clean_csv()