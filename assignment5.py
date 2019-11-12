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
#print df

# create N, N'
n = []
nprime = [] 

# ask for a node
node = raw_input("Please, provide the node's name: ")

n.append(node)
nprime.remove(node)

print "The following is nPrime"
print nprime

distU = getnum(node, 'u', df)
distV = getnum(node, 'v', df)
distW = getnum(node, 'w', df)
distX = getnum(node, 'x', df)
distY = getnum(node, 'y', df)
distZ = getnum(node, 'z', df)

pathU = [node]
pathV = [node]
pathW = [node]
pathX = [node]
pathY = [node]
pathZ = [node]

final_path = []

 #Repeat
    #while 
    #find w not in nprime such that D(w) is min
    # add w to nprime
    #	D(v) = min(D(v), D(w)+c(w,v))
    # compare with if statement to determine min
    #until all of nodes in nprime
shortest = node
while ((len(nprime) > 0)):
    minimum = 9999
    print nprime
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

    print shortest
    
    if 'u' in nprime:
        distU = min(distU, Shortdist + getnum(shortest, 'u', df))    
    if 'v' in nprime:
        distV = min(distV, Shortdist + getnum(shortest, 'v', df)) 
    if 'w' in nprime:
        distW = min(distW, Shortdist + getnum(shortest, 'w', df)) 
    if 'x' in nprime:
        distX = min(distX, Shortdist + getnum(shortest, 'x', df)) 
    if 'y' in nprime:
        distY = min(distY, Shortdist + getnum(shortest, 'y', df)) 
    if 'z' in nprime:
        distZ = min(distZ, Shortdist + getnum(shortest, 'z', df)) 

    #print "u: {}\nv: {}\nw: {}\nx: {}\ny: {}\nz: {}\n".format(distU, distV, distW, distX, distY, distZ)

    n.append(shortest)
    nprime.remove(shortest)

print "Shortest path tree for node {}:".format(node)
print "Costs of least-cost paths for node {}:\nu:{}, v:{}, w:{}, x:{}, y:{}, z:{}".format(node, distU, distV, distW, distX, distY, distZ)

