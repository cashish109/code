from bs4 import BeautifulSoup
import requests
import re
import lxml
import csv


website = "https://order.wingstop.com/"
fieldnames = ['location name', 'street', 'city', 'state', 'zip','phone']

html = requests.get("https://order.wingstop.com/locations")
soup = BeautifulSoup(html.text, 'lxml')

lists = soup.findAll('a')
urls = list()

for url in lists:
	if(re.search('locations/',url['href'])):
		urls.append(website + url['href'])

with open('wingstop 2.csv', 'w', newline='') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for link in urls:
		response = requests.get(link)
		source = BeautifulSoup(response.text, 'lxml')
		locations = source.findAll('li',class_='vcard')

		for location in locations:
			if location.a is not None:
				html = requests.get(location.a['href'])
				locData = BeautifulSoup(html.text, 'lxml')
			else:
				print(location)

			name = locData.h1.text.strip()
			street = locData.find('span', class_='street-address').text.strip()
			locality = locData.find('span',class_='locality').text.strip()
			region = locData.find('span',class_='region').text.strip()
			postal_code = locData.find('span', class_='postal-code').text.strip()	
			telephon = locData.find('span', class_='tel').text.strip()

			writer.writerow({'location name':name, 'street':street, 'city':locality, 'state':region, 'zip':postal_code,'phone':telephon})
