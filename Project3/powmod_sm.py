#CSCI 360 - 99
#Andrew Lam

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

def main():
    print(powmod_sm(250,461,629))   #CH7_4 

main()
