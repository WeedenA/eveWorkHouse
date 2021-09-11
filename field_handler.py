'''
Handles dynamic record of objects found in belt parse.
'''

class oreDictionary(dict):

    def __init__(self):
        self = dict()

    # Creates new ore entry with initial volumes
    def addKey(self, key, value=0, isOutRange=False):
        self.setdefault(key, [])
        self[key].append(value)
        if isOutRange:
            self[key].append(0)
        else:
            self[key].append(1)
        self['Total'] += value

    # Adds volume to existing ore entries
    def incrementKey(self, key, value):
        self[key][0] += value
        self[key][1] += 1
        self['Total'] += value

    # Total m3 of belt parse
    def total(self):
        return self['Total']

    # Rounds maximum m3 for graphing purposes
    # todo: re-verify
    def roundedMaxExcludeTotal(self):
        tempList = []
        for key in self:
            if key == 'Total':
                pass
            else:
                tempList.append(self[key][0])
        roundedMax = (200000 - (max(tempList) % 200000)) + max(tempList)
        return roundedMax

    # Creates and returns list of every ore's total volume
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