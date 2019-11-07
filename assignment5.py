# Names: Brad, Caleb, Sam
# Assignment #5

# libraries used
import sys
import pandas as pd

# get filename of .csv, get it as a dataframe
filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)
print df

# ask for a node
node = raw_input("Please, provide the node's name: ")
print node

# get the row that corresponds to our node
print(df.loc[[node]])

# for v in nodes:
# if v != 9999
# D(v) = c(u,v)
# else D(v) = infinity

#Repeat
#find w not in nprime such that D(w) is min
# add w to nprime
#	D(v) = min(D(v), D(w)+c(w,v))
# compare with if statement to determine min
#until all of nodes in nprime
