import math
primes_so_far = []


def is_prime(num):
	if primes_so_far and primes_so_far[-1] <= math.sqrt(num):
		for primes in primes_so_far:
			if num % primes == 0:
				return False
		#no prime factors found
		return True
	else:
		for primes in primes_so_far:
			if num % primes == 0:
				return False
		olist = (x for x in range(primes_so_far[-1] if primes_so_far else 2, int(math.sqrt(num))+1) if x==2 or x%2==1)
		for i in olist:
			if num % i == 0:
				return False
		#no factors found in the extended list
		return True

ctr = 0
i = 2
while True:
	if is_prime(i) :
		primes_so_far.append(i)
		ctr+=1
		if ctr == 10001:
			print i
			break
	i+= (1 if i==2 else 2)


