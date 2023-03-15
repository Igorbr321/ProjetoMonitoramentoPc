import writeCsv
import alterCsv
import importCsvToExcel
import os.path
import hardwareInformation as info
import tkinter

def showInfos():
    text = f'''
    Desktop: {info.getDesktop()}
    Motherboard Model: {info.getMotherboardModel()}
    GPU Usage Percentage: {info.getGpuUsagePercentage()}
    CPU Model: {info.getCpuModel()}
    CPU Usage Percentage: {info.getCpuUsagePercentage()}    
    '''
    
    infoHardwareText["text"] = text 

    persistOnCsvFile()


def persistOnCsvFile():

    path = './csv/hardwareInformation.csv'

    check_file = os.path.isfile(path)

    if (check_file == False): 
        writeCsv.writeCsv(
            info.getDesktop(), 
            info.getMotherboardModel(), 
            info.getGpuUsagePercentage(),
            info.getCpuModel(),
            info.getCpuUsagePercentage()
        )
    else:
        alterCsv.alterCsv(
            info.getDesktop(), 
            info.getMotherboardModel(), 
            info.getGpuUsagePercentage(),
            info.getCpuModel(),
            info.getCpuUsagePercentage()
        )

window = tkinter.Tk()
window.title("Hardware Informations!")

orientationText = tkinter.Label(window, text="Clique no botão para ver suas informações de hardware")
orientationText.grid(column=0, row=0, padx= 400, pady=10)

buttonGetInfosHardware = tkinter.Button(window, text="Mostrar informações de hardware!", command=showInfos)
buttonGetInfosHardware.grid(column=0, row=1, pady=10)

infoHardwareText = tkinter.Label(window, text="")
infoHardwareText.grid(column=0, row=2, pady=80)

buttonGetInfosHardware = tkinter.Button(window, text="Importar informações para o Excel", command=importCsvToExcel.importToExcel)
buttonGetInfosHardware.grid(column=0, row=3, pady=40)

window.mainloop()


