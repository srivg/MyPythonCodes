#__author__ = 'srivathsan'

import sys
import os
import pandas as pd


def printtest(s):
    a = s ** 3
    print("hello world")
    print("Hello world", a)
    pass


def checkfileexistance():
    """ Check if the file exists """
    if os.path.isfile(filename):
        print("\nCongratulations the file exists")
        buff=open(filename,'rt')
    else:
        print(filename)
        sys.exit('\nThe file doesnot exist please enter a valid filename')
    return buff

def createresultfile():
    if os.path.isfile(fileorign+"/output.xls"):
        print(os.remove(fileorign+"/output.xls"))
        buff=open(fileorign+"/output.xls",'at')
    else:
        buff=open(fileorign+"/output.xls",'at')

    return buff

##This is the end of function definition


#fileorign=input('Please enter the file location of the data     :')
fileorign="C:/Users/srivg/Documents/"
filename=fileorign+"/input1.txt"
r=checkfileexistance()

all=r.read()
allwords=all.split()

uniquewords=[]
uniquenum=[]

for wordi in allwords:
    if wordi in uniquewords:
        position=uniquewords.index(wordi)
        uniquenum[position]+=1
    else:
        uniquewords+=[wordi]
        uniquenum+=[1]

if len(uniquewords)==0:
    sys.exit("There is nothing in the file to count")
flag=0
i=0

df=pd.DataFrame([uniquenum, uniquewords],['Recurrence', 'Word'])
dft=df.transpose()
df=dft
del dft

writer = pd.ExcelWriter(fileorign+"/"+'WordCount.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()


"""




Use the following code to print in HTML

wfile=createresultfile()

htmlbodytableheadderer='<html>\n  <head>\n    <META http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <style>                      td, th {font:11px verdana; text-align:left; padding:2px;}            th {font-weight:bold; background-color:#ddd;}            #results {border-collapse:collapse;}                  </style>\n  </head>\n  <body>\n    <table id="results" border="1">\n      <thead>\n        <tr>\n'
tableheaddingfinisher='        </tr>\n      </thead>\n'
rowbodyheadder='      <tbody class="jr row">\n        <tr class="jrow">\n'
rowinitializer='          <td>'
columnbreak='</td>\n          <td>'
columnend='</td>\n'
rowender='        </tr>\n      </tbody>\n'
htmlbodytablefinisher='    </table>\n  </body>\n</html>\n'


tableheadding='          <th>'+'Word'+'</th>\n          <th>'+'Recurrence'+'</th>\n '


wfile.write(htmlbodytableheadderer)
wfile.write(tableheadding)
wfile.write(tableheaddingfinisher)

for i in range(len(uniquewords)):
    wfile.write(rowbodyheadder)
    rowdata=rowinitializer+uniquewords[i]+columnbreak+str(uniquenum[i])+columnend
    wfile.write(rowdata)
    wfile.write(rowender)


#
#htmlbodytableheadderer='<html>\n  <head>\n    <META http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <style>                      td, th {font:11px verdana; text-align:left; padding:2px;}            th {font-weight:bold; background-color:#ddd;}            #results {border-collapse:collapse;}                  </style>\n  </head>\n  <body>\n    <table id="results" border="1">\n      <thead>\n        <tr>\n'
#tableheaddingfinisher='        </tr>\n      </thead>\n'
#rowbodyheadder='      <tbody class="jr row">\n        <tr class="jrow">\n'
#rowinitializer='          <td>'
#columnbreak='</td>\n          <td>'
#columnend='</td>\n'
#rowender='        </tr>\n      </tbody>\n'
#htmlbodytablefinisher='    </table>\n  </body>\n</html>\n'
#

"""

#sys.modules[__name__].__dict__.clear()

