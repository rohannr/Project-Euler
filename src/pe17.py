import math

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

oneseq = list(enumerate(ones, start=1))
tenseq = list(enumerate(tens start = 10))


def to_words(num): 
	if num <= 10:
		return ones[num -1]
	else if num <=20
		return tens[num-11]

total = 0;
for i in range(1, 10001):
	total += to_words(i)



