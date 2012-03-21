
n = 2000000
primes = [[x, True] for x in range(0,n)]



for p in primes:
	if p[0] >=2 and p[1] == True:
		i = p[0]*p[0]
		while i < n:
			primes[i][1] = False
			i+=p[0]
	pass

def add(x,y): 
	return x+y

primesum = reduce(add,  [x[0] for x in primes if x[1] == True and x[0] >=2])
print primesum

