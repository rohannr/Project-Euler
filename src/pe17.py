import math

ones = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = [" ", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]




oneseq = list(enumerate(ones, start=1))
tenseq = list(enumerate(tens, start=10))


def to_words(num): 
	if (num < 10):
		return ones[num]
	elif (num < 20):
		return teens[num-10]
	elif (num < 1000):
		unit = num % 10
		ten = num/10 % 10
		hundreds = num/100
		return ones[hundreds] + " " + ("hundred " if hundreds != 0 else "") + (" and " if hundreds != 0 and (ten != 0 or unit != 0) else "") + (tens[ten] if ten >= 2 else "") + ("-" if ten >=2 and unit !=0 else "") + (teens[unit] if ten ==1 else ones[unit])
	else:
		return "one thousand"


total = 0
for i in range(1,1001):
	length = len(to_words(i).replace(" ", "").replace("-", ""))
	total+= length


print 
