# Names: Bradford, Caleb, Sam
# Assignment #5

# libraries used
import sys
import pandas as pd

#getnum function
def getnum(node, i, df):
    return df.loc[node, i]
    
# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)

# create N'
nprime = [] 

# ask for a node
node = input("Please, provide the node's name: ")	

 # for v in nodes:	
for col in df.columns:
    nprime.append(col)

distU = getnum(node, 'u', df)
distV = getnum(node, 'v', df)
distW = getnum(node, 'w', df)
distX = getnum(node, 'x', df)
distY = getnum(node, 'y', df)
distZ = getnum(node, 'z', df)

path = ['u', 'v', 'w', 'x', 'y', 'z']

shortest = node
while ((len(nprime) > 0)):
    minimum = 9999
    for i in nprime:
        if i == 'u' and distU < minimum:
            minimum = distU
            shortest = i
        elif i == 'v' and distV < minimum:
            minimum = distV
            shortest = i
        elif i == 'w' and distW < minimum:
            minimum = distW
            shortest = i
        elif i == 'x' and distX < minimum:
            minimum = distX
            shortest = i
        elif i == 'y' and distY < minimum:
            minimum = distY
            shortest = i
        elif i == 'z' and distZ < minimum:
            minimum = distZ
            shortest = i
        
        if shortest == 'u':
            Shortdist = distU
        elif shortest == 'v':
            Shortdist = distV
        elif shortest == 'w':
            Shortdist = distW
        elif shortest == 'x':
            Shortdist = distX
        elif shortest == 'y':
            Shortdist = distY
        elif shortest == 'z':
            Shortdist = distZ

    if 'u' in nprime:
        change = Shortdist + getnum(shortest, 'u', df)
        distU = min(distU, change)    
        if distU == change:
            if shortest == 'v':
                path[0] = path[1] + 'u'
            if shortest == 'w':
                path[0] = path[2] + 'u'
            if shortest == 'x':
                path[0] = path[3] + 'u'
            if shortest == 'y':
                path[0] = path[4] + 'u'
            if shortest == 'z':
                path[0] = path[5] + 'u'
    if 'v' in nprime:
        change = Shortdist + getnum(shortest, 'v', df)
        distV = min(distV, change) 
        if distV == change:
            if shortest == 'u':
                path[1] = path[0] + 'v'
            if shortest == 'w':
                path[1] = path[2] + 'v'
            if shortest == 'x':
                path[1] = path[3] + 'v'
            if shortest == 'y':
                path[1] = path[4] + 'v'
            if shortest == 'z':
                path[1] = path[5] + 'v'
    if 'w' in nprime:
        change = Shortdist + getnum(shortest, 'w', df)
        distW = min(distW, change) 
        if distW == change:
            if shortest == 'u':
                path[2] = path[0] + 'w'
            if shortest == 'v':
                path[2] = path[1] + 'w'
            if shortest == 'x':
                path[2] = path[3] + 'w'
            if shortest == 'y':
                path[2] = path[4] + 'w'
            if shortest == 'z':
                path[2] = path[5] + 'w'
    if 'x' in nprime:
        change = Shortdist + getnum(shortest, 'x', df)
        distX = min(distX, change) 
        if distX == change:
            if shortest == 'u':
                path[3] = path[0] + 'x'
            if shortest == 'v':
                path[3] = path[1] + 'x'
            if shortest == 'w':
                path[3] = path[2] + 'x'
            if shortest == 'y':
                path[3] = path[4] + 'x'
            if shortest == 'z':
                path[3] = path[5] + 'x'
    if 'y' in nprime:
        change = Shortdist + getnum(shortest, 'y', df)
        distY = min(distY, change) 
        if distY == change:
            if shortest == 'u':
                path[4] = path[0] + 'y'
            if shortest == 'v':
                path[4] = path[1] + 'y'
            if shortest == 'w':
                path[4] = path[2] + 'y'
            if shortest == 'x':
                path[4] = path[3] + 'y'
            if shortest == 'z':
                path[4] = path[5] + 'y'
    if 'z' in nprime:
        change = Shortdist + getnum(shortest, 'z', df)
        distZ = min(distZ, change) 
        if distZ == change:
            if shortest == 'u':
                path[5] = path[0] + 'z'
            if shortest == 'v':
                path[5] = path[1] + 'z'
            if shortest == 'w':
                path[5] = path[2] + 'z'
            if shortest == 'x':
                path[5] = path[3] + 'z'
            if shortest == 'y':
                path[5] = path[4] + 'z'

    nprime.remove(shortest)
    
path.sort(key=len)
print("Shortest path tree for node {}:".format(node))
if node == 'u':
    print("{}, {}, {}, {}, {}".format(path[1], path[2], path[3], path[4], path[5]))
if node == 'v':
    print("{}, {}, {}, {}, {}".format(path[0], path[2], path[3], path[4], path[5]))
if node == 'w':
    print("{}, {}, {}, {}, {}".format(path[0], path[1], path[3], path[4], path[5]))
if node == 'x':
    print("{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[4], path[5]))
if node == 'y':
    print("{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[3], path[5]))
if node == 'z':
    print("{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[3], path[4]))

print("Costs of least-cost paths for node {}:\nu:{}, v:{}, w:{}, x:{}, y:{}, z:{}".format(node, distU, distV, distW, distX, distY, distZ))
