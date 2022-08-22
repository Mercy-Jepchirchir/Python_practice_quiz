#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
#An additional requirement is that the result is not to exceed 25, which is done with the break statement.
#Fill in the blanks to complete the function to satisfy these conditions
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	start = 1
	# Only want to loop through to 5
	while start <= 5:
		result =  number*start
		# What is the additional condition to exit out of the loop?
		if result>25 :
			break
		print(str(number) + "x" + str(start) + "=" + str(result))
		# Increment the variable for the loop
		start += 1

multiplication_table(3) # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5) # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	# Should print: 8x1=8 8x2=16 8x3=24
multiplication_table(9) #should print: 9x1 =9 9x2=18