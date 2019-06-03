from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import time


locations = requests.get("https://www.blazepizza.com/locations")
soupLocations = bs(locations.text, "html.parser")
locationList = soupLocations.find_all('a',{'class':'location-link'})
fieldnames = ['location name', 'address', 'phone', 'url']
urls = list()
for url in locationList:
	if(re.search('locations/',url['href'])):
		urls.append('https://www.blazepizza.com/'+url['href'])

with open('blazepizza 2.csv', 'w', newline='') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for loc in urls:
		
		locality = requests.get(loc)
		soupLocation = bs(locality.text, 'html.parser')

		locationTitle = soupLocation.find('div', {'id':'locationTitle'}).text.strip()
		locationAddress = soupLocation.find('div', {'id':'locationAddress'}).text.strip()
		locationPhone = soupLocation.find('div',{'id':'locationPhone'}).text.strip()
		locationEmail = soupLocation.find('div',{'id':'locationEmail'}).text.strip()

		time.sleep(5)

		print(locationTitle)
		print(locationAddress)
		print(locationPhone)
		print(locationEmail)

		writer.writerow({'location name':locationTitle, 'address':locationAddress, 'phone':locationPhone, 'url':loc})
