import os
import xlrd
from utils.handle_path import testData_path
def get_excel_data(excelDir,sheet_name):
    workBook=xlrd.open_workbook(excelDir,formatting_info=True)
    workSheet=workBook.sheet_by_name(sheet_name)
    #获取一列数据 col_values(0))
    print(workSheet.col_values(0))
    #获取一行数据 row_values(0))
    #获取单元格数据-workSheet.cell(行编号,列编号)
    print(workSheet.cell(0,0).value)
    resList = []
    rowIndex = 0
    for one in workSheet.col_values(0):
        reqBody = workSheet.cell(rowIndex, 9).value  # 请求Body
        respData = workSheet.cell(rowIndex, 11).value  # 响应数据
        resList.append((reqBody, respData))  # [(请求1，响应1),(请求2，响应2)]
        rowIndex += 1  # 行编号 加1  下一行操作
    print(resList)
if __name__ == '__main__':
    fileDir = os.path.join(testData_path, 'Delivery_System_V1.5.xls')
    get_excel_data(fileDir, '登录模块')
