import math
import array

primes = array.array('i',[2])
primeString = str(primes[0])

def Solution(i):
    LoadPrimeString()
    return primeString
     
        
def LoadPrimeString():
    global primeString
    n = 3
    while len(primes) < 10000:
        isPrime = True
        for p in primes:
            if (n % p == 0):
                isPrime = False
                break
         
        if (isPrime):
            primes.append(n)
            primeString += str(n)
        n += 1

print(Solution(3))