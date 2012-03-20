import os


num = 2**1000
sum = 0

while (num > 0):
	dig = num%10
	num = num/10
	sum = sum + dig

print sum