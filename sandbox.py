import numpy as np
oreList = ['Veldspar', 'Scordite', 'Pyro']
ores = [100,200,300]

test = np.array([oreList, ores])
print(test)
print(f"Veldspar: {test[:,0]}")


comboOre = [veld, scor, pyro]
comboOre = [int(x) for x in comboOre]
# begin terminal analysis
divOre = [i/1000 for i in comboOre]
# print(f"Total Veldspar: {int(divOre[0])}km3")
# print(f"Total Scordite: {int(divOre[1])}km3")
# print(f"Total Pyroxeres: {int(divOre[2])}km3")
cycleOre = np.divide(comboOre, 2714)
cycleOre = cycleOre.astype(np.uint)
timeOre = np.divide(comboOre, 2100).astype(np.uint)
alloc = np.array([['Veldspar', 'Scordite', 'Pyroxeres'], cycleOre])
for x in alloc: print(x)
cyclePC = sum(cycleOre) / 6


print("\nOre: Character Cycles / Character Time / Assigned Chars")
print(f"Veldspar: {cycleOre[0]} cycles / {timeOre[0]} minutes / ")
print(f"Scordite: {cycleOre[1]} cycles / {timeOre[1]} minutes / ")
print(f"Pyroxeres: {cycleOre[2]} cycles / {timeOre[2]} minutes / ")
# test, works :)
# for x in range (len(ores)):
#     print(f"{oreList[x]} : {ores[x]}")
# What next?
