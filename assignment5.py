# Names: Brad, Caleb, Sam
# Assignment #5

# libraries used
import sys
import pandas as pd


def getnodes(row):
	# D(v) = c(u,v)
	#dv = [node+col, df.loc[node,col]]
	pv = row
	dv = (graph.loc[row,col])
	hold.append([dv, pv, col])
	
	
# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
# create graph
graph = pd.read_csv(filename, index_col=0)
print graph

# create N', hold
hold = []
nprime = [] 

# ask for a node
source = raw_input("Please, provide the node's name: ")
nprime.append(source)
row = source

# for all neighbors
for col in graph.columns:
	if col not in nprime:
		nprime.append(col)
	# if v < 9999	
	if graph.loc[row, col] < 9999:		
		getnodes(row)
		
print hold
print nprime
