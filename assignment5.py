# Names: Brad, Caleb, Sam
# Assignment #5

# libraries used
import sys
import pandas as pd

#getnum function
def getnum(node, i):
    print "{}, {}".format(node,i)
    #Repeat
    #while 
    #find w not in nprime such that D(w) is min
    # add w to nprime
    #	D(v) = min(D(v), D(w)+c(w,v))
    # compare with if statement to determine min
    #until all of nodes in nprime
    

# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)
print df

# create N, N'
n = []
hold = []
nprime = [] 

# ask for a node
node = raw_input("Please, provide the node's name: ")

# get the row that corresponds to our node
#n = df.loc[[node]]

# for v in nodes:
for col in df.columns:
	# if v < 9999
	if df.loc[node, col] < 9999:		
		# D(v) = c(u,v)
		dv = [col, df.loc[node,col]]		
		hold.append(dv)
        nprime.append(col)
	# else D(v) = infinity
print hold
print nprime

for i in nprime:
    if i != node:
        getnum(node,i)
    else:
        n.append(node, 0)
