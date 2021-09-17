'''
Playground, random stuff
'''

import sql_server
import pandas as pd
import requests

'''
Web-Scraping
'''
url = "https://pgsus.space/buyback/bteam-buyback/"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

df = pd.DataFrame(columns=['OreName', 'Price'])

for row in soup.find(class_='table table-bordered table-hover').find_all('tr'):
    col = row.find_all('td')
    ore_name = col[0].text
    price = col[1].text
    df = df.append({"OreName":ore_name, "Price":price}, ignore_index=True)
print(df)

df["OreName"] = df["OreName"].str.replace('9.*','', regex=True)
df["OreName"] = df["OreName"].str.strip()
df["Price"] = df["Price"].str.replace('K ', '00', regex=True)
df["Price"] = df["Price"].str.replace('[\.,ISK]', '', regex=True)
df["Price"] = df["Price"].str.strip()



df["Price"] = pd.to_numeric(df["Price"],downcast="integer")
print(df)



# '''
# Display handling
# '''
#
#
# ORE_NAMES = ['Loparite', 'Monazite', 'Xenotime', 'Ytterbite',
#              'Carnotite', 'Cinnabar', 'Pollucite', 'Zircon',
#              'Chromite', 'Otavite', 'Sperrylite', 'Vanadinite']
#
# class sandbox(object):
#
#     def __init__(self):
#         self.df = self.openRecord()
#         self.oreNames = ORE_NAMES
#         self.df['date'] = self.df['date'].dt.date
#
#     def openRecord(self):
#         engine = sql_server.create_sqlalch_engine()
#         table = 'ore_price_record'
#         df = pd.read_sql(table, engine)
#         return df
#
#     def parseGraph(self):
#         graphSplitter = 0
#         subGraphCol = 0
#         for i in range(len(self.oreNames)):
#             if graphSplitter == 8:
#                 subGraphCol = 1
#             ax[subGraphCol].plot(self.df['date'], self.df[self.oreNames[i]])
#             ax[subGraphCol].set_yticks(np.arange(2000, 15000, 1000))
#             graphSplitter += 1
#         return fig, ax
#
#     def plotTiersBar(self):
#         latest_record = self.latest_record
#         tier_price = [latest_record, latest_record*1.15 - latest_record, latest_record*1.15,
#                           latest_record * 2 - latest_record * 1.15, latest_record * 2]
#
#         ax[2].barh(self.oreNames, tier_price[0], label='Base')
#         ax[2].barh(self.oreNames, tier_price[1], left=tier_price[0], label='T2')
#         ax[2].barh(self.oreNames, tier_price[3], left=tier_price[2], label='Jackpot')
#         ax[2].legend()
#
#         # add value in-graph
#         for ore in self.oreNames:
#             ax[2].text(0, ore, tier_price[0][ore], va='top')
#             ax[2].text(int(tier_price[2][ore]), ore, int(tier_price[2][ore]), va='center')
#             ax[2].text(tier_price[4][ore], ore, tier_price[4][ore], va='bottom')
#
#         # graph title, ticks, grid
#         xRange = np.arange(0, 28000, 1000).tolist()
#         ax[2].set_xticks(xRange, minor=True)
#         ax[2].grid(which='minor', alpha=0.4)
#         ax[2].grid(which='major', alpha=1)
#         ax[2].set_title('Current Price Tiers')
#
#
#     def plotFigure(self):
#         title = 'Goo Pricing'
#         fig.suptitle(title)
#         ax1 = ax[0]
#         ax2 = ax[1]
#         axList = [ax1, ax2]
#
#
#         ax1.set_title("R64/32")
#         ax2.set_title("R16")
#
#         # might need unique
#         ax1.set_xticks(self.df['date'], minor=True)
#         ax2.set_xticks(self.df['date'], minor=True)
#
#         for axis in axList:
#             axis.grid(which='major', alpha=0.8)
#             axis.grid(which='minor', alpha=0.4)
#
#         ax1.legend(self.oreNames[:8], loc='lower left')
#         ax2.legend(self.oreNames[8:12], loc='lower left')
#
#         fig.set_figwidth(18)
#         fig.set_figheight(9)
#         fig.show()
#
#
# def run():
#     sand = sandbox()
#     global fig, ax
#     fig, ax = plt.subplots(1, 3)
#     sand.parseGraph()
#     sand.plotTiersBar()
#     sand.plotFigure()
#
#
#
# if __name__ == "__main__":
#     run()
