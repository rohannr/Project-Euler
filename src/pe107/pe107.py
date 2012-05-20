import networkx as nx 
import matplotlib.pyplot as plt
import sys

G = nx.Graph()

fp = open('network.txt', 'r')

nov = 40 #number of vertices in graph
i=0
j=0

def convert(v):
	if v == '-':
		return sys.maxint
	else:
		return int(v)

def isum(wlist):
	ctr = 0
	for weight in wlist:
		ctr+= (0 if weight == sys.maxint else weight)
	return ctr
	
for line in fp:
	adj = map(convert, line.rstrip('\r\n').split(','))
	for j in range(nov):
		G.add_edge(i,j,weight=adj[j])
	i+=1

# total_weight = sum([weight for edge, weight, in nx.get_edge_attributes(G, 'weight')])

weight_list = (G[a][b]['weight'] for a,b in nx.get_edge_attributes(G, 'weight'))

total_weight = isum(weight_list)

print total_weight

T =nx.prim_mst(G)
new_weight_list = (T[a][b]['weight'] for a,b in nx.get_edge_attributes(T, 'weight')) 
new_weight = isum(new_weight_list)

print new_weight

print "Savings %ld" % (total_weight - new_weight)

#set root's key to zero
