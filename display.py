import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
from operator import itemgetter
from random import randint
# todo: before using in any other files, indent into a function
# todo: Also remember all these prices are straight from EvE values (API pls)
# todo: List biggest deltas (daily, overall)
# todo: main to run parse, price, etc all at once
# todo: add time to granularize multi-day updates
# todo: separate tiers of ore for better visualization(multi-axis or multi-plot? sentdex)
# todo: delta vs yesterday, vs avg
# todo: fix xticks date (time?)
# todo: add into mining parse to only show what's present
# todo: add class to separate key stats likely to be used in the future: ie lastPriceList, overallDeltaList, etc
#       in order to make adding features easier
# todo: interactive "choose what ores" vs auto sense from mining parse (tie into parse, sep out, have true main)

# parse date ranges for x values
def appendDates(log):
    result = []
    for entry in log:
        result.append(entry['date'][5:])
    return result

# parse through adding lines to subplots, prints historic and most recent price tiering

def parseGraph(oreNames, log):
    #plt.style.use('fivethirtyeight')
    dailyTally = []
    graphSplitter = 0
    subGraphCol = 0
    subGraphRow = 0
    for ore in oreNames:
        axChanging = ax[subGraphCol]
        orePrices = []
        if graphSplitter == 8:
            subGraphCol = 1
        for entry in log:
            orePrices.append(entry[ore])
        axChanging.plot(xDateRange, orePrices)
        axChanging.set_yticks(np.arange(2000, 15000, 1000))
        if subGraphCol == 1:
            rand = randint(1,3)
            axChanging.text(xDateRange[-rand], orePrices[-1], ore, rotation=0, va='bottom')
        else:
            axChanging.text(xDateRange[-2], orePrices[-1], ore, rotation=0, va='bottom')
        print(f'Ore: {ore}\tPriceHist: {orePrices}')
        dailyTally.append([ore, orePrices[-1]])
        dailyTally.append(['T2 ' + ore, orePrices[-1] * 1.15])
        dailyTally.append(['T3 ' + ore, orePrices[-1] * 2])
        graphSplitter += 1
    print("\n\n")
    dailyTally = sorted(dailyTally, key=itemgetter(1), reverse=True)
    for item in dailyTally:
        print(item)
    return fig, ax

# graph maintenance
def display(fig, ax):
    title = 'B-Team Buyback Price Log'
    fig.suptitle(title)
    ax1 = ax[0]
    ax2 = ax[1]
    axList = [ax1, ax2]
    for axis in axList:
        axis.grid()

    ax1.set_title("R64/32")
    ax2.set_title("R16")

    ax1.legend(oreNames[:8], loc='lower left')
    ax2.legend(oreNames[8:12], loc='lower left')

    fig.set_figwidth(12)
    fig.set_figheight(7)
    fig.show()



if __name__ == "__main__":
    # Access class methods for oreNames, price history log
    # todo: latest todo can be applied in this class
    playDict = priceDict()
    oreNames = playDict.oreNameList()
    log = playDict.openLog()
    xDateRange = appendDates(log)
    fig, ax = plt.subplots(1, 2)
    fig, ax = parseGraph(oreNames, log)
    #ax[2].plot(np.arange(0,10,1), np.arange(5,15,1))
    display(fig, ax)





