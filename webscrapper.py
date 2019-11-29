#from selenium import webdriver
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone+11+128+gb&crid=23DLRDR76GUBQ&sprefix=iphone%2Caps%2C301&ref=nb_sb_ss_i_3_6"
url_client = ureq(url)
page_html = url_client.read()
url_client.close()

page_soup = soup(page_html, 'html.parser')
containers = page_soup.findAll("div", {"class": "sg-col-inner"})
#container = containers[0]
print(containers)






