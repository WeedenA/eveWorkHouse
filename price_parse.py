'''
Parses pasted new price data and saves new log entry.
'''
from price_handler import PriceData
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from sql_server import create_sqlalch_engine, execute_alch_query



def scrape(record):
    url = "https://pgsus.space/buyback/bteam-buyback/"
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html.parser')
    soup.prettify()

    tables = soup.find_all('table')
    for x in range(3):
        rows = tables[x].find_all('tr')
        for row in rows:
            row = row.get_text().split()
            if row[2] == 'of':
                ore_name = row[0]
                row[8] = re.sub('[,.]', '', row[8])
                ore_price = int(re.sub('[K]', '00', row[8]))
                record[ore_name] = ore_price


# If the last entry was today, don't make another
# Else add new record to db
def insert_new_price_record(df, today):
    last_entry_date = df['date'].iloc[-1]
    if last_entry_date == pd.Timestamp(today['date']):
        print("Already ran today")
        print(f"Here's your new dict anyways: {today}")
    else:
        cols = ', '.join("`" + str(x).replace('/', '_') + "`" for x in today.keys())
        vals = ', '.join("'" + str(x).replace('/', '_') + "'" for x in today.values())
        query = f"INSERT INTO ore_price_record ({cols}) VALUES ({vals})"
        engine = create_sqlalch_engine()
        execute_alch_query(engine, query)
        print("New log entry recorded if query successful")


def run():
    handler = PriceData()
    scrape(handler.dict)
    insert_new_price_record(handler.df, handler.dict)



if __name__ == '__main__':
    run()



