import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\client.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\client.csv")

    row_num = len(data)

    result = list(list())

    id = set()

    for r in range(row_num):
        if r == 0:
            line = ["client_id", "birth_number", "district_id", "age", "gender"]
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
        if not utils.is_birth(v1):
            print("错误birth_number：", r, 1, v1)
            continue
        year = int(v1[0:2])
        month = int(v1[2:4])
        day = int(v1[4:6])

        # 女
        if month > 12:
            month -= 50
            gender = "female"
        else:
            gender = "male"

        birthday = "19" + str(year) + "-" + str(month) + "-" + str(day)

        if not utils.is_valid_date(birthday):
            print("错误birth_number：", r, 1, v1)
            continue
        age = str(100 - year)

        v2 = data[r][2]
        if not utils.is_number(v2):
            print("错误district_id：", r, 2, v2)
            continue
        if int(v2) < 1 or int(v2) > 77:
            print("外键不存在：", r, 2, v2)
            continue

        line = [v0, v1, v2, age, gender]
        result.append(line)

    utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\client.csv")
    # utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\test.csv")

if __name__ == '__main__':
    clean_csv()
