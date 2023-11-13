import random   #enables random function for use within algorithms

#Miller-Rabin Test - Primality test algorithm determines if argument is prime or not
def MillerRabinTest(num):
    if num == 3 or (num > 1 and num < 3):   #Check if num is equal to 3 or between 1 and 3 (inclusive) - PRIME
        return True
    if (num % 2 == 0) or (num < 2): #Check if number is even or less than 2 - NOT PRIME
        return False
    
    #Initialize r and s for finding an odd number s and power of 2 r such that num - 1 = (2^r) * s
    r = 0
    s = num - 1

    #Calculate s and r by dividing s by 2 repeatedly until it becomes odd, and incrementing r
    while (s % 2 == 0):
        s //= 2
        r += 1
    
    #Repeat the primality test for 10 random bases
    for i in range(10):
        a = random.randint(2, num - 2)  #Generate a random int a between 2 and num - 2
        b = pow(a, s, num)  #Compute b as (a^s) % num using modular exponentiation
        
        if (b == num - 1) or (b ==1):   #Check if b is congruent to num - 1 or 1
            continue

        for j in range(r - 1):  #Perform r-1 additional modular exponentiations of b
            b = pow(b, 2, num)

            if (b == num - 1):  #If b becomes congruent ot num - 1, exit the loop. Otherwise, return False
                break
            else:
                return False
            
    return True #If the number has passed all tests for different random bases, 
                #return True (indicates that it is likely prime)

#Randomly generates prime number
def primeNumGenerator(n):
    while True: #Loop generates numbers until a prime number is found
        prime = random.randint(2**(n-1), 2**n - 1)  #Generate a random integer 'prime' between 2^(n-1) and 2^n - 1
        if MillerRabinTest(prime) == True:  #Check if 'prime' is prime using the Miller-Rabin Test
            return prime    #If the number is determined to be prime, return it

def main():
    print(MillerRabinTest(2665)) #CH7_9  num = 2665

main()