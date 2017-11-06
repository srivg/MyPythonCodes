
import pyodbc as sq
import os
import pandas as pd
from RIMSDatapull import GetSearchString
import datetime
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

input("Welcome to RIMS Report\nPress any key to start")
print('The program default path is c:\RIMSreport')
print('')
print('')

print('Do you want to select your search criteria or would you like to choose from a file')
print('1. Select from file')
print('2. Choose through the selection')

InCall='Select ProjectName, Build, SubSystem, Component, Config, UnitSerialNumber, TestName, EvaluationName, EvaluationVariation, MeasurementValue, UnitofMeasurement, MeasurementTime, ActualReadout, PlannedReadout, UnitofDuration from dbo.vOtherCTRTestResults where ' 

path="C:\\RIMSReport\\FilePaths"

os.chdir("C:\\")
if not os.path.isdir('RIMSReport'):
    os.makedirs(path)

os.chdir("C:\\RIMSReport")
if not os.path.isdir('FilePaths'):
    os.makedirs("FilePaths")
    


Choice=input()
if Choice =='2':
    GetStringg=GetSearchString()
    Choice='2'
else:    
    if Choice =='':
        if os.path.isfile(path+"\\Default.txt"):
            filepath=path+"\\Default.txt"
            GetStringg=open(filepath).read()
        else:

            Choice='1'
    else:
        Choice='1'
        listoffiles=os.listdir(path)
        if len(listoffiles)==0:
            print("No preSaved query. Please create a new query")
            GetStringg=GetSearchString()
            Choice='2'
        else:
            print('Here are the files to choose from. Please make a selection')
            j=1
            for i in listoffiles:
                print(str(j),'. ',i)
                j+=1
            while True:
                name = input()
                if name == '':
                    print('Make at least one selection')
                else:
                    try:
                        intnae=int(name)
                    except:
                        print('Enter only numbers')
                        continue                      
                            
                    if int(name)<=len(listoffiles):
                        filepath=path+"\\"+listoffiles[int(name)-1]
                        GetStringg=open(filepath).read()
                        break
                    else:
                        print('Enter within range')
            
if Choice=='2':
    print('would you like to save the filepath')
    print('1. Save the file as Default')
    print('2. Do not save the file')
    print('3. Save this as a new query')
    Choice=input()
    if Choice =='1':
        open(path+"\\Default.txt",'w').write(GetStringg)
    if Choice == '3':
        Choice = input('name')
        open(path+"\\"+Choice+".txt",'w').write(GetStringg)
       


SearchString= InCall+ GetStringg
   
print('Fetching file please wait')
#DRIVER={ODBC Driver 13 for SQL Server}
cnxn= sq.connect('DRIVER={SQL Server};SERVER=azsrfhwrsql01; Trusted_Connection=Yes; DATABASE=RIMS')
cursor=cnxn.cursor()
cursor.execute(SearchString)
tables=cursor.fetchall()
tables=list(tables)
Columnnames=['ProjectName', 'Build', 'SubSystem', 'Component', 'Config', 'UnitSerialNumber', 'TestName', 'EvaluationName', 'EvaluationVariation', 'MeasurementValue', 'UnitofMeasurement', 'MeasurementTime', 'ActualReadout', 'PlannedReadout', 'UnitofDuration']
df=pd.DataFrame.from_records(tables, columns=Columnnames)

#        #dfg=df[(df['UnitSerialNumber']=='0001') & (df['TestName']=='HINGE-LIFE')]
#
#        #dfg[['ActualReadout', 'MeasurementValue']]

df.ActualReadout=pd.to_numeric(df['ActualReadout'], errors='coerce')
df.MeasurementValue=pd.to_numeric(df['MeasurementValue'], errors='coerce')
print('File Fetched')
print("Have you closed the \n1. RIMS-report.xls\n2. RIMsreport.pdf")
input()

