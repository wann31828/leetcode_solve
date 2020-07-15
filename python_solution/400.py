'''
400. Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 
4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
... is a 0, which is part of the number 10.

'''

#total digits : 1*9 +2*90 + 3*900 + 4*9000 ....
def findNthDigit(n):
    digit =1
    while(n > 0):
        n -= digit* pow(10,digit-1) * 9
        digit += 1

    digit -= 1
    n += digit * 9*pow(10,digit-1)

    if digit == 1:
        target , location = int(n/digit),  n%digit
    else :
        location =  n%digit
        if n<= digit:
            target = pow(10,digit-1)
        else:
            if(location == 0):
                target = pow(10,digit-1) + int(n/digit) -1
            else:
                target = pow(10,digit-1) + int(n/digit)

    if(location == 0):
        return int(str(target)[-1])
    else:
        return int(str(target)[location-1])
