'''
Parses pasted new price data, retrieves saved historical data and saves new dict.
todo: Modularize
'''
from gooPriceHistory import gooPriceHistory as priceDict
import pickle

PRICE_LOG = 'PRICE_LOG.txt'


def run():
    # Open pasted prices
    file = open('pennys.txt')
    lines = file.readlines()
    file.close()

    # Pull historical pricing
    todaysDict = priceDict()
    log = todaysDict.openLog()
    todaysDict.populate()
    mapping = list(map(str.strip, lines))

    # Clean new values, populate into price dict
    i = 0
    for item in mapping:
        if item in todaysDict:
            value = mapping[i + 1][32:38]
            value = value.replace('K', '00')
            value = value.replace(',', '')
            value = value.replace('.', '')
            value = int(value.strip())

            todaysDict[item] = value
        i += 1

    # todo: bring this in-class
    todaysDict.graph()

    # If the last entry was today, don't make another
    # Else append today's dict, pickle to file (overwrite)
    if log[-1]['date'] == todaysDict['date']:
        print("Already ran today")
        print(f"Here's your new dict anyways: {todaysDict}")
    else:
        log.append(todaysDict)
        with open(PRICE_LOG, 'wb') as f:
            pickle.dump(log, f)
        f.close()

if __name__ == '__main__':
    run()



