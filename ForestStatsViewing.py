import pandas
import re
import sys
import datetime


def setup():
    pandas.set_option('display.max_rows',500)
    pandas.set_option('display.max_columns',10)
    pandas.set_option('display.width',150)  #setup sets up the display for the inforamtion

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
    print(dfd)  #applyFilter applies the fiter you want and displays the information

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
    appMain()   #appMain is the main menu of the app

def duration():
    #Select the index of the Tree you want to check Duration
    indexx = input("Enter index: ")
    indexx = convertList(indexx)
    #its important to make sure that the values are voids
    dfd = []
    durationLi = []
    durationTime = datetime.timedelta()

    #here the code loops through the indexx and finds the Start and End time
    for i in range (0, len(indexx)):
        dfd.append([datetime.datetime.strptime(df.loc[indexx[i],'Start Time'].replace(' GMT-03:00',''),'%c'),datetime.datetime.strptime(df.loc[indexx[i],'End Time'].replace(' GMT-03:00',''),'%c')])
    
    #here the code loops and calculates the duration of each element in the list ( start - end time)
    for i in range (0,len(dfd)):
        durationLi.append(dfd[i][1]-dfd[i][0])

    #here the code sums the duration of all the elements in the list
    for i in range (0,len(durationLi)):
        durationTime += durationLi[i]

    print(durationTime) #duration calculates the difference between starts and end times from the information csv

def convertList(string):
    #Convrts the input string to a list of int to use as an index
    li = list(string.split(","))
    li = list(map(int, li))
    return li   #convert to list creates a list from the input string to a list of int that can be used as indexes



setup()
#ts = ['DiaDeLaSemana','Mes','DiaNumerico','Horario','ZonaHoraria','Año']
col_types = [str,str,str,str,str,bool]
col_names = ['Start Time','End Time','Tag','Note','Tree Type','Success']
options = ['Exit','Print Everything','Filter','Duration']
df = pandas.read_csv('Forest.csv',names=col_names,skiprows=[0],usecols=[0,1,2,5])

appMain()
raise SystemExit