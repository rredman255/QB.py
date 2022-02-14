qb = input("Enter QB name:")

# Creating a "helper" function to loop through each integer input variable from user to validate it is truely an int.
def userInput(strname) -> int:
	while True:
		try:
			num = int(input("Enter number of %s: " % strname))
			return num
			break
		except ValueError:
			print("Invalid")

# Creating a "helper" function to create the logic of must meet criteria
def rules(comp, att, td, inter):
	if (comp > att):
		print("The number of completions cannot exceed the number of attempts. Please re-enter these values")
		comp = userInput("completions")
		att = userInput("attempts")

	if (td > comp):
		print("The number of touchdowns cannot exceed the number of completions. Please re-enter these values")
		comp = userInput("completions")
		td = userInput("passing TDs")

	if (inter > att):
		print("The number of interceptions cannot exceed the number of attempts. Please re-enter these values")
		inter = userInput("interceptions")
		att = userInput("attempts")

# Assigning the variables by function. Sending the type of verbiage to function for user display.
att = userInput("attempts")
comp = userInput("completions")
td = userInput("passing TDs")
inter = userInput("interceptions")
yard = userInput("passing yards")

# Now that we validated all user input is in fact type integer we can verify it against our rules function.
rules(comp, att, td, inter)



def rating():
	a = float((comp/att - .3) * 5)
	b = float((yard/att - 3) * .25)
	c = float((td/att) * 20)
	d = float(2.375 - (inter/att) * .25)

	myList=[a, b, c, d]
	newList=[]

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
