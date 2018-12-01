def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

# print(factorial(10))

def bunnyEars(bunnies):
    if bunnies==0:
        return 0
    if bunnies==1:
        return 2
    return 2+bunnyEars(bunnies-1)

# print(bunnyEars(5))

def fibonacci(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(7))

def bunnyEars2(bunnies):
    if bunnies==0:
        return 0
    if bunnies==1:
        return 2
    if bunnies%2==0:
        return 3+bunnyEars2(bunnies-1)
    return 2+bunnyEars2(bunnies-1)

# should be 25
# print(bunnyEars2(10))

def triangle(blocks):
    if blocks==0:
        return 0
    if blocks==1:
        return 1
    return blocks + triangle(blocks-1)

# should be 28
# print(triangle(7))

def sumDigits(n):
    if n == 0:
        return 0
    return (n%10)+sumDigits(n//10)

# should be 21
# print(sumDigits(123456))

def count7(num):
    if num == 0:
        return 0
    if num%10 == 7:
        return 1 + count7(num//10)
    return count7(num//10)

# should be 3
# print(count7(727457))

def count8(num):
    if num==0:
        return 0
    if num%10==8 and (num//10)%10==8:
        return 2+count8(num//10)
    if num%10==8:
        return 1+count8(num//10)
    return 0+count8(num//10)

# should be 4
print(count8(8818))


