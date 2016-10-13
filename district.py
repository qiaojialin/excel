import xlrd
import utils

def clean_excel():
    data = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\dataset.xlsx")
    name = "district"

    table = data.sheet_by_name(name)

    row_num = table.nrows
    col_num = table.ncols
    result = utils.gen_matrix(row_num, col_num)

    id = set()

    for r in range(row_num):
        if r == 0:
            result[0] = table.row_values(0)
            continue
        for c in range(col_num):
            cell_value = table.row(r)[c].value
            if type(cell_value) == float:
                cell_value = str(round(cell_value))

            #处理district_id列
            if c == 0:
                if cell_value in id:
                    print("错误数据：", r, c, cell_value)
                id.add(cell_value)
                # result[r][c] = cell_value
            # else:
            #     result[r][c] = cell_value

    # write_data(result, name)



if __name__ == '__main__':
    clean_excel()
