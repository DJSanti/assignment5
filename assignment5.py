# Names: Bradford, Caleb, Sam
# Assignment #5
# Dr. Timofeyev
# CSC 450
# Dijkstra's Algorithm

# libraries used
import sys #For system input
import pandas as pd #For .csv file input

#getnum function to calculate the costs from .csv
def getnum(node, i, df):
    return df.loc[node, i]
    
# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)

# create N'
nprime = [] 

# ask for a node
node = raw_input("Please, provide the node's name: ")

#puts each node from .csv in nprime
#Initialization in algorithm
for col in df.columns:
    nprime.append(col)

#Cacluates costs for the neighbors attached to starting node
#Initialization in algorithm
distU = getnum(node, 'u', df)
distV = getnum(node, 'v', df)
distW = getnum(node, 'w', df)
distX = getnum(node, 'x', df)
distY = getnum(node, 'y', df)
distZ = getnum(node, 'z', df)

#Used to keep track of the paths and used for shortest path
path = ["u", "v", "w", "x", "y", "z"]

#Beginning node is shortest since it is always 0
shortest = node

#Repeating until there is nothing left in nprime
#Same as repeat in algorithm
while ((len(nprime) > 0)):

    #Makes first minimum 9999 since we only want neighbors
    minimum = 9999

    #Loops through the list of nodes not visited yet and find the minimum value out of all of them
    for i in nprime:
        #First checks to see if the current node is unvisited and if its current value is less than min
        #If so then current value is new min and it shortest path
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
        
        #If the shortest node is one of these, then make the shortest distane the same as their cost
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
    
    #This is where it checks to see if D(v) = min(D(v), D(w) + c(w, v))
    #Basically updates each neighbor of the current visited node to figure out its path
    #Finally, appends the path of the nodes to the path array
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

    #Removes the current node from the list since it has already been visited and added to path
    #Includes part of algorithm where it removes the visited nodes
    nprime.remove(shortest)

#Just formatting and output
#Prints shortest path tree for the node
print "Shortest path tree for node {}:".format(node)
if node == 'u':
    print "{}, {}, {}, {}, {}".format(path[1], path[2], path[3], path[4], path[5])
if node == 'v':
    print "{}, {}, {}, {}, {}".format(path[0], path[2], path[3], path[4], path[5])
if node == 'w':
    print "{}, {}, {}, {}, {}".format(path[0], path[1], path[3], path[4], path[5])
if node == 'x':
    print "{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[4], path[5])
if node == 'y':
    print "{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[3], path[5])
if node == 'z':
    print "{}, {}, {}, {}, {}".format(path[0], path[1], path[2], path[3], path[4])

#Prints the least-cost paths for the node
print "Costs of least-cost paths for node {}:\nu:{}, v:{}, w:{}, x:{}, y:{}, z:{}".format(node, distU, distV, distW, distX, distY, distZ)

