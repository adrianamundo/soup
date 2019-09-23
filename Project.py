#!/usr/bin/env python3
from bs4 import BeautifulSoup, CData
import requests,sys,csv,json

#lista de url's a usar
url1="http://ufm.edu/Portal"
url2 = "http://ufm.edu/Estudios"
#url3
#url4

print ("<Adriana Mundo>")

class Minisoup:
    def portal(self):
        print("===================================================")
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url1).text
except:
    print(f"unable to get {url1}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

print("1.Portal")
#print(soup.title)
#print(soup.title.string)

title = soup.title.string

print("GET the title and print it: <",title, ">")
print("-------------------------------------------------------------------------------------------------------")

#GET the complete Address of UFM
for datos in soup.find_all("meta", {"property":"og:url"}):
    address = datos.get("content")
print("GET the Complete Adress of UFM <", address,">")
print("-------------------------------------------------------------------------------------------------------")

#GET the phone number and info mail
for datos in soup.find_all("a", {"href":"tel:+50223387700"}):
    tel = datos.text

for datos in soup.find_all("a",{"href":"mailto:inf@ufm.edu"}):
    mail = datos.text

print ("GET the phone number <",tel,"> and info mail<",mail,">")
print("-------------------------------------------------------------------------------------------------------")

#GET all item that are part of the upper nav menu (id:menu-table)
print("GET all item that are part of the upper nav menu (id:menu-table): ")
table = soup.find("table", { "id" : "menu-table" })
for datos in table.findAll("tr"):
 for datos in table.findAll("div",{"class":"menu-key"}):
      cells = datos.get_text("data-menu")
      print("<",cells,">")

print("-------------------------------------------------------------------------------------------------------")

#find all properties that have href (link to somewhere)
print("find all properties that have href (link to somewhere):")
for datos in soup.find_all('a', limit =3):
    links = datos.get('href')
    print("- <",links,">")
print("-------------------------------------------------------------------------------------------------------")

#GET href of "UFMail" button
for datos in soup.find_all("a",{"id":"ufmail_"}):
    button = datos.get('href')
    #print(button)
    print("GET href of UFMail button <",button,">")
print("-------------------------------------------------------------------------------------------------------")

#GET href "MiU" button
for datos in soup.find_all("a",{"id":"miu_"}):
    button2 = datos.get('href')
    #print(button2)
    print("GET href MiU button <",button2,">")
print("-------------------------------------------------------------------------------------------------------")

#get hrefs of all &lt;img>
print("get hrefs of all &lt;img>:")
for datos in soup.find_all('a'):
    if datos.img:
        print("<",datos.img['src'],">")

print("-------------------------------------------------------------------------------------------------------")

#count all &lt;a>
print("count all &lt;a:")
a=0
for datos in soup.find_all('a'):
    #if datos.img:
        a += 1
        print("-",a)
print("-------------------------------------------------------------------------------------------------------")

print("=======================================================================================================")
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
print("count all &lt;a:")
d=0
for datos in soup.find_all('a'):
        d += 1
        print("-",d)
print("-------------------------------------------------------------------------------------------------------")
print("=======================================================================================================")
print("3.CS")

#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")