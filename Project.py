#!/usr/bin/env python3
from bs4 import BeautifulSoup, CData
import requests,sys,csv,json

#lista de url's a usar
url1="http://ufm.edu/Portal"
#url2
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



#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")