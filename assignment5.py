# Names: Brad, Caleb, Sam
# Assignment #5

#Dijkstra's Algorithm
import sys
import pandas as pd

filename = sys.argv[1]
df = pd.read_csv(filename, index_col=0)
print df


node = raw_input("Please, provide the node's name: ")
print node

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
