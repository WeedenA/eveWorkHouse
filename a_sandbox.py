'''
Playground, random stuff
'''
import sql_server
from datetime import date

from price_handler import PriceData

handle = PriceData()
lastDate = handle.df['date'].iloc[-1]

print(lastDate)

print('yes') if lastDate == date.today() else print('no')

# print(date.today())
#
# print('yes') if dates.tail(1) == date.today() else print('no')





# engine = sqlServer.create_sqlalch_engine()
# res = sqlServer.execute_alch_query(engine, 'SELECT * FROM ore_price_record')
# for item in res:
#     print(item)



# PRICE_LOG = 'zPRICE_LOG.txt'
# with open(PRICE_LOG, 'rb') as f:
#     log = pickle.load(f)
# f.close()
# print(len(log))
#
# log = log[:-1]
# print(log[-1])

#
# with open(PRICE_LOG, 'wb') as f:
#     pickle.dump(log, f)
# f.close()
