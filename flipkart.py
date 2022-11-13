import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2F4io&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=clp_metro_expandable_1_apple-categ-94e9d_iPhone_apple-products-store_90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite_wp1&fm=neo/merchandising&iid=M_aa732c04-041f-4fc9-a115-975905fbcdea_1.90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite&ppt=CLP&ppn=CLP:apple-products-store/"

page = requests.get(url)


soup = BeautifulSoup(page.content,'html.parser')


models = [mod.text for mod in soup.find_all("div", attrs={'class': '_3wU53n'})]
prices = [pri.text.strip('\u20b9') for pri in soup.find_all("div", attrs={'class': '_1vC4OE _2rQ-NK'})]
ratings =[rat.text.strip('\u2605') for rat in soup.find_all("div", attrs={'class': 'hGSR34 _2beYZw'})]

# print(len(prices))
# print(len(models))
# print(len(ratings)

data = pd.DataFrame({
	'model':models,
	'price':prices,
	'rating':ratings,
	})

data.to_csv('appleproducts.csv')