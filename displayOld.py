'''
Previously used display of historical pricing.
Single graph of historical pricing without current price tiers or in-graph labels
todo: pull the trigger and delete (later)
'''
import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
from operator import itemgetter


fig, ax = plt.subplots()
title = 'B-Team Buyback Price Log'

playDict = priceDict()
oreNames = playDict.oreNameList()
log = playDict.openLog()
print(log)

xDateRange = []
for entry in log:
    xDateRange.append(entry['date'][5:])
dailyTally = []
for ore in oreNames:
    orePrices = []
    for entry in log:
        orePrices.append(entry[ore])

    ax.plot(xDateRange, orePrices)
    print(f'Ore: {ore}\tPriceHist: {orePrices}')
    dailyTally.append([ore, orePrices[-1]])
    dailyTally.append(['T2 ' + ore, orePrices[-1]*1.15])
    dailyTally.append(['T3 ' + ore, orePrices[-1] * 2])
print("\n\n")
dailyTally = sorted(dailyTally, key=itemgetter(1), reverse=True)
for item in dailyTally:
    print(item)

plt.title(title)
plt.yticks(np.arange(2000,14000,1000))
plt.xticks(rotation=55)
plt.grid()
plt.legend(oreNames, loc='lower left')
fig.set_figwidth(15)
fig.set_figheight(9)
plt.show()