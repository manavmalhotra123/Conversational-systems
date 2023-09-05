# from scrapping 
from bs4 import BeautifulSoup
# reuqest to use the website access
import requests
# for csv file conversion 
import pandas as pd 


# url = ""
# request = requests.get(url, headers)
# request.text   ( for whole of the html code )

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.h1.text)

    
