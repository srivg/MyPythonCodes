# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:29:15 2017

@author: srivathsan
"""

def GetSearchString():
        
    import pyodbc as sq       
    #DRIVER={ODBC Driver 13 for SQL Server}
    cnxn= sq.connect('DRIVER={SQL Server};SERVER=azsrfhwrsql01; Trusted_Connection=Yes; DATABASE=RIMS')
    cursor=cnxn.cursor()
    #cursor.execute("SELECT COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME LIKE N'vTestTracker' ") #add N to make it a string
    #heading=cursor.fetchall()
    #for ros in heading:
    #    print(ros)
    # Select Project Name
    cursor.execute("SELECT DISTINCT ProjectName from dbo.vOtherCTRTestResults")
    tables=cursor.fetchall()
    tables=list(tables)
    print('Project Names to choose from :')
    j=1
    for i in tables:
        print(str(j),'. ',i[0])
        j+=1
    ProjectNamesi = []
    print('Enter the number before the project names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:    
        name = input()
        if name == '':
            if len(ProjectNamesi)==0:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            ProjectNamesi = ProjectNamesi + [name]
        except:
            print('Enter only numbers')       
    ProjectNames='('    
    for i in ProjectNamesi:
        ProjectNames=ProjectNames+"N'"+list(tables[i-1])[0]+"', "
    ProjectNames= ' ProjectName in '+ProjectNames[:-2]+')'
        
    ############################################################################################
    
    cursor.execute("SELECT DISTINCT Build from dbo.vOtherCTRTestResults where"+ProjectNames)
    tables=cursor.fetchall()
    tables=list(tables)
    print('build Names to choose from :')
    j=1
    for i in tables:
        print(str(j),'. ',i[0])
        j+=1
    buildNamesi = []
    print('Enter the number before the build names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
    
        name = input()
        if name == '':
            if len(buildNamesi)==0:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            buildNamesi = buildNamesi + [name]
        except:
            print('Enter only numbers')
        
        
        
    buildNames='('    
    for i in buildNamesi:
        buildNames=buildNames+"N'"+list(tables[i-1])[0]+"', "
    buildNames=' and Build in '+ buildNames[:-2]+')'
        
      #############################################################################################
    
    
    cursor.execute("SELECT DISTINCT SubSystem from dbo.vOtherCTRTestResults where"+ProjectNames + buildNames)
    tables=cursor.fetchall()
    tables=list(tables)
    print('SubSystem Names to choose from :')
    j=1
    NullThereY=99999
    for i in tables:
        if list(i)[0]==None:
            i[0]='System'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    SubSystemNamesi = []
    print('Enter the number before the SubSystem names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(SubSystemNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                SubSystemNamesi = SubSystemNamesi + [name-1]
            else:
                if name==NullThereY:
                    SubSystemNamesi=SubSystemNamesi
                    NullThere=NullThereY
                else:
                    SubSystemNamesi = SubSystemNamesi + [name]
        except:
            print('Enter only numbers')    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(SubSystemNamesi)==0:
            SubSystemNames = " and (SubSystem is NULL)"
        else:
            SubSystemNames = " and (SubSystem is NULL or SubSystem in ("
            for i in SubSystemNamesi:
                SubSystemNames=SubSystemNames+"N'"+list(tables[i-1])[0]+"', "
            SubSystemNames=SubSystemNames[:-2]+'))'
    else:
        SubSystemNames='(' 
        for i in SubSystemNamesi:
            SubSystemNames=SubSystemNames+"N'"+list(tables[i-1])[0]+"', "
        SubSystemNames = ' and SubSystem in '+ SubSystemNames[:-2]+')'
        
        ##########################################################################################
    cursor.execute("SELECT DISTINCT Component from dbo.vOtherCTRTestResults where"+ProjectNames + buildNames + SubSystemNames)
    tables=cursor.fetchall()
    tables=list(tables)
    print('Component Names to choose from :')
    j=1
    NullThereY=99999
    for i in tables:
        if list(i)[0]==None:
            i[0]='System'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    ComponentNamesi = []
    print('Enter the number before the Component names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(ComponentNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                ComponentNamesi = ComponentNamesi + [name-1]
            else:
                if name==NullThereY:
                    ComponentNamesi=ComponentNamesi
                    NullThere=NullThereY
                else:
                    ComponentNamesi = ComponentNamesi + [name]
        except:
            print('Enter only numbers')    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(ComponentNamesi)==0:
            ComponentNames = " and (Component is NULL)"
        else:
            ComponentNames = " and (Component is NULL or Component in ("
            for i in ComponentNamesi:
                ComponentNames=ComponentNames+"N'"+list(tables[i-1])[0]+"', "
            ComponentNames=ComponentNames[:-2]+'))'
    else:
        ComponentNames='(' 
        for i in ComponentNamesi:
            ComponentNames=ComponentNames+"N'"+list(tables[i-1])[0]+"', "
        ComponentNames = ' and SubSystem in '+ ComponentNames[:-2]+')'
        
        
    #############################################################################################
     
    
       
    cursor.execute("SELECT DISTINCT Config from dbo.vOtherCTRTestResults where"+ProjectNames + buildNames + SubSystemNames + ComponentNames)
    tables=cursor.fetchall()
    tables=list(tables)
    
    
    print('Config to choose from :')
    j=1
    NullThereY=99999999
    for i in tables:
        if list(i)[0]==None:
            i[0]='No Data Provided'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    ConfigNamesi = []
    print('Enter the number before the Config names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(ConfigNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                ConfigNamesi = ConfigNamesi + [name-1]
            else:
                if name==NullThereY:
                    ConfigNamesi=ConfigNamesi
                    NullThere=NullThereY
                else:
                    ConfigNamesi = ConfigNamesi + [name]
        except:
            print('Enter only numbers')    
        
    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(ConfigNamesi)==0:
            ConfigNames = " and (Config is NULL)"
        else:
            ConfigNames = " and (Config is NULL or Config in ("
            for i in ConfigNamesi:
                ConfigNames=ConfigNames+"N'"+list(tables[i-1])[0]+"', "
            ConfigNames=ConfigNames[:-2]+'))'
    else:
        ConfigNames='(' 
        for i in ConfigNamesi:
            ConfigNames=ConfigNames+"N'"+list(tables[i-1])[0]+"', "
        ConfigNames = ' and Config in '+ ConfigNames[:-2]+')'
        
        ##########################################################################################
        
        
    cursor.execute("SELECT DISTINCT TestName from dbo.vOtherCTRTestResults where"+ProjectNames + buildNames + SubSystemNames  + ComponentNames + ConfigNames)
    tables=cursor.fetchall()
    tables=list(tables)
    
    
    print('TestName to choose from :')
    j=1
    NullThereY=99999999
    for i in tables:
        if list(i)[0]==None:
            i[0]='No Data Provided'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    TestNameNamesi = []
    print('Enter the number before the TestName names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(TestNameNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                TestNameNamesi = TestNameNamesi + [name-1]
            else:
                if name==NullThereY:
                    TestNameNamesi=TestNameNamesi
                    NullThere=NullThereY
                else:
                    TestNameNamesi = TestNameNamesi + [name]
        except:
            print('Enter only numbers')    
        
    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(TestNameNamesi)==0:
            TestNameNames = " and (TestName is NULL)"
        else:
            TestNameNames = " and (TestName is NULL or TestName in ("
            for i in TestNameNamesi:
                TestNameNames=TestNameNames+"N'"+list(tables[i-1])[0]+"', "
            TestNameNames=TestNameNames[:-2]+'))'
    else:
        TestNameNames='(' 
        for i in TestNameNamesi:
            TestNameNames=TestNameNames+"N'"+list(tables[i-1])[0]+"', "
        TestNameNames = ' and TestName in '+ TestNameNames[:-2]+')'
        
        ##########################################################################################
        
        
    cursor.execute("SELECT DISTINCT EvaluationName from dbo.vOtherCTRTestResults where"+\
                   ProjectNames + buildNames + SubSystemNames  + ComponentNames + ConfigNames + TestNameNames)
    tables=cursor.fetchall()
    tables=list(tables)
    
    
    print('EvaluationName to choose from :')
    j=1
    NullThereY=99999999
    for i in tables:
        if list(i)[0]==None:
            i[0]='No Data Provided'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    EvaluationNameNamesi = []
    print('Enter the number before the EvaluationName names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(EvaluationNameNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                EvaluationNameNamesi = EvaluationNameNamesi + [name-1]
            else:
                if name==NullThereY:
                    EvaluationNameNamesi=EvaluationNameNamesi
                    NullThere=NullThereY
                else:
                    EvaluationNameNamesi = EvaluationNameNamesi + [name]
        except:
            print('Enter only numbers')    
        
    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(EvaluationNameNamesi)==0:
            EvaluationNameNames = " and (EvaluationName is NULL)"
        else:
            EvaluationNameNames = " and (EvaluationName is NULL or EvaluationName in ("
            for i in EvaluationNameNamesi:
                EvaluationNameNames=EvaluationNameNames+"N'"+list(tables[i-1])[0]+"', "
            EvaluationNameNames=EvaluationNameNames[:-2]+'))'
    else:
        EvaluationNameNames='(' 
        for i in EvaluationNameNamesi:
            EvaluationNameNames=EvaluationNameNames+"N'"+list(tables[i-1])[0]+"', "
        EvaluationNameNames = ' and EvaluationName in '+ EvaluationNameNames[:-2]+')'
        
        ##########################################################################################
        
        
    cursor.execute("SELECT DISTINCT EvaluationVariation from dbo.vOtherCTRTestResults where"+\
                   ProjectNames + buildNames + SubSystemNames  + ComponentNames + ConfigNames + TestNameNames +\
                   EvaluationNameNames)
    tables=cursor.fetchall()
    tables=list(tables)
    
    
    print('EvaluationVariation to choose from :')
    j=1
    NullThereY=99999999
    for i in tables:
        if list(i)[0]==None:
            i[0]='No Data Provided'
            NullThereY=j
        print(str(j),'. ',i[0])
        j+=1
    
    NullThere=-1
    EvaluationVariationNamesi = []
    print('Enter the number before the EvaluationVariation names to be selected' +
          ' (Or enter nothing to stop.):')
    while True:
        name = input()
        if name == '':
            if len(EvaluationVariationNamesi)==0 and NullThere==-1:
                print('Make at least one selection')
            else:
                break
        try:
            name = int(name)
            if name > len(tables):
                print("Enter within range")
                continue
            if name>NullThereY:
                EvaluationVariationNamesi = EvaluationVariationNamesi + [name-1]
            else:
                if name==NullThereY:
                    EvaluationVariationNamesi=EvaluationVariationNamesi
                    NullThere=NullThereY
                else:
                    EvaluationVariationNamesi = EvaluationVariationNamesi + [name]
        except:
            print('Enter only numbers')    
        
    
    
    if NullThere!=-1:
        del tables[NullThereY-1]
        if len(EvaluationVariationNamesi)==0:
            EvaluationVariationNames = " and (EvaluationVariation is NULL)"
        else:
            EvaluationVariationNames = " and (EvaluationVariation is NULL or EvaluationVariation in ("
            for i in EvaluationVariationNamesi:
                EvaluationVariationNames=EvaluationVariationNames+"N'"+list(tables[i-1])[0]+"', "
            EvaluationVariationNames=EvaluationVariationNames[:-2]+'))'
    else:
        EvaluationVariationNames='(' 
        for i in EvaluationVariationNamesi:
            EvaluationVariationNames=EvaluationVariationNames+"N'"+list(tables[i-1])[0]+"', "
        EvaluationVariationNames = ' and EvaluationVariation in '+ EvaluationVariationNames[:-2]+')'
        
        ##########################################################################################
    
    SearchString=  ProjectNames + buildNames + SubSystemNames  + ComponentNames + ConfigNames + TestNameNames +\
                   EvaluationNameNames + EvaluationVariationNames
                   
                   
    return SearchString              