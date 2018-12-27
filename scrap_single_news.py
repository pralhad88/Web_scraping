from bs4 import BeautifulSoup
import urllib.request

article = []
data_storage = {}
source = urllib.request.urlopen("https://www.ndtv.com/india-news/pm-modi-in-telangana-says-seek-your-support-blessings-for-bjp-in-coming-polls-1953954").read()
soup = BeautifulSoup(source,'lxml')

data_storage['Title'] = soup.h1.string
data_storage["PublishDate"] = (soup.find('span', {"itemprop":"dateModified"}).string)
data_storage["Publisher/Author"] = (soup.find('span', {"itemprop":"author"}).string)

for paragraph in soup.find_all('p'):
	if "Advertisement" in paragraph.text:
		break
	article.append(paragraph.text)
	
connector = ' '*(len(data_storage["Publisher/Author"])-1)
for i in article[1:]:
	connector = connector + i + ' '

data_storage['Article'] = connector

for data in data_storage.values():
	print(data)
