import string


def charsum(x,y):
	return x-64 + y


fp = open('names.txt', 'r')

str = fp.read()
names = str.rstrip('\n').replace('\"', '').split(',')


names.sort()

alpha_sum = 0
i = 1
for name in names:
	alpha_sum += i*sum(map(lambda x:ord(x)-64, list(name)))
	i+=1

print alpha_sum


