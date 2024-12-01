# part 1 of d01


column_a = []
column_b = []

#read txt and splits into lists
f = open('text1.txt', "r")

for line in f:
	number = line.split()
	column_a.append(int(number[0]))
	column_b.append(int(number[1]))

#print("Column A:", column_a)
#print("Column B:", column_b)

#sorts the lists
list.sort(column_a)
list.sort(column_b)

#print("Column A:", column_a)
#print("Column B:", column_b)

absoluteDifferences = [abs(a - b) for a, b in zip(column_a, column_b)]

#print("absolute differences:", absoluteDifferences)

total = sum(absoluteDifferences)
print("total:", total)