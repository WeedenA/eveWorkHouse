import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
from operator import itemgetter
from random import randint
from openOsFile import openApp
from PriceData import PriceData
# todo: add into mining parse to only show what's present
# todo: interactive "choose what ores" vs auto sense from mining parse (tie into parse, sep out, have true main)
# todo: enumerate into barchart deltas, or tiered pricing (like from mining parse names)


def printStats():
    i = 0
    for ore in Handler.oreNames:
        print(f'Ore: {ore}\tPriceHist: {Handler.prices[i]}')
        print(f'Daily Delta: \t{Handler.intraDelta[i]}')
        print(f'Over Delta: \t{Handler.interDelta[i]}')

        i += 1


def parseGraph():
    graphSplitter = 0
    subGraphCol = 0
    subGraphRow = 0
    i = 0
    for ore in Handler.oreNames:
        if graphSplitter == 8:
            subGraphCol = 1
        ax[subGraphCol].plot(Handler.dates, Handler.prices[i])
        ax[subGraphCol].set_yticks(np.arange(2000, 15000, 1000))
        if subGraphCol == 1:
            rand = randint(1,3)
            ax[subGraphCol].text(Handler.dates[-rand], Handler.prices[i][-1], ore, rotation=0, va='bottom')
        else:
            ax[subGraphCol].text(Handler.dates[-2], Handler.prices[i][-1], ore, rotation=0, va='bottom')
        graphSplitter += 1
        i += 1
    return fig, ax


def plotHistLines():
    title = 'B-Team Buyback Price Log'
    fig.suptitle(title)
    ax1 = ax[0]
    ax2 = ax[1]
    axList = [ax1, ax2]
    for axis in axList:
        axis.grid()

    ax1.set_title("R64/32")
    ax2.set_title("R16")

    ax1.legend(Handler.oreNames[:8], loc='lower left')
    ax2.legend(Handler.oreNames[8:12], loc='lower left')


def plotTiersBar():
    bars = np.add(Handler.lastPrice,Handler.lastPriceT2).tolist()
    for i in range(3):
        ax[2].barh(Handler.oreNames, Handler.lastPrice, label='Base')
        ax[2].barh(Handler.oreNames, Handler.lastPriceT2, left=Handler.lastPrice, label='T2')
        ax[2].barh(Handler.oreNames, Handler.lastPriceT3, left=bars, label='Jackpot')
    xRange = np.arange(0,25000,1000).tolist()
    ax[2].set_xticks(xRange, minor=True)
    ax[2].grid(which='minor', alpha=0.8)
    ax[2].grid(which='major', alpha=1)


def plotFigure():
    fig.set_figwidth(15)
    fig.set_figheight(7)
    fig.show()


if __name__ == "__main__":
    Handler = PriceData()
    Handler.populate()
    fig, ax = plt.subplots(1, 3)
    parseGraph()
    plotTiersBar()
    plotHistLines()
    plotFigure()
    printStats()






