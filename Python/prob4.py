"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def findPalindromebyString(num1, num2):
    result = int(num1 * num2)
    n = len(str(result))

    if n % 2 == 0 :  n = int(n / 2)
    else : n = int((n-1) / 2)

    success = False
    print(result)
    if (compareStrings(result,n) or hasThreeDigitFactors(result) == False):
        print(result)
        while (success == False):
            break
            result = result - 1
            if(compareStrings(result, n)):
                success = hasThreeDigitFactors(result)

    print (result)

def hasThreeDigitFactors(result):
    f1 = 100
    ret = False
    while f1 <= 999:
        if (result % f1 == 0):
            f2 = int(result % f1)
            print(result,f1,f2)
            if (isThreeDigits(f2)):
                ret = True
                print(f1,f2)
                break

        f1 += 1
        ret = False

    return ret

def isThreeDigits(num):
    return (len(str(num)) == 3)

def compareStrings(number, n):
    x = str(number)[0:n]
    y = str(number)[int(n*-1):][::-1]

    return (x == y)



# def findPalindromeInReverse(max):
#     success = False
#     while (!success):

#     result = 

findPalindromebyString(999,999)

