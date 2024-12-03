
import copy

def newcheckthisline(numberLine):
	length = len(numberLine)
	j = 0
	k = 0
	while j + 2 <= length and 1 <= (numberLine[j] - numberLine[j + 1]) <= 3:
		j += 1
	while k + 2 <= length and 1 <= (numberLine[k + 1] - numberLine[k]) <= 3:
		k += 1
	if j + 1 == length or k + 1 == length:
		return (1)
	return (0)

def isitsafe(numberLine, j, k):
	newnumberLine = copy.copy(numberLine)
#	print("CHECKING FOR SAFETY...")
	if j:
		newnumberLine.pop(j)
#		print("Checking removal of this number j", numberLine[j], "j is", j)
	else:
		newnumberLine.pop(k)
#		print("Checking removal of this number k", numberLine[k], "k is", k)
#	print("New number List:", newnumberLine)

	if newcheckthisline(newnumberLine):
#		print("CHECKED SAFE EDGE CASE")
		return (1)
	else:
#		print("ORIGINAL INDEX REMOVAL NOT SAFE, RETRY WITH NEXT NUMBER IF POSSIBLE")
		newnumberLine = copy.copy(numberLine)
#		print("Number list reverted to", newnumberLine)
#	print("j is", j, "k is", k, "length is", len(numberLine))
	if j == len(numberLine) - 1 or k == len(numberLine) - 1:
#		print("NO NEXT NUMBER...")
		return(0)
	if j:
		newnumberLine.pop(j + 1)
#		print("Checking removal of this number instead j + 1", numberLine[j + 1], "j + 1 is", j + 1)
	else:
		newnumberLine.pop(k + 1)
#		print("Checking removal of this number instead k + 1", numberLine[k + 1], "k + 1 is", k + 1)
	if newcheckthisline(newnumberLine):
#		print("NUMBER REMOVAL CHECKED TO BE SAFE")
		return (1)
	else:
#		print("NEXT NUMBER REMOVAL NOT SAFE, RETRY WITH PREVIOUS NUMBER IF POSSIBLE")
		newnumberLine = copy.copy(numberLine)
#		print("Number list reverted to", newnumberLine)
#	print("j is", j, "k is", k, "length is", len(numberLine))
	if j == 0 and k == 0:
#		print("NO PREVIOUS NUMBER...")
		return(0)
	if j:
		newnumberLine.pop(j - 1)
#		print("Checking removal of this number instead j - 1", numberLine[j - 1], "j - 1 is", j - 1)
	else:
		newnumberLine.pop(k - 1)
#		print("Checking removal of this number instead k - 1", numberLine[k - 1], "k - 1 is", k - 1)
	if newcheckthisline(newnumberLine):
#		print("NUMBER REMOVAL CHECKED TO BE SAFE")
		return (1)
	return (0)


def checkthisline(numberLine):
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
		return (1)
	elif isitsafe(numberLine, j, k):
		return (1)
	return (0)

def main():

	counter = 0
#	linecounter = 1
	f = open('txt.txt', "r")

	for line in f:
#		print("Line:", linecounter)
		numberLine = [int(num) for num in line.split()]
#		print("Original list is :", numberLine)
		if checkthisline(numberLine):
			counter += 1
#			print("line", linecounter, "SAFE. Counter now at", counter)
#		else:
#			print(linecounter, "NOT SAFE", "Number list is:", numberLine)
#		linecounter += 1
	
	print("Finally Tally:", counter)

if __name__ == "__main__":
	main()