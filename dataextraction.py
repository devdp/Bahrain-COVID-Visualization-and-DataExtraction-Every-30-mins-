import re
import pandas as pd
import string

print('in data extraction')

def ext():
    df=pd.read_csv('data.csv')

    case_nos,ages,nationalitys,sexs,contact_tracing_numbers=[],[],[],[],[]
    for i,text in enumerate(df['text']):
        text=text.lower()
        print(text)
        try:
            case_no=re.findall('\d+',(re.search('(case|ase) no.*?\s*\d+',text).group(0)))[0].capitalize()
            case_nos.append(case_no)
        except:
            case_nos.append(None)
        try:
            age=re.findall('\d+',(re.search('age.*?\s*\d+',text).group(0)))[0].capitalize()
            ages.append(age)
        except:
            ages.append(None)
        try:
            nationality=re.search('nationality.*?\s*\w+',text).group().split()[1].capitalize()
            nationalitys.append(nationality)
        except:
            nationalitys.append(None)
        try:
            sex=re.search('sex.*?\s*\w+',text).group().split()[1].capitalize()
            sexs.append(sex)
        except:
            sexs.append(None)
        try:
            contact_tracing_number=re.split('-?contact tracing:?',text)[1].strip().strip('-').replace('\n',' ')
            #print('Extracted is---',contact_tracing_number)
            contact_tracing_numbers.append(contact_tracing_number)
    
        except:
            contact_tracing_numbers.append(None)


    extracted_df=pd.DataFrame({'case_no':case_nos,
                                'age':ages,
                                'nationality':nationalitys,
                                'sex':sexs,
                                'contact_tracing':contact_tracing_numbers  
                              })

    extracted_df.to_csv('datawoarea.csv')
print('over')