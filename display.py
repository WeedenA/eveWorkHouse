import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
# todo: before using in any other files, indent into a function
# todo: Also remember all these prices are straight from EvE values

fig, ax = plt.subplots()
title = 'B-Team Buyback Price Log'

playDict = priceDict()
oreNames = playDict.oreNameList()
log = playDict.openLog()

xDateRange = []
for entry in log:
    xDateRange.append(entry['date'])

for ore in oreNames:
    orePrices = []
    for entry in log:
        orePrices.append(entry[ore])
    ax.plot(xDateRange, orePrices)
    print(f'Ore: {ore}\tPriceHist: {orePrices}')

plt.title(title)
plt.yticks(np.arange(0,15000,1000))
plt.grid()
plt.legend(oreNames, loc='lower left')
plt.show()


