from bs4 import BeautifulSoup, CData
import requests,sys,csv,json,os, urllib.request, re
import json


url2 = "http://ufm.edu/Estudios"
def estudios(Minisoup):
    print("2.Estudios")

#now navigate to  /Estudios (better if you obtain href from the DOM)
try:
    html_content = requests.get(url2).text
except:
    print(f"unable to get {url2}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")

#display all items from "topmenu" (8 in total)
print("Display all items from topmenu:")
b = 0
tabla = soup.find("div", { "id" : "topmenu" })
for datos in tabla.findAll("li"):
# for datos in tabla.findAll("a",{"class":"external text"}):
      celda = datos.text
      b += 1
      print(b,"<",celda,">")
print("-------------------------------------------------------------------------------------------------------")

#display ALL "Estudios" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)
print("Display all Estudios:")
tablas1 = soup.find("div",{"id":"mw-content-text"})
for datos in tablas1.findAll("div",{"class":"estudios"}):
        celdas = datos.text
        print("-",celdas)
print("-------------------------------------------------------------------------------------------------------")

#display from "leftbar" all &lt;li> items (4 in total)
print("Display from leftbar all &lt;li> items:")
c=0
tablas2 = soup.find("div",{"class":"leftbar"})
for datos in tablas2.findAll("li"):
#for datos in tablas2.findAll("a",{"class":"external text"}):
        celdas2 = datos.text
        c += 1
        #print(celdas2)   
        print(c,"<",celdas2,">")
print("-------------------------------------------------------------------------------------------------------")

#get and display all available social media with its links (href) "class=social pull-right"
print("Get and display all available social media with its links (href) class =social pull -right:")
tablas3 = soup.find("div",{"class":"social pull-right"})
for datos in tablas3.findAll('a'):
        celdas3 = datos.get('href')
        print("-<",celdas3,">")
print("-------------------------------------------------------------------------------------------------------")

#count all &lt;a> (just display the count)
d=0
for datos in soup.find_all('a'):
        d += 1
print("count all &lt;a: <",d,">")
print("-------------------------------------------------------------------------------------------------------")
print("=======================================================================================================")