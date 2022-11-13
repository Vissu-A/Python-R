import requests,re
import bs4

url = 'https://www.amazon.in/dp/B06Y28BWKW/ref=dra_a_ms_r_ho_xx_P1400_1000?tag=dradisplayi0a-21&ascsubtag=b0699cd56105706ceb2c418b7427f493_S'
page = requests.get(url)
print(page)
print(page.status_code)
print(page.content)
print()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
print(soup.p)
print(soup.title)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.a)
print()
print(soup.prettify())
print('\n','\n')
print('-------------------------------------------------------------------------------')
links = soup.findAll('a')
print(links)
l = []
count = 0
for link in links:
	print(link.get('href'))
	l.append(link.get('href'))
for i in l:
    count += 1
   
print('count of href links in the page:',count)