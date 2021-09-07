'''
Playground, random stuff
'''
import pickle

PRICE_LOG = 'PRICE_LOG.txt'
with open(PRICE_LOG, 'rb') as f:
    log = pickle.load(f)
f.close()
print(len(log))

log = log[:-1]

print(len(log))
with open(PRICE_LOG, 'wb') as f:
    pickle.dump(log, f)
f.close()
