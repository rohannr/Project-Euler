
fp = open('grid.txt', 'r')

ilist = []
for line in fp:		
	ilist.append(map(int, line.rstrip('\n').split(' ')))


max_prod = 1;

for i in range(0,20):
	for j in range(0,20):
		down  = i + 3 < 20 and ilist[i][j]* ilist[i+1][j]* ilist[i+2][j]* ilist[i+3][j] or 1
		right = j + 3 < 20 and ilist[i][j]* ilist[i][j+1]* ilist[i][j+2]* ilist[i][j+3] or 1
		diag1 = (i + 3 < 20 and j + 3 < 20) and ilist[i][j] *ilist[i+1][j+1]*ilist[i+2][j+2]*ilist[i+3][j+3] or 1
		diag2 = (i + 3 < 20 and j - 3 >=0) and ilist[i][j] *ilist[i+1][j-1]*ilist[i+2][j-2]*ilist[i+3][j-3] or 1
		max_prod = max(down,right,diag1, diag2, max_prod)
		
print max_prod

	