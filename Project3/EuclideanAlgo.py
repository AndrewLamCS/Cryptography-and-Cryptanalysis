#Euclidean Algorithm - used to evaluate a 
#greatest common denominator between two arguments

def EuclideanAlgorithm(a,b):
    while b:    #Loop as long as b not equal to 0
        a, b = b, a % b #Update a with the value of b
                        #Update b with the remainder of a divided by b
    return a            #Return GCD, which is stored in a after loop completion

def main():
    print("GCD is: ", EuclideanAlgorithm(76,51))    #Test case CH6_7    GCD = 1

main()
