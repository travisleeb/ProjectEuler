"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#Using Prime Factorization method

def getLargestPrimeFactor(num):
    result = num
    factor = 2 #Since a Prime is divisible by 1, we start with 2

    #We loop until the largest factor is the result itself
    while (factor != result):
        if(result % factor == 0) : 
            result = result / factor
            factor = 2 #Reset back to 2
        else:
            factor += 1 #Go to next possible factor

    return int(result)

print("The largest prime for 600,851,475,143 is " + str(getLargestPrimeFactor(600851475143)))



#Python Lesson: str() and int() will convert values to String and Integer, respectively


        
