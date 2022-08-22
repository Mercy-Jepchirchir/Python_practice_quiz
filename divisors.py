#A divisor is a number that divides into another without a remainder.
def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  return sum([i for i in range(1, n)
                if n % i == 0])
 #A divisor, also known as a factor, is an integer m which evenly divides n.               
print(sum_divisors(0))
#0
print(sum_divisors(2)) # Should sum of 1 : 1

print(sum_divisors(36)) #1+2+3+4+6+9+12+18

print(sum_divisors(102))