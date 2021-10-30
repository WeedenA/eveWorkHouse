'''
Displays historical pricing across two graphs and a tiered chart of current prices.
Prints complete price history

stretch: integrate into mining parse to only show what's present
stretch: switch to monthly bucket xticks
stretch: Append ore labels in-graph (no overlap)
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from price_handler import PriceData

# Displays ore name, total price log history
# place delta calcs here
def print_stats(hand):
    for ore in hand.oreNames:
        print(f'Ore: \t\t{ore}\nPriceHist: {hand.df[ore].tolist()}')


# Plots graphs - Splits bottom 1/3 of ores into second graph to reduce overlap
def plot_hist_prices(hand, ax):
    graphSplitter = 0
    subGraphCol = 0
    for i in range(len(hand.oreNames)):
        if graphSplitter == 8:
            subGraphCol = 1
        ax[subGraphCol].plot(hand.df['date'], hand.df[hand.oreNames[i]])
        ax[subGraphCol].set_yticks(np.arange(2000, 15000, 1000))
        graphSplitter += 1
    return ax


# Plots 3-tiered bar chart for last known price values
def plot_tiered_axis(hand, ax):
    latest_record = hand.latest_record
    tier_price = [latest_record, latest_record * 1.15 - latest_record, latest_record * 1.15,
                  latest_record * 2 - latest_record * 1.15, latest_record * 2]

    ax[2].barh(hand.oreNames, tier_price[0], label='Base')
    ax[2].barh(hand.oreNames, tier_price[1], left=tier_price[0], label='T2')
    ax[2].barh(hand.oreNames, tier_price[3], left=tier_price[2], label='Jackpot')
    ax[2].legend()

    # Place value in-graph
    for ore in hand.oreNames:
        ax[2].text(0, ore, tier_price[0][ore], va='top')
        ax[2].text(int(tier_price[2][ore]), ore, int(tier_price[2][ore]), va='center')
        ax[2].text(tier_price[4][ore], ore, tier_price[4][ore], va='bottom')

    return ax


# Graph axes titles, labels, legends
def plot_figure(hand, fig, ax):
    title = 'Goo Pricing'
    fig.suptitle(title)


    ax[0].set_title("R64/32")
    ax[1].set_title("R16")
    ax[2].set_title('Current Price Tiers')

    ax[0].legend(hand.oreNames[:8], loc='upper center', ncol=2)
    ax[1].legend(hand.oreNames[8:12], loc='upper center')

    # data formatter, to be changed to monthly buckets
    for x in range(2):
        xfmt = mdates.DateFormatter('%Y-%m-%d')
        ax[x].xaxis.set_major_formatter(xfmt)
        ax[x].set_xticks(hand.df['date'])
        ax[x].set_xticklabels(hand.df['date'].dt.strftime('%m-%d'), rotation=90)

    tiered_x_range = np.arange(0, 28000, 1000).tolist()
    ax[2].set_xticks(tiered_x_range, minor=True)

    for axis in ax:
        axis.grid(which='major', alpha=1)
        axis.grid(which='minor', alpha=0.4)

    fig.set_figwidth(20)
    fig.set_figheight(10)




def run():

    fig, ax = plt.subplots(1, 3)
    handle = PriceData()
    ax = plot_hist_prices(handle, ax)
    ax = plot_tiered_axis(handle, ax)
    plot_figure(handle, fig, ax)
    print_stats(handle)
    plt.show()

if __name__ == "__main__":
    run()







