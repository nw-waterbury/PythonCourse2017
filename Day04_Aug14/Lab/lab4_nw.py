from bs4 import BeautifulSoup
import urllib2
import csv
import random
import time
import os
import re

web_address='http://polisci.wustl.edu/faculty/specialization'
web_page= urllib2.urlopen(web_address)
soup=BeautifulSoup(web_page)
info=soup.find_all('div', {'class': 'views-row'})
names=[]
titles=[]
specializations=[]
emails=[]
websites=[]

#Names & Titles
for i in range(len(info)):
    name=(str(info[i].get_text().split('\n')[1]))
    names.append(str(info[i].get_text().split('\n')[1]))
    titles.append(str(info[i].get_text().split('\n')[2]))


#Specializations
specs_info=soup.find_all('h3')
for sub in specs_info:
    for sibling in sub.next_siblings:
            if sibling in specs_info:
    			break
            else:
                try:
                        sibling.get_text()
                        specializations.append(sub)
                except:
                        pass

#Intermediate Links
href=[]
for x in soup.find_all('a',{'class':"person-view-primary-field" }):
    href.append(str(x['href']))
    new_link= []
    for x in href:
	       new_link.append('http://polisci.wustl.edu%s' % x)
new_link[16]="http://polisci.wustl.edu/Matthew_Gabel"
new_link[32]="http://polisci.wustl.edu/Matthew_Gabel"

#Emails
for link in new_link:
    web_add=link
    new_web_page= urllib2.urlopen(web_add)
    new_soup=BeautifulSoup(new_web_page.read())
    soup.prettify()
    if '@' in new_soup.find_all('a', href=True)[16].text:
        emails.append(new_soup.find_all('a', href=True)[16].text)
    elif '@' in new_soup.find_all('a', href=True)[15].text:
        emails.append(new_soup.find_all('a', href=True)[15].text)
    elif '@' in new_soup.find_all('a', href=True)[17].text:
        emails.append(new_soup.find_all('a', href=True)[17].text)
    else:
        emails.append("No Email Found")

#Websites
for link in new_link:
    web_add=link
    new_web_page= urllib2.urlopen(web_add)
    new_soup=BeautifulSoup(new_web_page.read())
    prof_personalpage= 'NA'
    div = new_soup.find('div', {'class' : 'field field-name-field-person-website field-type-link-field field-label-inline clearfix'})
    if div:
        prof_personalpage = div.find('a')['href']


#mydict={}
#for i in range(lens(names_list))



#profs=open('profs.csv', wb )
#my_writer= csv.writer(profs)
#my_writer=csv.DictWriter(profs, fieldnames=("Name")
#for i in range(lens(names_list)):
#    my_writer.writerow({"Name":individ_name})
