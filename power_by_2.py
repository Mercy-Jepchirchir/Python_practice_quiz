#function that determines if a parameter is a power of 2
def is_power_of_two(n): 
    if n  == 0: 
        return False 
#checking if number is divisible by 2 without a remeinder
    while n % 2 == 0: 
        n = n / 2 
#If after dividing by two the number is 1, it's a power of two
    return n == 1 

print(is_power_of_two(4))
print(is_power_of_two(0))
print(is_power_of_two(5))