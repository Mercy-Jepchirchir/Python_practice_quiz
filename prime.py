# #1. Write a function print all the prime factors of a number.
# #A prime number is a natural number greater than 1 
# # that has no positive divisors other than 1 and itself.

# To take input from the user
num = int(input("Enter a number: "))

def primeChecker(): 
# prime numbers are greater than 1
    if num > 1:    
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        
        else:
            print(num,"is a prime number")       
# if input number is less than
# or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
        
primeChecker()