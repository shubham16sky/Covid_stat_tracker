#A basic utility to show the current covid related stats of bengaluru city


import requests
import bs4
import plyer
import time
import threading

def html_data(url):
    data=requests.get(url)
    return data

def bengaluru_corona_cases():
    url="https://apps.bbmpgov.in/Covid19/en/index.php"
    data=html_data(url)
    bs=bs4.BeautifulSoup(data.text,'html.parser')
    info=bs.find_all("p",class_="stat_no")
    totalCase=info[0].getText()
    totalActiveCase=info[1].getText()
    totaRecoveries=info[2].getText()
    totalDeath=info[3].getText()
    details=""
    details=details+ "Total Number of cases : "+totalCase+"\n"+"Total Active Cases :"+totalActiveCase+"\n"+"Total Recoveries : "+totaRecoveries+"\n"+"Total Deaths : "+totalDeath+"\n"

    # print(totalCase)
    # print(totalActiveCase)
    # print(totaRecoveries)
    # print(totalDeath)
    #print(details)
    return details
#print(bengaluru_corona_cases())

def notification():
    while True:
        plyer.notification.notify(
            title="BENGALURU COVID STATS\n-------------------------------------",
            message=bengaluru_corona_cases(),
            timeout=30

        )

        time.sleep(5)


thread1=threading.Thread(target=notification())
thread1.start()

















