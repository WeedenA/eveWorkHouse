from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import pickle

ORE_NAMES = ['Loparite', 'Monazite', 'Xenotime', 'Ytterbite',
             'Carnotite', 'Cinnabar', 'Pollucite', 'Zircon',
             'Chromite', 'Otavite', 'Sperrylite', 'Vanadinite']

class gooPriceHistory(dict):

    def __init__(self):
        self = dict()


    def populate(self):
        self['date'] = str(date.today())
        for name in ORE_NAMES:
            self[name] = 0



    def graph(self):
        date = list(self.values())[0]
        values = list(self.values())[1:]
        fig, ax = plt.subplots()
        ax.barh(ORE_NAMES, values)
        plt.title(date)
        plt.show()

    def openLog(self):
        with open('PRICE_LOG.txt', 'rb') as f:
            log = pickle.load(f)
        f.close()
        return(log)

    def oreNameList(self):
        return ORE_NAMES