import pandas
import re
import sys
import datetime

#setup sets up the display for the inforamtion
def setup():
    pandas.set_option('display.max_rows',500)
    pandas.set_option('display.max_columns',10)
    pandas.set_option('display.width',150)

#applies the filter you need and returns the indexes in the df
def applyFilter(name,val):
    if col_types[name]==str:
        inp_string = (col_names[name] + '==' + "\'" + val + "\'")
        dfd = df.query(inp_string)
    elif col_types[name]==bool:    
        inp_bool = (col_names[name] + '==' + val)
        dfd = df.query(inp_bool)
    indexx = dfd.index
    return indexx

#appMain is the main menu of the app
def appMain():
    for index, value in enumerate(options):
        print(index, value)
    val = int(input("Select Option:"))
    if val == 1:
        print(df)
    elif val == 2:#This calls the apply filter function and passes the name and val
        #here the code displays the titles of the rows so you now the filters you can apply
        print("Names of rows:")
        for index, value in enumerate(col_names):
            print(index, value)
        #prompts the user with the name and values to filter
        name = int(input("Select Name:"))
        val = input("Enter val: ")
        printIndex(applyFilter(name,val))
    elif val == 3:
        #Select the index of the Tree you want to check Duration
        indexx = input("Enter index: ")
        indexx = convertList(indexx)
        print(duration(indexx))
    elif val == 0:
        return
    appMain()   

#duration calculates the difference between starts and end times from the information csv
def duration(indexx):
    #its important to make sure that the values are voids
    dfd = []
    durationLi = []
    durationTime = datetime.timedelta()

    #here the code loops through the indexx and finds the Start and End time
    for i in range (0, len(indexx)):
        dfd.append([df.loc[indexx[i],'Start Time'],df.loc[indexx[i],'End Time']])
        #This is the old code ↓↓↓↓↓  it uses the csv from forest without modifying it, I found it was more practical to remove the time zone manually.
        #dfd.append([datetime.datetime.strptime(df.loc[indexx[i],'Start Time'].replace(' GMT-03:00',''),'%c'),datetime.datetime.strptime(df.loc[indexx[i],'End Time'].replace(' GMT-03:00',''),'%c')])
    #here the code loops and calculates the duration of each element in the list ( start - end time)
    for i in range (0,len(dfd)):
        durationLi.append(dfd[i][1]-dfd[i][0])

    #here the code sums the duration of all the elements in the list
    for i in range (0,len(durationLi)):
        durationTime += durationLi[i]

    return(durationTime) 

#convert to list creates a list from the input string to a list of int that can be used as indexes
def convertList(string):
    li = []
    #Convrts the input string to a list of int to use as an index
    if string.isnumeric():
        li.append(int(string))
        return li
    elif ',' in string:
        aux = (list(string.split(',')))
        for i in range (0,len(aux)):
            li.append(int(aux[i]))
    elif '-' in string:
        for i in range(int(string.split('-')[0]),int(string.split('-')[1])):
            li.append(i)
    else:
        print('Wrong argument')

    li = list(map(int, li))
    return li   

#uses the indexes to print the dataframe
def printIndex(indexx):
    for i in range (0,len(indexx)):
        print('____________________________________________________________')
        print(df.iloc[indexx[i],:])
   

col_types = [datetime,datetime,str,str,str,bool]
col_names = ['Start Time','End Time','Tag','Note','Tree Type','Success']
options = ['Exit','Print Everything','Filter','Duration']
df = pandas.read_csv('Forest - Copy.csv',names=col_names,skiprows=[0],usecols=[0,1,2,5])
df['Start Time'] = pandas.to_datetime(df['Start Time'],format='%c')
df['End Time'] = pandas.to_datetime(df['End Time'],format='%c')
setup()

appMain()

raise SystemExit