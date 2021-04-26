import matplotlib.pyplot as plt
import numpy as np
from gooPriceHistory import gooPriceHistory as priceDict
from operator import itemgetter
from random import randint
from openOsFile import openApp
from PriceData import PriceData
# todo: add into mining parse to only show what's present
# todo: interactive "choose what ores" vs auto sense from mining parse (tie into parse, sep out, have true main)
# todo: display deltas in graph
# todo: price tier legend (wonky graphing colors)
# todo: PyQt tut

def printStats():
    i = 0
    for ore in Handler.oreNames:
        print(f'Ore: \t\t{ore}\nPriceHist: {Handler.prices[i]}')
        print(f'Intra Delta: \t{Handler.intraDelta[i]}')
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
        if subGraphCol == 1 and i % 2 == 0:
            rand = randint(1,3)
            ax[subGraphCol].text(Handler.dates[-3], Handler.prices[i][-1]+150, ore, rotation=0, va='bottom')
        elif subGraphCol == 0  and i == 2:
            ax[subGraphCol].text(Handler.dates[-3], Handler.prices[i][-1]+150, ore, rotation=0, va='bottom')
        else:
            ax[subGraphCol].text(Handler.dates[-1], Handler.prices[i][-1], ore, rotation=0, va='bottom')
        graphSplitter += 1
        i += 1
    return fig, ax


def plotHistLines():
    pass


def plotTiersBar():
    bars = np.add(Handler.lastPrice,Handler.lastPriceT2).tolist()
    ax[2].barh(Handler.oreNames, Handler.lastPrice, label='Base')
    ax[2].barh(Handler.oreNames, Handler.lastPriceT2, left=Handler.lastPrice, label='T2')
    ax[2].barh(Handler.oreNames, Handler.lastPriceT3, left=bars, label='Jackpot')
    ax[2].legend()
    i = 0
    for ore in Handler.oreNames:
        last = int(Handler.lastPrice[i])
        last2 = int(Handler.lastPriceT2[i] + last)
        last3 = int(Handler.lastPriceT3[i] * 2)
        ax[2].text(0, ore, last, va='top')
        ax[2].text(last, ore, last2, va='center')
        ax[2].text(last3, ore, last3, va='bottom')
        i += 1
    xRange = np.arange(0,25000,1000).tolist()
    ax[2].set_xticks(xRange, minor=True)
    ax[2].grid(which='minor', alpha=0.8)
    ax[2].grid(which='major', alpha=1)
    ax[2].set_title('Current Price Tiers')


def plotFigure():
    title = 'Goo Pricing'
    fig.suptitle(title)
    ax1 = ax[0]
    ax2 = ax[1]
    axList = [ax1, ax2]
    for axis in axList:
        axis.grid()

    ax1.set_title("R64/32")
    ax2.set_title("R16")

    ax1.set_xticklabels(Handler.uniqueDates, rotation=90)
    ax2.set_xticklabels(Handler.uniqueDates, rotation=90)

    ax1.legend(Handler.oreNames[:8], loc='lower left')
    ax2.legend(Handler.oreNames[8:12], loc='lower left')

    fig.set_figwidth(18)
    fig.set_figheight(9)
    fig.show()

def run():
    global Handler
    global fig
    global ax
    Handler = PriceData()
    Handler.populate()
    plt.style.use('default')
    fig, ax = plt.subplots(1, 3)
    parseGraph()
    plotTiersBar()
    plotHistLines()
    plotFigure()
    printStats()

    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available if style != 'classic')
    print(style_list)

if __name__ == "__main__":
    run()







