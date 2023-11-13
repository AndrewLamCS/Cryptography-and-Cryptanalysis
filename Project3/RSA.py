#CSCI 360 - 99
#Andrew Lam 

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
        
#Extended Euclidean Algorithm - used to evaluate the GCD, s, and t values for two integers        
def ExtendedEuclideanAlgo(a,b):
    x, prev_x = 0, 1    #Initalize x and prev_x as 0 and 1, respectively
    y, prev_y = 1, 0    #Initalize y and prev_y as 1 and 0, respectively
    z, prev_z = b, a    #Initalize z and with b and prev_z with a

    while (z != 0): #Loop while z is not equal to 0
        q = prev_z // z #Continue integer division of prev_z by z and store it in q
        prev_z, z = z, prev_z - q * z   #Update prev_z and z using the EEA formula
        prev_x, x = x, prev_x - q * x   #Update prev_x and x            
        prev_y, y = y, prev_y - q * y   #Update prev_y and y
    return prev_z, prev_x, prev_y       #Return the GCD (prev_z), and coefficients (s is prev_x, t is prev_y)

#Compute modular inverse
def InverseModulus(a, m):
    gcd, x, y = ExtendedEuclideanAlgo(a,m)  #Calculate the GCD and coefficients using EEA
    if (gcd != 1):
        print("Modular inverse DOES NOT EXIST between", a,"and", m ) #If GCD is not 1, the modular inverse does not exist
    return (x % m + m) % m  #Return the modular inverse (x mod m)

#Square and Multiply algorithm to evaluate exponentiation
def powmod_sm(base, exp, mod):
    res = 1 #Initialize the result to 1

    while (exp > 0):  #Loop to perform modular exponentiation
        if (exp % 2 == 0):    #Check if exp is even
            base = (base * base) % mod     #SQUARE base and apply modulo mod
            exp //= 2             #Halve exp by integer division
        else:
            res = (res * base) % mod #Update result by MULTIPLYING base and apply modulo mod
            exp -= 1              #Decrement exp by 1
    return res              #Return final result

#Generate an RSA key pair
def GenerateKeyPair(num):
    p = primeNumGenerator(num)  #Generate random prime number p with num bits
    q = primeNumGenerator(num)  #Generate random prime number q with num bits

    while q == p:   #Check if q is equivalent to p. If so, generate q again
        q = primeNumGenerator(num)

    n = p * q   #Calculate the RSA modulus n by multiplying p and q
    EulerPhi = (p - 1) * (q - 1)    #Calculate Euler's totient function for n
    e = 12234231423412232232    #Choose specific value e as public exponent
    d = ExtendedEuclideanAlgo(e, EulerPhi)[1]   #Calculate the private exponent d using ExtendedEuclideanAlgorithm function
    dOfP = d % (p - 1)  #Calculate  d mod (p-1) for use in RSA decryption
    dOfQ = d % (q - 1)  #Calculate  d mod (q-1) for use in RSA decryption
    qInv = InverseModulus(q, p) #Calculate the modular inverse using InverseModulus function
    publicGen = (n, e)  #Create the public key as a tuple - immutable data structure
    privateGen = d  #Create the private key, d
    return publicGen, privateGen    #return public and private keys

#Encrypt a message using the public key
def RSA_Enc(msg, public_key):
    n, ENC = public_key     #Extract modulus n and public exponent, ENC from the public key
    print("\nEncryption of e: ", ENC)   #Print public exponent, ENC
    print("\nN:\n", n)  #Print modulus, n
    b = powmod_sm(msg, ENC, n)  #Encrypt the message, msg using powmod_sm function
    return b    #Return ciphertext

#Decrypt ciphertext using the private key
def RSA_Dec(cipher, private_key, n):
    DEC = private_key   #Extract the private exponent, DEC from the private key
    msg = powmod_sm(cipher, DEC, n) #Decrypt the ciphertext, cipher using powmod_sm function
    return msg  #Return the decrypted plaintext message

def main():

    public_key, private_key = GenerateKeyPair(1028) #Generate an RSA key pair with 1028-bit primes 
    e, num = public_key     #Extract the public exponent, e and modulus, num from the public key
    print("\nPublic Key:", num) #Print modulus, num of the public key
    msg = 7368467   #Define plaintext message, msg to be encrypted
    print("\nMessage:", msg)    #Print plaintext msg
    cipher = RSA_Enc(msg, public_key)   #Encrypt the plaintext, msg using the public key - obtain ciphertext
    decrypted = RSA_Dec(cipher, private_key, num)   #Decrypt the ciphertext, cipher using the private key and modulus - obtain decrypted message
    print("\nCipher:\n", cipher)    #Print ciphertext
    print("\nDecrypted Message:\n", msg)  #Print decrypted message


main()