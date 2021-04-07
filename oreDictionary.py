'''
Functional Dictionary to handle ore data top to bottom

@author: Alex Weeden
'''

class oreDictionary(dict):

    def __init__(self):
        self = dict()

    # todo: combine these two
    def addKey(self, key, value=0, isOutRange=False):
        self.setdefault(key, [])
        self[key].append(value)
        if isOutRange:
            self[key].append(0)
        else:
            self[key].append(1)
        self['Total'] += value

    def incrementKey(self, key, value):
        self[key][0] += value
        self[key][1] += 1
        self['Total'] += value

    def total(self):
        return self['Total']

    def roundedMaxExcludeTotal(self):
        tempList = []
        result = 0
        for key in self:
            if key == 'Total':
                pass
            else:
                tempList.append(self[key][0])
        roundedMax = (200000 - (max(tempList) % 200000)) + max(tempList)
        return roundedMax

    def volumeList(self):
        returnList = []
        for entry in self.values():
            try:
                entry[0]
            except TypeError:
                returnList.append(entry)
                continue
            returnList.append(entry[0])
        return returnList