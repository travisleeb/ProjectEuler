# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#for each number greater than 0 and lesser than 1000, add value to a total if number mod 3 or 5 equals 0.
def sumMultiples(max):
    index = 1
    total = 0
    while index < max:
        if index % 3 == 0 or index % 5 == 0:
            total = total + index
        index += 1
    print(total)

sumMultiples(1000)