import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
# Pull in text file
file = open('miningParse.txt')
lines = file.readlines()
file.close()
# Assign Ore names
# todo: parse column to add names as found (sort by variant percentage?) dicts-Veldspar:0 Dense:1 etc
# todo: multiple graphs to show densities etc side by side
my_dict = {}
# list of ores, total = index9
oreList = ['Veldspar', 'Concentrated Veldspar', 'Dense Veldspar', 'Scordite',
           'Condensed Scordite', 'Massive Scordite', 'Pyroxeres', 'Solid Pyroxeres',
           'Viscous Pyroxeres', 'TotalDIV10']
ores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
oreCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# splits lines, cleans extraneous text, pseudo-switch
for line in lines:
    line = line.split('\t')
    line = [i.strip() for i in line]
    if (len(line) == 1):
        for x in range(2): line.append('0 m3')
    line[2] = line[2][:-3]
    line[2] = line[2].replace(',', '')
    intVol = int(line[2])
    for x in range(len(oreList)):
        if line[0] == oreList[x]:
            choice = x
    ores[choice] = ores[choice] + intVol
    oreCount[choice] += 1
    ores[9] = ores[9] + intVol


maxOreVolume = (20000 - (max(ores[:9]) % 20000)) + max(ores[:9])  # rounded max ore to size graph
total = ores[9]
ores[9] = 0

# New plotting
fig, ax = plt.subplots()
ax.barh(oreList, ores)
plt.xticks(np.arange(0,maxOreVolume, 10000))
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
plt.xlabel('m3')
plt.ylabel('ore variant')
plt.title('Belt Ore Distribution')
plt.grid(axis='x')

# add values in-graph
for i, v in enumerate(ores):
    if i == 9:  # puts actual total as text for divided total bar
        ax.text(v, i, str(total), fontweight='bold')
    else:
        ax.text(v, i, str(int(v)), fontweight='bold')
plt.show()

# Terminal summations/analysis
#
# total v/s/p
veld, scor, pyro = 0,0,0
veldCount, scorCount, pyroCount = 0,0,0
for x in range(3):
    veld += ores[x]
    veldCount += oreCount[x]
for x in range(3,6):
    scor += ores[x]
    scorCount += oreCount[x]
for x in range(6,9):
    pyro += ores[x]
    pyroCount += oreCount[x]
comboOre = [veld, scor, pyro]
comboCount = [veldCount, scorCount, pyroCount]
comboOre = [int(x) for x in comboOre]
oreDensity = np.divide(comboOre, comboCount)
# begin terminal analysis
cycleOre = np.divide(comboOre, 2714)
cycleOre = cycleOre.astype(np.uint)
timeOre = np.divide(comboOre, 2100).astype(np.uint)
baseOreList = ['Veldspar','Scordite','Pyroxeres']
allocOre = [0,0,0]
cycleOreMod = cycleOre.copy()
cyclePC = sum(cycleOre) / 6
for x in range(3):
    while (cycleOreMod[x] > cyclePC):
        allocOre[x] += 1
        cycleOreMod[x] = cycleOreMod[x] - cyclePC
iOfMax = np.argmax(cycleOreMod)
allocOre[iOfMax] += 1
df = np.array([baseOreList, comboOre, cycleOre, timeOre, allocOre])
for x in range(df.shape[1]):
    print(f"{df[0,x]}: {df[1,x]}m3, {df[2,x]} cycles, "
          f"{df[3,x]}min, allocate {df[4,x]}")

print(oreCount)
print(oreDensity)













