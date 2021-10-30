'''
Playground, random stuff
'''

import sql_server
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

'''
Web-Scraping
'''
url = "https://pgsus.space/buyback/bteam-buyback/"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
soup.prettify()



tables = soup.find_all('table')
rows = tables[1].find_all('tr')

for row in rows:

    row = row.get_text().split()
    print(row)
    if row[2] == 'of':
        ore_name = row[0]
        row[8] = re.sub('[,.]', '', row[8])
        ore_price = int(re.sub('[K]', '00', row[8]))
        print(f"{ore_name}, price: {ore_price}")


