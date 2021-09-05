'''
Data processing on historical prices
'''
from gooPriceHistory import gooPriceHistory

ORE_NAMES = ['Loparite', 'Monazite', 'Xenotime', 'Ytterbite',
             'Carnotite', 'Cinnabar', 'Pollucite', 'Zircon',
             'Chromite', 'Otavite', 'Sperrylite', 'Vanadinite']

class PriceData(object):

    def __init__(self):
        self.log = gooPriceHistory().openLog()
        self.dates = []
        self.uniqueDates = []
        self.prices = []
        self.oreNames = ORE_NAMES
        self.lastPrice = []
        self.lastPriceT2 = []
        self.lastPriceT3 = []
        self.intraDelta = []
        self.interDelta = []


    #migrate mining parse
    def addParse(self):
        pass

    # Handles date processing for multiple single-day entries
    # todo: what were you thinking? you can do better than this
    def setXDates(self):
        xDates = []
        xUnique = []
        for entry in self.log:
            thisDate = entry['date'][5:]
            xDates.append(thisDate)
            # find a better workaround for empty entries
            if len(xUnique) == 0:
                xUnique.append(thisDate)
            elif thisDate != xUnique[-1]:
                xUnique.append(thisDate)
            else:
                continue
        self.dates = xDates
        self.uniqueDates = xUnique

    # Parses price data from historical log
    def setPrices(self):
        priceList = []
        for ore in self.oreNames:
            orePrice = []
            for entry in self.log:
                orePrice.append(entry[ore])
            priceList.append(orePrice)
        self.prices = priceList

    # Set most current prices and tiers
    def setLastPrices(self):
        daily, daily2, daily3 = [],[],[]
        for ore in self.oreNames:
            lastPrice = self.log[-1][ore]
            t2 = lastPrice * 1.15 - lastPrice
            daily.append(lastPrice)
            daily2.append(t2)
            daily3.append(lastPrice - t2)
        self.lastPrice = daily
        self.lastPriceT2 = daily2
        self.lastPriceT3 = daily3

    # Set day-to-day and overall historical change in price for each ore
    def setDeltas(self):
        intraDeltas = []
        interDeltas = []
        for ore in self.oreNames:
            intra = self.log[-1][ore] - self.log[-2][ore]
            inter = self.log[-1][ore] - self.log[0][ore]
            intraDeltas.append(intra)
            interDeltas.append(inter)
        self.intraDelta = intraDeltas
        self.interDelta = interDeltas

    # Runs the above methods to populate a working historical log.
    # todo: what's a cleaner way to do this?
    def populate(self):
        self.setXDates()
        self.setPrices()
        self.setLastPrices()
        self.setDeltas()