'''
Parses pasted new price data, retrieves saved historical data and saves new log.
'''
from PriceData import PriceData
import pickle

PRICE_LOG = 'PRICE_LOG.txt'


# Open pasted prices
def newPrices():
    file = open('pennys.txt')
    price_lines = file.readlines()
    file.close()
    mapping = list(map(str.strip, price_lines))
    return price_lines, mapping


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
# Else append today's dict, pickle to file (overwrite, todo: switch to db)
def pickler(handle, today):
    if handle.log[-1]['date'] == today['date']:
        print("Already ran today")
        print(f"Here's your new dict anyways: {today}")
    else:
        handle.log.append(today)
        with open(PRICE_LOG, 'wb') as f:
            pickle.dump(handle.log, f)
        f.close()
        print("New log entry recorded")


def run():
    lines, mapping = newPrices()
    handler = PriceData()
    todays_dict = cleanse(handler.dict, mapping)
    pickler(handler, todays_dict)


if __name__ == '__main__':
    run()



