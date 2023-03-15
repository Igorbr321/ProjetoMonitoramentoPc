import pandas as pd

def importToExcel():
    cvsDataframe = pd.read_csv('./csv/hardwareInformation.csv')
    resultExcelFile = pd.ExcelWriter('./excel/hardwareInformation.xlsx')
    cvsDataframe.to_excel(resultExcelFile, index=False)
    resultExcelFile.save()
