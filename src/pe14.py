# seq = [0 for x in range(0, 1000001)]
# seq[1] = 1

def seq(num):
	if num == 1:
		return 1
	else:
		return 1 + ( seq(num/2) if x%2==0 else seq(3*num + 1))

max_seq=1

for x in range(2,1000001):
	ctr = seq(x)
	max_seq = max(ctr, max_seq)
	
print max_seq