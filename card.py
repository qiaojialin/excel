import utils


def clean_csv():
    #读取要处理的csv
    data = utils.read_csv(r"C:\Users\Administrator\Desktop\数据仓库与数据挖掘第一次作业\数据仓库与数据挖掘第一次作业\dataset\card.csv")
    # data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\card.csv")

    disp_data = utils.read_csv(r"C:\Users\Administrator\Desktop\clean\disp.csv")
    size = len(disp_data)
    disp_id = set()
    for r in range(size):
        if r == 0:
            continue
        disp_id.add(disp_data[r][0])

    row_num = len(data)

    result = list(list())

    type = {"classic", "junior", "gold"}

    id = set()

    for r in range(row_num):
        if r == 0:
            line = ["card_id", "disp_id", "type", "issued"]
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
        if v1 not in disp_id:
            print("disp_id不存在：", r, 1, v1)
            continue

        v2 = data[r][2]
        if v2 not in type:
            print("错误type：", r, 2, v2)
            continue
        # if v2 == "golden":
        #     v2 = "gold"

        v3 = data[r][3]
        if not utils.is_date(v3):
            print("错误issued：", r, 3, v3)
            continue

        line = [v0, v1, v2, v3]
        result.append(line)

    utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\card.csv")
    # utils.write_csv(result, r"C:\Users\Administrator\Desktop\clean\test.csv")

if __name__ == '__main__':
    clean_csv()
