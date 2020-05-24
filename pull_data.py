from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from dataextraction import ext
from datatranformation import trans

def pull():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {"download.default_directory" : r"C:\Users\Bramhesh_Algo8\Documents\up_map_Sel_data\\"}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=options)
    df = pd.DataFrame(columns=['Case No','Age','Nationality','Area'])
    #fetch Active Cases and all
    driver.get("https://www.moh.gov.bh/Covid19")
    driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/div/a[6]').click()
    time.sleep(10)
    active_cases = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/table/thead/tr[2]/td/span').text
    stable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/table/thead/tr[4]/td[1]/span').text
    critical = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/table/thead/tr[4]/td[2]/span').text
    discharged = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/table/thead/tr[6]/td/span').text
    death = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/table/thead/tr[7]/td/span').text

    time.sleep(5)

    driver.get("https://www.moh.gov.bh/Covid19/ContactsTracing")
    #driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/div/a[6]').click()
    time.sleep(10)
    number_of_cases = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/table/tbody/tr[2]/td/p/strong').text
    res = [int(i) for i in number_of_cases.split() if i.isdigit()]

    df=pd.DataFrame(columns=['Text'])

    for i in range(int(res[0]+4)):
        k=''
        try:
            if(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td/p').text):
                elem = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td/p').text
            else:
                elem = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td').text
            a = {
                'text': elem
                }
            print(a)
            df=df.append(a,ignore_index=True)
        except:
            print(str(i))

    df.to_csv('data.csv')

    driver.get('https://github.com/owid/covid-19-data/tree/master/public/data')
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/main/div[2]/div/div[2]/table/tbody[2]/tr[10]/td[2]/span/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/main/div[2]/div/div[3]/div[1]/div[2]/div[1]/a[1]').click()
    time.sleep(10)
    ext()
    trans()

    return active_cases,stable,critical,discharged,death