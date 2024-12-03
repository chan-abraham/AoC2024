counter = 0
#linenumber = 1

#read txt and splits into lists
f = open('txt.txt', "r")

for line in f:
	numberLine = [int(num) for num in line.split()]
#	print("line number is", linenumber)
#	linenumber += 1
#	print ("numberLine is", numberLine)
	length = len(numberLine)
	j = 0
	k = 0
	#this loop condition needs to be at "j" or "k" + 2 because we are looking at two numbers at the same time
	while j + 2 <= length and 1 <= (numberLine[j] - numberLine[j + 1]) <= 3:
		j += 1
	while k + 2 <= length and 1 <= (numberLine[k + 1] - numberLine[k]) <= 3:
		k += 1
	#this counter returns to +1. because upon doing through the entire list, the index + 1 shuold equal the strength length
	if j + 1 == length or k + 1 == length:
		counter += 1
#	print("j is", j)
#	print("k is", k)
#	print("length is", length)
#	print("counter is at:", counter)
print("Finally Tally:", counter)

