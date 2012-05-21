

seq = {1:1}  #initializing first memoization

def eval_collatz(n):
	if n in seq:
		return seq[n]
	elif n%2 == 0:
		n1 = n/2
		return 1 + eval_collatz(n1)
	else:
		n1 = 3*n + 1
		return 1 + eval_collatz(n1)

max_seq = 1
max_terms = 1

for x in xrange(1,1000001):
	terms = eval_collatz(x)
	seq[x] = terms
	max_seq = x if terms > max_terms else max_seq
	max_terms = max(terms, max_terms)
	

print max_seq