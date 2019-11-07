# Names: Brad, Caleb, Sam
# Assignment #5

# libraries used
import sys
import pandas as pd

# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)
print df

# create N, N'
n = []
nprime = [] 

# ask for a node
node = raw_input("Please, provide the node's name: ")

# get the row that corresponds to our node
n = df.loc[[node]]
print n
print "\n"

# for v in nodes:
for col in df.columns:
	# if v != 9999
	if df.loc[node, col] < 9999:		
		# D(v) = c(u,v)
		nprime.append([col, df.loc[node,col]])
		print "{}, {}".format(col, df.loc[node,col])
	# else D(v) = infinity
	else:
		print "{} is infinity".format(col)
print nprime

#Repeat
#find w not in nprime such that D(w) is min
# add w to nprime
#	D(v) = min(D(v), D(w)+c(w,v))
# compare with if statement to determine min
#until all of nodes in nprime
