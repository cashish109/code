from bs4 import BeautifulSoup
import requests
import csv


website = "https://www.ubreakifix.com/"
fieldnames = ['location name', 'address','phone']

html = requests.get(website+"locations")
soup = BeautifulSoup(html.text,"html.parser")

locationUrls = soup.findAll('a',{'class':'gtm-store-btn rounded'})

with open('ubreakifix.csv', 'w', newline='') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for url in locationUrls:
		location = website+url.get('href')
		locationSource = requests.get(location)
		locationData = BeautifulSoup(locationSource.text, 'html.parser')
		location_name = re.sub(' +',' ', locationData.find('h1',{'class':'text-black h2'}).text.strip('\n'))
		address = locationData.find('div',{'class':'address'}).text.strip()
		if(locationData.find('a',{'class':'phone hidden-xs gtm-call-btn'}) is None):
			phone = '999999999'
		else:
			phone = locationData.find('a',{'class':'phone hidden-xs gtm-call-btn'}).text.strip()
			
		print(location_name,"---",address,"---",phone)
		writer.writerow({'location name':location_name, 'address':address, 'phone':phone})