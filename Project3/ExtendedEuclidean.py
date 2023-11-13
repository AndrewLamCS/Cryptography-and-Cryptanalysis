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

def main():
    print("EEA: ", ExtendedEuclideanAlgo(444,91)) #Test case CH6_9   GCD = 1, s = 33, t = -161
    print("Inverse Modulus:", InverseModulus(444,91))

main()