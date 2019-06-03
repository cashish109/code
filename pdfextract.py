import PyPDF2 as pdf
import pandas
import sys

pdfObject = open(sys.argv[1],'rb')

pdfReader = pdf.PdfFileReader(pdfObject)
pages = pdfReader.numPages
reviews = []
pageIndex = 0

while pageIndex < pages:

	page = pdfReader.getPage(pageIndex)
	if(len(reviews) != 0): 
		reviews.extend(page.extractText().split('NPS:'))
	else:
		reviews = page.extractText().split('NPS:')
	pageIndex += 1
#final = string.replace(re.findall(r"([0-9]{4}\-[0-9]{2}\-[0-9]{2})",string)[0],'')
#print(reviews)
my_df = pandas.DataFrame(reviews)
my_df.to_csv('pdfreviews 2.csv', index=False, header=False)