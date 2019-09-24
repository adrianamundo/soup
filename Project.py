#!/usr/bin/env python3
from bs4 import BeautifulSoup, CData
import requests,sys,csv,json,os, urllib.request, re
import json

#lista de url's a usar
url1="http://ufm.edu/Portal"
url2 = "http://ufm.edu/Estudios"
url3 = "https://fce.ufm.edu/carrera/cs/"
url4 = "https://www.ufm.edu/Directorio"

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
#if len(soup.find_all('a')) < 31:
for datos in soup.find_all('a'):
    links = datos.get('href')
    print("- <",links,">")
#else:
   # filename = "logs/href.txt"
 #   with open(filename,"w+") as f:
  #      for datos in soup.find_all('a'):
#            json.dump(datos,f)
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
def estudios(self):
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
print("3.CS")
try:
    html_content = requests.get(url3).text
except:
    print(f"unable to get {url3}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")

#GET title
titulo = soup.title.string
print("GET title <",titulo,">")
print("-------------------------------------------------------------------------------------------------------")

#GET and display the href
for datos in soup.find_all("meta", {"property":"og:url"}):
    hrefaddress = datos.get("content")
print("GET and display the href <", hrefaddress,">")
print("-------------------------------------------------------------------------------------------------------")

#Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically)
print("Download the FACULTAD DE CIENCIAS ECONÓMICAS logo.:")
logo = soup.find("div",{"class":"fl-photo-content fl-photo-img-png"})
for datos in logo.findAll('img'):
    logophoto = datos.get('src')
    urllib.request.urlretrieve(logophoto, os.path.basename(logophoto))
    print("<",logophoto,">")
print("-------------------------------------------------------------------------------------------------------")

#GET following &lt;meta>: "title", "description" ("og")
print("GET the following &lt;meta>:")
for datos in soup.find_all("meta", {"property":"og:title"}):
    tituloog = datos.get("content")
    print("- title <",tituloog,">")

for datos in soup.find_all("meta", {"property":"og:description"}):
    descriptionog = datos.get("content")
    print("- description <",descriptionog,">")
print("-------------------------------------------------------------------------------------------------------")

#count all &lt;a> (just display the count)
e = 0
for datos in soup.find_all('a'):
    e += 1
print("count all &lt;a: <",e,">")
print("-------------------------------------------------------------------------------------------------------")

#count all &lt;div> (just display the count)
f = 0
for datos in soup.find_all('div'):
    f += 1
print("count all &lt;div: <",f,">")
print("-------------------------------------------------------------------------------------------------------")

print("=======================================================================================================")
print("4.Directorio")
try:
    html_content = requests.get(url4).text
except:
    print(f"unable to get {url4}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")

#Sort all emails alphabetically (`href="mailto:arquitectura@ufm.edu"`) in a list, dump it to logs/4directorio_emails.txt
tabladirectorio = soup.find_all("a",{"href":re.compile('@ufm.edu')})
tabladirectorio_text = []
for datos in tabladirectorio:
    #emails = datos.get('href')
    tabladirectorio_text.append(datos.text)

email_list= list(dict.fromkeys(sorted(tabladirectorio_text)))

filename= "Miniproyecto/soup/logs/4directorio_emails.json"
with open(filename, "w+") as writer:
    for datos in email_list:
        #json.dump(datos, writer)
        writer.write('-'+datos+'\n')
print("Sort all emails alphabetically in a list and dump it to /logs/4directorio_emails.txt:",filename)
print("-------------------------------------------------------------------------------------------------------")

#Count all emails that start with a vowel. (just display the count)
vocal = 0
for datos in email_list:
    if datos[0] in ["a", "e", "i", "o","u"]:
        vocal +=1
print("Count all emails that start with a vowel <",vocal,">")
print("-------------------------------------------------------------------------------------------------------")

#Group in a JSON all rows that have `Same Address` (dont use Room number) as address, dump it to logs/4directorio_address.json
tabladireccion = soup.find("table",{"class":"tabla ancho100"})
tabladireccion2 = soup.find_all("table",{"class":"tabla ancho100"})[1]

direccion = {}
oficinas = []
pagina = []
ambos1 = []

for datos in tabladireccion2.findAll("tr"):
        daton = datos.find_all("td")

        for datos in daton:
             if len(daton) == 4:
                 oficinas =[]
                 pagina = []
                 a = daton[4].get_text().strip().split(',')[0]
                 b=daton[1].get_text.strip()
                 oficinas.append(a)
                 pagina.append(b)
                 ambos1.append(oficinas,pagina)

ambos = dict(zip(oficinas,pagina))

#for datos in tabladireccion2.findAll("tr"):
 #   daton2 = datos.find_all("td")
  #  if len(daton2) == 4:
   #     c = daton2[4].get_text().strip.split(',')[0]
     #   d=daton2[0].get_text().strip()
    #    oficinas.append(d)
      #  pagina.append(c)
#ambos = oficinas + pagina
#ambos = dict(zip(oficinas, pagina))


with open("Miniproyecto/soup/logs/4directorio_address.json","w+") as writer2:
    #for datos in direccion:
    json.dump(direccion, writer2)
         #writer2.write(json_string)
         #writer2.close()
print("-------------------------------------------------------------------------------------------------------")

#Try to correlate in a JSON Faculty Dean and Directors, and dump it to `logs/4directorio_deans.json`
tabladean = soup.find_all("table",{"class":"tabla ancho100 col3"})[1]
facultad = []
for datos in tabladean.findAll("td"):
    i = 0
    datosdean = datos.text
    facultad1 = ' '
    nombre = ' '
    correo = ' '

   
    facultad.append(datos.text)

facultad_lista= list(dict.fromkeys(sorted(facultad)))

with open("Miniproyecto/soup/logs/4directorio_deans.json","w+") as writer3:
    for datos in facultad_lista:
        writer3.write('-'+datos+'\n')

#GET the directory of all 3 column table and generate a CSV with these columns (Entity,FullName, Email), and dump it to `logs/4directorio_3column_tables.csv`



            







#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")