qb = input("Enter QB name:")

try:
	comp = int(input("Enter number of completions:"))
	att = int(input("Enter number of attempts:"))
	yard = int(input("Enter number of passing yards:"))
	td = int(input("Enter number of passing TDs:"))
	inter = int(input("Enter number of interceptions:"))

except TypeError:
	print("Input for Completions, Attempts, Yards, Touchdowns and Interceptions must all be of type Int. Exiting Program")
	quit()

except ValueError:
	print("You must enter a valid integer. Exiting program")
	quit()

if (comp > att):
	print("The number of completions cannot exceed the number of attempts. Exiting program")
	quit()
if (td > comp):
	print("The number of touchdowns cannot exceed the number of completions. Exiting program")
	quit()
if (inter > att):
	print("The number of interceptions cannot exceed the number of attempts.Exiting program")
	quit()


def rating():
	a = float((comp/att - .3) * 5)
	b = float((yard/att - 3) * .25)
	c = float((td/att) * 20)
	d = float(2.375 - (inter/att) * .25)

	myList=[]
	newList=[]
	myList.append(a)
	myList.append(b)
	myList.append(c)
	myList.append(d)

	for i in myList:
		if i > 2.375:
			i = 2.375
			newList.append(i)
		else:
			newList.append(i)

	newA = newList[0]
	newB = newList[1]
	newC = newList[2]
	newD = newList[3]

	rate = float(((newA + newB + newC + newD) / 6) * 100)
	roundRate = float(round(rate, 1))
	return roundRate

"""
	if a > 2.375:
		a = 2.375

	if b > 2.375:
		b = 2.375

	if c > 2.375:
		c =2.375

	if d > 2.375:
		d = 2.375	
"""
print (qb, "has a passer rating of", rating())
