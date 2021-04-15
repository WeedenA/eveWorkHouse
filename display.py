import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
from operator import itemgetter
# todo: before using in any other files, indent into a function
# todo: Also remember all these prices are straight from EvE values (API pls)
# todo: List biggest deltas (daily, overall)
# todo: main to run parse, price, etc all at once
# todo: add time to granularize mutli-day updates
# todo: separate tiers of ore for better visualization(multi-axis or multi-plot? sentdex)
# todo: delta vs yesterday, vs avg
# todo: fix xticks date (time?)

fig, ax = plt.subplots()
title = 'B-Team Buyback Price Log'

playDict = priceDict()
oreNames = playDict.oreNameList()
log = playDict.openLog()
print(log)

xDateRange = []
for entry in log:
    xDateRange.append(entry['date'])
# todo: clean this, add into mining parse to only show what's present
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
plt.grid()
plt.legend(oreNames, loc='lower left')
plt.show()




