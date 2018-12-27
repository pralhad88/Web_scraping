from bs4 import BeautifulSoup
import urllib.request

main_link = "https://www.ndtv.com/latest/page- "
count = 1
while True:
	main_link = main_link.replace(main_link[-1:],str(count))
	sauce = urllib.request.urlopen(main_link).read()
	soup = BeautifulSoup(sauce,'lxml')
	a=[]
	latest_news = soup.find('div',{'class':'new_storylising'})

	for list1 in latest_news.find_all("li"):
		ancher = list1.find('a')
		if ancher == None:
			continue
		link = ancher.get('href')
		#a.append(link)
		sauce = urllib.request.urlopen(link).read()
		soup = BeautifulSoup(sauce,'lxml')
		non_type_class = soup.find('span', {"itemprop":"dateModified"})
		if non_type_class == None:
			continue
		print("Headline:-",soup.h1.text)
		print("Date:-",soup.find('span', {"itemprop":"dateModified"}).text)
		print("Author:-",soup.find('span', {"itemprop":"author"}).text)
		for paragraph in soup.find_all('p'):
			if paragraph.text == "................................ Advertisement ................................":
				break
			print(paragraph.text)
		print(' ')
	if count == 8:
		break
	count+=1