from gooPriceHistory import gooPriceHistory as priceDict
import pickle

PRICE_LOG = 'PRICE_LOG.txt'
#Load pickled list of historical data dictionaries


# Open price copy/paste
file = open('pennys.txt')
lines = file.readlines()
file.close()

# Initiate, fill from scanned file
todaysDict = priceDict()
log = todaysDict.openLog()
todaysDict.populate()
mapping = list(map(str.strip, lines))

# Clean values, assign prices
i = 0
for item in mapping:
    if item in todaysDict:
        value = mapping[i+1][32:38]
        value = value.replace('K', '00')
        value = value.replace(',', '')
        value = value.replace('.', '')
        value = int(value.strip())

        todaysDict[item] = value
    i += 1

# Make it pretty
todaysDict.graph()

# If the last entry was today, don't make another
# Else append today's dict, pickle to file (overwrite)
if log[-1]['date'] == todaysDict['date']:
    print("already ran it today dumbass")
    print(f"here's your dict: {todaysDict}")
    log.append(todaysDict)
    with open(PRICE_LOG, 'wb') as f:
        pickle.dump(log, f)
    f.close()
else:
    log.append(todaysDict)
    with open(PRICE_LOG, 'wb') as f:
        pickle.dump(log, f)
    f.close()




