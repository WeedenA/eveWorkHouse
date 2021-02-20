import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
# Pull in text file
file = open('miningParse.txt')
lines = file.readlines()
file.close()
# Assign Ore names
# todo: parse column to add names as found (sort by variant percentage?)
my_dict = {}
# list of ores, total = index9
oreList = ['Veldspar', 'Concentrated Veldspar', 'Dense Veldspar', 'Scordite',
           'Condensed Scordite', 'Massive Scordite', 'Pyroxeres', 'Solid Pyroxeres',
           'Viscous Pyroxeres', 'TotalDIV10']
print(oreList)
ores = [0,0,0,0,0,0,0,0,0,0]

# splits lines, cleans extraneous text, pseudo-switch
for line in lines:
    line = line.split('\t')
    line = [i.strip() for i in line]
    #empt = np.append(empt, np.array([line]), axis=0)
    if (len(line) == 1):
        for x in range(2): line.append('0 m3')
    line[2] = line[2][:-3]
    line[2] = line[2].replace(',', '')
    intVol = int(line[2])
    # kill me now, not after
    if line[0] == oreList[0]:
        ores[0] = ores[0] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[1]:
        ores[1] = ores[1] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[2]:
        ores[2] = ores[2] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[3]:
        ores[3] = ores[3] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[4]:
        ores[4] = ores[4] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[5]:
        ores[5] = ores[5] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[6]:
        ores[6] = ores[6] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[7]:
        ores[7] = ores[7] + intVol
        ores[9] = ores[9] + intVol
    elif line[0] == oreList[8]:
        ores[8] = ores[8] + intVol
        ores[9] = ores[9] + intVol

print(f"{ores}\n")  # final values before div
ores[9] = ores[9] / 10  # doesn't skew graph as much (TOTAL)
maxOreVolume = (20000 - (max(ores) % 20000)) + max(ores)  # rounded max ore to size graph

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
        ax.text(v, i, str(int(v) * 10), fontweight='bold')
    else:
        ax.text(v, i, str(int(v)), fontweight='bold')
plt.show()

# Terminal summations/analysis
#
# total v/s/p
veld, scor, pyro = 0,0,0
for x in range(3):
    veld = ores[x] + veld
for x in range(3,6):
    scor = ores[x] + scor
for x in range(6,9):
    pyro = ores[x] + pyro
comboOre = [veld, scor, pyro]
comboOre = [int(x) for x in comboOre]
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
        allocOre[x] = allocOre[x] + 1
        cycleOreMod[x] = cycleOreMod[x] - cyclePC
df = np.array([baseOreList, comboOre, cycleOre, timeOre, allocOre])
for x in range(df.shape[1]):
    print(f"{df[0,x]}: {df[1,x]}m3, {df[2,x]} cycles, "
          f"{df[3,x]}min, allocate {df[4,x]}")
freePilots = 6 - sum(allocOre)
print(f"Free pilots: {freePilots}\t||\tCPC:{cyclePC}")












