Author="__ABHISHEK MISHRA__"
print(Author)
output_form="PLEASE NOTE THAT OUTPUT IS IN FORM OF\n hex-code, \n rgb-ratio, \n hsl-ratio, \n hsv-ratio, \n color-name, \n cmyk-ratio, \n XYZ-value, \n svg-url, \n base-value \n"
print(output_form)
import extcolors
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import webbrowser
import requests
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
colors, pixel_count = extcolors.extract_from_path("medium.jpg")
a=""
for i in colors:
    for j in range(3):
        #a+hex(list(i[0])[j])
        if(list(i[0])[j] in range(0,16)):
           a=a+"0"+hex(list(i[0])[j])[2:4]
        else:
           a=a+hex(list(i[0])[j])[2:4]
    #print(a)
    url=(f"https://www.thecolorapi.com/id?hex={a}&format=html")
    driver.get(url)
    time.sleep(3)
    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    for a in soup.findAll('table',attrs={'pure-table'}):
        s=a.find('td')
        print(s.text)
    print("\n")
    a=""
