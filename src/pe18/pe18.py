
#dynamic programming solution
import sys


tri = []

fp = open('triangle', 'r')

for line in fp:		
	tri.append(map(int, line.rstrip('\n').split(' ')))

m = len(tri) #height of triangle
n = len(tri[-1]) #breadth of triangle



A = [[] for x in range(m)]
for i in range(m):
	for j in range(n):
		if j < len(tri[i]):
			A[i].append(tri[i][j])  
		else:
			A[i].append(0)


S = [[0 for x in range(n)] for y in range(m)] #initialize state array

S[0][0] = A[0][0]
maxPath = S[0][0]

for i in range(1,m):
	t = len(tri[i])
	for j in range(t):
		S[i][j] = A[i][j] + max(S[i-1][j], j > 0 and S[i-1][j-1] or 0)
		maxPath = S[i][j] >= maxPath and S[i][j] or maxPath

print maxPath