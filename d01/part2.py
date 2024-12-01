# part 2 of d02

i = 0
similarityScore = 0

column_a = []
column_b = []
	
#read txt and splits into lists
f = open('text1.txt', "r")

for line in f:
	number = line.split()
	column_a.append(int(number[0]))
	column_b.append(int(number[1]))

#calculate similarity score by comparing value of a number in column a and iterating through column b
for a in column_a:
	for b in column_b:
		if a == b:
			i += 1

	similarityScore = a * i + similarityScore
	#print(a, i, similarityScore, sep=", ")
	i = 0
print("Final Similarity Score =", similarityScore)

