Author="__ABHISHEK MISHRA__"
print(Author)
output_form="PLEASE NOTE THAT OUTPUT IS IN FORM OF\n hex-code, \n rgb-ratio, \n hsl-ratio, \n hsv-ratio, \n color-name, \n cmyk-ratio, \n XYZ-value, \n svg-url, \n base-value \n"
print(output_form)
import extcolors #pip install extcolor
from selenium import webdriver #pip install selenium
from bs4 import BeautifulSoup #pip install bs4
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
colors, pixel_count = extcolors.extract_from_path("medium.jpg")#image path
akm=""
for i in colors:
    for j in range(3):
        #a+hex(list(i[0])[j])
        if(list(i[0])[j] in range(0,16)):
           akm=akm+"0"+hex(list(i[0])[j])[2:4]
        else:
           akm=akm+hex(list(i[0])[j])[2:4]
    #print(a)
    url=(f"https://www.thecolorapi.com/id?hex={akm}&format=html")#thecolorapi.com 
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')#web scrapping
    for a in soup.findAll('table',attrs={'pure-table'}):
        s=a.find('td')
        print(s.text)
    print("\n")
    akm=""
