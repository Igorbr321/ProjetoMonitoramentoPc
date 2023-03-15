import csv
import datetime


def writeCsv(
    dataDesktop, 
    dataMotherboard, 
    dataGpuUsagePercentage,
    dataCpuModel,
    dataCpuUsagePercentage
    ):
    with open('./csv/hardwareInformation.csv', 'w', newline='') as csvfile:
        fieldnames = [
            'DESKTOP', 
            'Motherboard', 
            'GPU Usage Percentage', 
            'CPU Model', 
            'CPU Usage Percentage', 
            'PERSISTED_AT'
            ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        date = datetime.datetime.now()
        date_string = date.strftime("%Y %m %d %H %M:%S")
        date_datetime = datetime.datetime.strptime(date_string, "%Y %m %d %H %M:%S")

        writer.writeheader()
        writer.writerow(
            {
                'DESKTOP': dataDesktop,
                'Motherboard': dataMotherboard,
                'GPU Usage Percentage': dataGpuUsagePercentage, 
                'CPU Model': dataCpuModel, 
                'CPU Usage Percentage': dataCpuUsagePercentage,
                'PERSISTED_AT': date_datetime,
            }
        )