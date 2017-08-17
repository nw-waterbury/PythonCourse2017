from bs4 import BeautifulSoup
import urllib2
import random
import time
import os
import re
import csv
from django.utils.encoding import smart_str, smart_unicode
from urlparse import *


address = 'https://petitions.whitehouse.gov/petitions'

def func_headers(website):
	"""Takes a URL and returns a list of petition headers, issues, and support numbers """
	headers = []
	Tag_Lists = []
	issue = []
	signatures = []
	for i in range(4):
		web_page = urljoin(str(website), '?page=%d' % i)
		web_text = urllib2.urlopen(web_page)
		head_soup = BeautifulSoup(web_text.read())
		headers.extend(head_soup.find_all('h3'))
		sigs = head_soup.find_all('span', {'class': 'signatures-number'})
		for sig in sigs:
			signatures.append(str(sig.get_text()))
		tag_list = head_soup.find_all('div', {'class': "field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"})
		for item in tag_list:
			Tag_Lists.append(item.find_all('h6'))
		for List in Tag_Lists:
			tags = []
			for tag in List:
				tags.append(str(tag.get_text()))
			issue.append(tags)
	issue = issue[-74:]
	return headers, issue, signatures

def func_titles(petitions):
	"""Takes a list of petitions and returns a list of specific URLs and titles """
	urls = []
	titles = []
	for petition in petitions:
		try:
			extension = petition.a['href']
		except:
			pass
		else:
			titles.append(smart_str(petition.a.get_text()))
			urls.append(urljoin("https://petitions.whitehouse.gov", str(extension)))
	return urls, titles

def pet_dates(urls):
	"""Takes in URL list of petitions and returns list of dates of submission """
	dates = []
	for link in urls:
		web_text = urllib2.urlopen(link)
		date_soup = BeautifulSoup(web_text.read())
		attrib = date_soup.find_all('h4', {'class': 'petition-attribution'})
		text_att = str(attrib[0].get_text())
		words = text_att.split()
		dates.append(' '.join(words[-3:]))
	return dates

def scrape_petitions(website):
	"""Takes a URL and returns petiton title, dates, issue tag, and support numbers """
	#Uses 3 functions detailed above
	headers, issue, sigs = func_headers(website)
	urls, titles = func_titles(headers)
	dates = pet_dates(urls)
	return titles, dates, issue, sigs

def write_csv(website):
		"""Creates a csv file for petitions and characteristics"""
		with open('hw2_nw.csv', 'wb') as f:
			writer = csv.DictWriter(f, fieldnames = ("PetitionTitle", "UploadDate", "IssueTags", "Signatures"))
			writer.writeheader()
			titles, dates, issue, sigs = scrape_petitions(website)
			#Written row by row
			for i in range(len(titles)):
				writer.writerow({'PetitionTitle':titles[i], 'UploadDate': dates[i], 'IssueTags': issue[i], 'Signatures': sigs[i]})

write_csv(address)
