import pandas
import sys
import re
from datetime import datetime
def setup():
    pandas.set_option('display.max_rows',500)
    pandas.set_option('display.max_columns',10)
    pandas.set_option('display.width',150)
def applyFilter():
    print("Names of rows:")
    for index, value in enumerate(col_names):
        print(index, value)
    name = int(input("Select Name:"))
    val = input("Enter val: ")
    if col_types[name]==str:
        inp_string = (col_names[name] + '==' + "\'" + val + "\'")
        dfd = df.query(inp_string)
    elif col_types[name]==bool:    
        inp_bool = (col_names[name] + '==' + val)
        dfd = df.query(inp_bool)
    print(dfd)
def appMain():
    for index, value in enumerate(options):
        print(index, value)
    val = int(input("Select Option:"))
    if val == 1:
        print(df)
    elif val == 2:
        applyFilter()
    elif val == 3:
        duration()
    elif val == 4:
        changeSettings()
    elif val == 0:
        return
    appMain()
def duration():
    #Select the index of the Tree you want to check Duration
    indexx = int(input("Enter index: "))
    #here the code gets the Start Time and End Time from     
    dfd = [df.loc[indexx,'Start Time'],df.loc[indexx,'End Time']]
    #dfd new is the timelist in string format
    dfd_new = [dfd[0].replace(' GMT-03:00','')]
    dfd_new.append(dfd[1].replace(' GMT-03:00',''))
    #time list has the time in datetime format
    time_list = [datetime.strptime(dfd_new[0],'%c')]
    time_list.append(datetime.strptime(dfd_new[1],'%c'))
    #calculates the duration with the time list
    duration = time_list[1]-time_list[0]
    print(duration)
#def dataframesetup():
    #for row in df:
        #datetime.strotime(df.loc[index,'Start Time'].replace(' GMT-03:00'), '%c')
setup()

#ts = ['DiaDeLaSemana','Mes','DiaNumerico','Horario','ZonaHoraria','Año']
col_types = [str,str,str,str,str,bool]
col_names = ['Start Time','End Time','Tag','Note','Tree Type','Success']
options = ['Exit','Print Everything','Filter','Duration']
df = pandas.read_csv('Forest.csv',names=col_names,skiprows=[0],usecols=[0,1,2,5])

appMain()
raise SystemExit