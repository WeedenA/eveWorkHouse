'''
Parses pasted new price data and saves new log entry.
todo: clean-up, pickle has been scrubbed
'''
from price_handler import PriceData
import pandas as pd
from sql_server import create_sqlalch_engine, execute_alch_query

PRICE_LOG = 'zPRICE_LOG.txt'


# Open pasted prices
def newPrices():
    file = open('zpaste_ore_prices.txt')
    price_lines = file.readlines()
    file.close()
    mapping = list(map(str.strip, price_lines))
    return mapping


# Clean new values, populate into price dict
def cleanse(today, map):
    i = 0
    for item in map:
        if item in today:
            value = map[i + 1][32:38]
            value = value.replace('K', '00')
            value = value.replace(',', '')
            value = value.replace('.', '')
            value = int(value.strip())

            today[item] = value
        i += 1

    return today


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

    mapping = newPrices()
    handler = PriceData()
    todays_dict = cleanse(handler.dict, mapping)
    insert_new_price_record(handler.df, todays_dict)



if __name__ == '__main__':
    run()



