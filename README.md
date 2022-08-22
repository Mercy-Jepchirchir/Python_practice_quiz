#Author
Mercy Jepchirchir Kemboi

#Questions
##returns the sum of all the divisors of a number, without including it.
-A divisor is a number that divides into another without a remainder.
-the first approach is to return the sum of all divisors of n, not including n
      def sum_divisors(n):
      ##Loop through the range
      return sum([i for i in range(1, n)
                if n % i == 0])

##Return the sum of all divisors of n, not including n
    print(sum_divisors(36)) #1+2+3+4+6+9+12+18

#The multiplication_table function prints the anycodings_python results of a number passed to it multiplied anycodings_python by 1 through 5
##An additional requirement is that the result is not to exceed 25, which is done with the break statement.
       
        Initialize the starting
        start = 1
        ##loop through
        while start <= 5:
		result =  number*start
		if result>25 :
			break
		print(str(number) + "x" + str(start) + "=" + str(result))
		## Increment the variable for the loop
		start += 1