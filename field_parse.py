'''
Parses and sanitizes survey scanner paste to visually present the amount of ore remaining.
Prints total and in-range amounts, number of asteroids to console.
todo: main is too long. modularize.
'''

import matplotlib.pyplot as plt; plt.rcdefaults()
from field_handler import oreDictionary as oreDict

MAX_SCANNER_RANGE = 121
MAX_MINING_RANGE = 24

def cleanLines(line):
    line = line.split('\t')
    # check if rocks went empty, handle it
    if (len(line) == 1):
        for x in range(2): line.append('0 m3')
        line.append('50 km')
    # remove "m3" from volume, ore header newlines
    name = line[0]
    name = name.strip('\n')
    volume = line[2][:-3]
    # remove comma from m3 to handle as int
    volume = volume.replace(',', '')
    volume = int(volume)
    distance = line[3][:-3].strip()
    distance = distance.replace(',', '')
    distance = int(distance)
    if distance > MAX_SCANNER_RANGE:
        distance = 10
    return name, volume, distance

# Pull in text file
file = open('zpaste_survey_scan.txt')
lines = file.readlines()
file.close()

# sets initial dict
dynamicOreNames = oreDict()
inRangeOre = oreDict()
inRangeOre['Total'] = 0
dynamicOreNames['Total'] = 0
# splits lines, cleans extraneous text, adds ore to dict or increments volume
for line in lines:
    name, volume, distance = cleanLines(line)
    if name not in dynamicOreNames:
        dynamicOreNames.addKey(name, volume)

        if distance < MAX_MINING_RANGE:
            inRangeOre.addKey(name, volume)
        else:
            inRangeOre.addKey(name, 0, isOutRange=True)
    else:
        dynamicOreNames.incrementKey(name, volume)
        if distance < MAX_MINING_RANGE:
            inRangeOre.incrementKey(name, volume)

# Terminal Outputs, graphing calcs
# todo: make a class for these sets?
print(f'Final Dict: {dynamicOreNames}')
print(f'In Range Ores: {inRangeOre}')
total= dynamicOreNames.total()
roundedMax = dynamicOreNames.roundedMaxExcludeTotal()
print(f'Max Volume Rounded: {roundedMax}')
oreNameList = list(dynamicOreNames.keys())
oreVolumeList = dynamicOreNames.volumeList()
print(f'Ore volumes: {oreVolumeList}')
# set total to 0 for graphing purposes, allows cleaner graph and can still label with actual total
oreVolumeList[0] = 0
print(f'Total m3: {total}')




# New plotting
fig, ax = plt.subplots()
ax.barh(oreNameList, oreVolumeList)
#plt.xticks(np.arange(0,roundedMax,roundedMax/10))
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
plt.xlabel('m3')
plt.ylabel('variant')
plt.title('Belt Distribution')
plt.grid(axis='x')

# add values in-graph
for i, v in enumerate(oreVolumeList):
    if i == 0:  # puts actual total as text for divided total bar
        ax.text(v, i, str(total), fontweight='bold')
    else:
        ax.text(v, i, str(int(v)), fontweight='bold')

fig.set_figwidth(11)
fig.set_figheight(7)
plt.show()