writer = pd.ExcelWriter('RIMS-report.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()


with PdfPages('RIMSReport.pdf') as pdf:    
    for ProjectN in df.ProjectName.unique():
        for BuildN in df.Build.unique():
            for SubSystemN in df.SubSystem.unique():
                for ComponentN in df.Component.unique():
                    for ConfigN in df.Config.unique():
                        for TestNameN in df.TestName.unique():
                            for EvaluationNameN in df.EvaluationName.unique():
                                for EvaluationVariationN in df.EvaluationVariation.unique():
                                    if SubSystemN is None:
                                        if ComponentN is None:
                                            adf=df[ (df['ProjectName']==ProjectN) & (df['Build']==BuildN) & (df['Config']==ConfigN) & (df['TestName']==TestNameN) & (df['EvaluationName']==EvaluationNameN) & (df['EvaluationVariation']==EvaluationVariationN) ]
                                            titlele=ProjectN+' | '+BuildN+' | System | Component| '+ConfigN+' | \n'+TestNameN +' | '+ EvaluationNameN + ' | ' + EvaluationVariationN
                                        else:                                        
                                            adf=df[ (df['ProjectName']==ProjectN) & (df['Build']==BuildN) & (df['Component']==ComponentN) & (df['Config']==ConfigN) & (df['TestName']==TestNameN) & (df['EvaluationName']==EvaluationNameN) & (df['EvaluationVariation']==EvaluationVariationN) ]
                                            titlele=ProjectN+' | '+BuildN+' | System | '+ComponentN+' | '+ConfigN+' | \n'+TestNameN +' | '+ EvaluationNameN + ' | ' + EvaluationVariationN
                                    else:
                                        if ComponentN is None:
                                            adf=df[ (df['ProjectName']==ProjectN) & (df['Build']==BuildN) & (df['Config']==ConfigN) & (df['TestName']==TestNameN) & (df['EvaluationName']==EvaluationNameN) & (df['EvaluationVariation']==EvaluationVariationN) ]
                                            titlele=ProjectN+' | '+BuildN+' | System | Component| '+ConfigN+' | \n'+TestNameN +' | '+ EvaluationNameN + ' | ' + EvaluationVariationN
                                        else:                                            
                                            adf=df[ (df['ProjectName']==ProjectN) & (df['Build']==BuildN) & (df['SubSystem']==SubSystemN) & (df['Component']==ComponentN) & (df['Config']==ConfigN) & (df['TestName']==TestNameN) & (df['EvaluationName']==EvaluationNameN) & (df['EvaluationVariation']==EvaluationVariationN) ]
                                            titlele=ProjectN+' | '+BuildN+' | '+SubSystemN+' | '+ComponentN+' | '+ConfigN+' | \n'+TestNameN +' | '+ EvaluationNameN + ' | ' + EvaluationVariationN
                                    if len(adf)!=0:
                                        plt.figure()
                                        for UnitSerialNumberN in adf.UnitSerialNumber.unique():
                                            agdf=adf[ (adf['UnitSerialNumber']==UnitSerialNumberN) ]
                                            agdf=agdf.sort_values('ActualReadout')
                                            X=list(agdf.ActualReadout)
                                            Y=list(agdf.MeasurementValue)
                                            plt.plot(X,Y, label=UnitSerialNumberN)
                                            plt.ylabel(list(agdf['EvaluationName'])[0] + ' [' +  list(agdf['UnitofMeasurement'])[0] + ']')
                                            plt.xlabel( '# [' +  list(agdf['UnitofDuration'])[0] + ']')
                                        plt.title(titlele)
                                        plt.legend()
                                        pdf.savefig()
                                        plt.close()
                                        
    d = pdf.infodict()
    d['Title'] = 'RIMS MUltipage Report'
    d['Author'] = u'Srivathsan, Watson'
    d['Subject'] = 'Data downloaded from RIMS'
    d['Keywords'] = 'PdfPages'
    d['CreationDate'] = datetime.datetime(2009, 11, 13)
    d['ModDate'] = datetime.datetime.today()       
print("RIMSReport can be found in \n C:\RIMSReport\RIMSReport.pdf " )
print("The raw data for RIMSReport can be found in \n  C:\RIMSReport\RIMS-report.xlsx")        
print("\n\n Press any key to exit")
input()            
                                   
                                
                            
                                    
                                
                                
                            
                
            
        
#        

        

