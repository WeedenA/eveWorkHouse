'''
Populates new daily dict


todo: merge into PriceData
'''
from datetime import date
import matplotlib.pyplot as plt
import pickle

ORE_NAMES = ['Loparite', 'Monazite', 'Xenotime', 'Ytterbite',
             'Carnotite', 'Cinnabar', 'Pollucite', 'Zircon',
             'Chromite', 'Otavite', 'Sperrylite', 'Vanadinite']
PRICE_LOG = 'PRICE_LOG.txt'

class gooPriceHistory(dict):

    def __init__(self):
        self = dict()

    # Initializes new daily dict with ore names
    def populate(self):
        self['date'] = str(date.today())
        for name in ORE_NAMES:
            self[name] = 0


    # Old graph of single-day pricing (todo: outdated, delete)
    def graph(self):
        date = list(self.values())[0]
        values = list(self.values())[1:]
        fig, ax = plt.subplots()
        ax.barh(ORE_NAMES, values)
        plt.title(date)
        plt.show()

    # Opens and returns historical price log
    def openLog(self):
        with open(PRICE_LOG, 'rb') as f:
            log = pickle.load(f)
        f.close()
        return(log)

    def oreNameList(self):
        return ORE_NAMES