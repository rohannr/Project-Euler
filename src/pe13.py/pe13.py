

fp = open('numbersfile', 'r')


first_ten_digits = 0

for line in fp.readlines():
	first_ten_digits += int(line[:10])

print first_ten_digits
