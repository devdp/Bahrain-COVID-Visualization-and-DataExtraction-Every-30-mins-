import pandas as pd
import numpy as np

print('in data transformation')

def trans():
    df = pd.read_csv('datawoarea.csv', index_col=0)
    df['contacts'] = np.nan
    df['count'] = np.nan
    res=[]
    for i in range(len(df)):
        text = df['contact_tracing'][i]
        text = str(text)
        if text.find('(')>0:
            text = text.replace("(",' ')
            text = text.replace(")",' ')
        if text.find(',')>0:
            text = text.replace(",",' ')
        try:
            text = [int(j) for j in text.split() if j.isdigit()]
            touch = len(text)
            df['count'][i] = touch
            text = str(text)
            if text.find('[')==0:
                text = text.replace('[','')
                text = text.replace(']','')
                print(text)
                df['contacts'][i] = text
        except:
            pass

    df['contact_tracing']=df['contact_tracing'].str.lower()

    df['Area'] = np.nan
    df['Lat'] = np.nan
    df['Long'] = np.nan
    df['Contact Tracing'] = np.nan

    ar = ['aleker','salmabad','hidd','hoora','al_seef','sitra','Ras Zuwayed Area','random','alhassy','malkiya','nuwaidrat','naim']
    ar = [element.lower() for element in ar] ; ar

    aleker = df[df['contact_tracing'].str.contains("aleker", na=False)]
    aleker['Area'] = 'aleker'
    print('1')
    salmabad = df[df['contact_tracing'].str.contains("salmabad", na=False)]
    salmabad['Area'] = 'salmabad'
    print('2')
    hidd = df[df['contact_tracing'].str.contains("hidd", na=False)]
    hidd['Area'] = 'hidd'
    print('3')
    hoora = df[df['contact_tracing'].str.contains("hoora", na=False)]
    hoora['Area'] = 'hoora'
    print('4')
    al_seef = df[df['contact_tracing'].str.contains("al seef|seef", na=False)]
    al_seef['Area'] = 'Al Seef'
    print('5')
    sitra = df[df['contact_tracing'].str.contains("sitra", na=False)]
    sitra['Area'] = 'sitra'
    print('6')
    ras_zuwayed_area = df[df['contact_tracing'].str.contains("ras zuwayed area|zuwayed", na=False)]
    ras_zuwayed_area['Area'] = 'ras zuwayed area'
    print('7')
    random = df[df['contact_tracing'].str.contains("random", na=False)]
    random['Area'] = 'random'
    print('8')
    alhassy = df[df['contact_tracing'].str.contains("alhassy|hassy", na=False)]
    alhassy['Area'] = 'alhassy'
    print('9')
    malkiya = df[df['contact_tracing'].str.contains("malkiya", na=False)]
    malkiya['Area'] = 'malkiya'
    print('10')
    nuwaidrat = df[df['contact_tracing'].str.contains("nuwaidrat", na=False)]
    nuwaidrat['Area'] = 'nuwaidrat'
    print('11')
    naim = df[df['contact_tracing'].str.contains("naim", na=False)]
    naim['Area'] = 'naim'
    print('12')
    print('---------total length-----------',len(aleker)+len(salmabad)+len(hidd)+len(hoora)+len(al_seef)+len(sitra)+len(ras_zuwayed_area)+len(random)+len(alhassy)+len(malkiya)+len(nuwaidrat)+len(naim))

    dfwithar = pd.DataFrame()
    dfwithar = pd.concat([aleker,salmabad,hidd,hoora,al_seef,sitra,ras_zuwayed_area,random,alhassy,malkiya,nuwaidrat,naim])
    dfwithar = dfwithar.reset_index()

    for i in range(len(df)):
        print("i -> ",i)
        for j in range(len(dfwithar)):
            print("j -> ",j)
            if df['case_no'][i] == dfwithar['case_no'][j]:
                df['Area'][i] = dfwithar['Area'][j]

    df['Area'] = df['Area'].str.lower()

    for i in range(len(df)):
        if df['Area'][i] == 'al seef':
            df['Lat'][i] = 26.2405608
            df['Long'][i] = 50.5286395
        elif df['Area'][i] == 'aleker':
            df['Lat'][i] = 26.143136
            df['Long'][i] = 50.5957497
        elif df['Area'][i] == 'alhassy':
            df['Lat'][i] = 26.2032358
            df['Long'][i] = 50.5905324
        elif df['Area'][i] == 'hidd':
            df['Lat'][i] = 26.2209113
            df['Long'][i] = 50.6395521
        elif df['Area'][i] == 'malkiya':
            df['Lat'][i] = 26.1002035
            df['Long'][i] = 50.4687664
        elif df['Area'][i] == 'naim':
            df['Lat'][i] = 26.2283972
            df['Long'][i] = 50.5624685
        elif df['Area'][i] == 'nuwaidrat':
            df['Lat'][i] = 26.1336858
            df['Long'][i] = 50.5826695
        elif df['Area'][i] == 'ras zuwayed area':
            df['Lat'][i] = 26.0856218
            df['Long'][i] = 50.6063942
        elif df['Area'][i] == 'salmabad':
            df['Lat'][i] = 26.185534
            df['Long'][i] = 50.504279
        elif df['Area'][i] == 'sitra':
            df['Lat'][i] = 26.1478346
            df['Long'][i] = 50.5996587
        else:
            print(df['Area'][i])

    df.to_csv('last.csv')
    return None
print('over')