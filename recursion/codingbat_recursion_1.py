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

'''
Given base and n that are both 1 or more, compute recursively (no loops) the value of base
to the n power, so powerN(3, 2) is 9 (3 squared).

powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
'''
def powerN(base, n):
    if n == 1:
        return base
    return base*powerN(base, n-1)
# print(powerN(3, 1))
# print(powerN(3, 2))
# print(powerN(3, 3))


'''
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''
def countX(string):
    if len(string) <= 0:
        return 0
    if string[-1] == 'x':
        return 1+countX(string[:-1])
    return countX(string[:-1])

# print(countX("xxhixx"))
# print(countX("xhixhix"))
# print(countX("hi"))

'''
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
'''
def countHi(string):
    if len(string) <= 1:
        return 0
    if string[:2] == 'hi':
        return 1+countHi(string[1:])
    return countHi(string[1:])

# print(countHi("xxhixx"))
# print(countHi("xhixhix"))
# print(countHi("hi"))
# print(countHi("h"))

'''
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars 
have been changed to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
'''
def changeXY(string):
    if len(string) <= 0:
        return ""
    char = string[0]
    if char=='x':
        char = 'y'
    if len(string) == 1:
        return char
    return char+changeXY(string[1:])

# print(changeXY("codex"))
# print(changeXY("xxhixx"))
# print(changeXY("xhixhix"))

'''
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
'''
def changePi(string):
    if len(string) <= 0:
        return ""
    if len(string) == 1:
        return string
    if len(string) == 2:
        if string[:2] == "pi":
            return "3.14"
        return string
    if len(string) > 2:
        if string[:2] == "pi":
            return "3.14"+changePi(string[2:])
        return changePi(string[1:])

# print(changePi("xpix"))
# print(changePi("pipi"))
# print(changePi("pip"))

'''
Given a string, compute recursively a new string where all the 'x' chars have been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
'''
def noX(string):
    if len(string) <= 0:
        return ""
    if len(string) == 1:
        if string[0] == 'x':
            return ""
        return string
    if string[0]=="x":
        return noX(string[1:])
    return string[0] + noX(string[1:])

# print(noX("xaxb"))
# print(noX("abc"))
# print(noX("xx"))

'''
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only 
the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the 
array. The initial call will pass in index as 0.

array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
'''
def array6(arr, index):
    if index >= len(arr):
        return False
    if arr[index]==6:
        return True
    return array6(arr, index+1)

# print(array6([1, 6, 4], 0))
# print(array6([1, 4], 0))
# print(array6([6], 0))

'''
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the
convention of considering only the part of the array that begins at the given index. In this way, a recursive call can 
pass index+1 to move down the array. The initial call will pass in index as 0.

array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
'''
def array11(arr, index):
    if index >= len(arr):
        return 0
    if arr[index]==11:
        return 1+array11(arr, index+1)
    return array11(arr, index+1)

# print(array11([1, 2, 11], 0))
# print(array11([11, 11], 0))
# print(array11([1, 2, 3, 4], 0))

'''
Given an array of ints, compute recursively if the array contains somewhere a value followed immediately in the array 
by that value times 10. We'll use the convention of considering only the part of the array that begins at the given
index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
'''
def array220(arr, index):
    if index+1 >= len(arr):
        return False
    if arr[index]*10 == arr[index+1]:
        return True
    return array220(arr, index+1)

# print(array220([1, 2, 20], 0))
# print(array220([3, 30], 0))
# print(array220([3], 0))

'''
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
'''
def allStar(string):
    if len(string) <= 1:
        return string
    if len(string) == 2:
        return string[0]+"*"+string[1]
    return string[0]+"*"+allStar(string[1:])

# print(allStar("hello"))
# print(allStar("abc"))
# print(allStar("ab"))

'''
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are 
separated from each other by a "*".

pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
'''
def pairStar(string):
    if len(string) <= 1:
        return string
    if len(string) == 2:
        if string[0] == string[1]:
            return string[0]+"*"+string[1]
        return string
    if string[0]==string[1]:
        return string[0]+"*"+pairStar(string[1:])
    return string[0]+pairStar(string[1:])

# print(pairStar("hello"))
# print(pairStar("xxyy"))
# print(pairStar("aaaa"))

'''
Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of 
the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
'''
def endX(string):
    if len(string) <= 1:
        return string
    if string[0]=='x':
        return endX(string[1:])+'x'
    return string[0]+endX(string[1:])

# print(endX("xxre"))
# print(endX("xxhixx"))
# print(endX("xhixhix"))

'''
We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. 
Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in 
the given string.

countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
'''
def countPairs(string):
    if len(string)<3:
        return 0
    if string[0]==string[2]:
        return 1+countPairs(string[1:])
    return countPairs(string[1:])

# print(countPairs("axa"))
# print(countPairs("axax"))
# print(countPairs("axbx"))

'''
Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
countAbc("ababc") → 2
'''
def countAbc(string):
    if len(string)<3:
        return 0
    if string[:2]=='ab' and (string[2]=='a' or string[2]=='c'):
        return 1+countAbc(string[2:])
    return countAbc(string[1:])

# print(countAbc("abc"))
# print(countAbc("abcxxabc"))
# print(countAbc("abaxxaba"))
# print(countAbc("ababc"))

'''
Given a string, compute recursively (no loops) the number of "11" substrings in the string. 
The "11" substrings should not overlap.

count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
'''
def count11(string):
    if len(string)<2:
        return 0
    if string[:2]=='11':
        return 1+count11(string[2:])
    return count11(string[1:])

# print(count11("11abc11"))
# print(count11("abc11x11x11"))
# print(count11("111"))

'''
Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a 
single char. So "yyzzza" yields "yza".

stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
'''
def stringClean(string):
    if len(string) <= 1:
        return string
    if string[0]==string[1]:
        return stringClean(string[1:])
    return string[0]+stringClean(string[1:])

# print(stringClean("yyzzza"))
# print(stringClean("abbbcdd"))
# print(stringClean("Hello"))

'''
Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" 
that have an 'x' immedately before them.

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
'''
def countHi2(string):
    if len(string)<2:
        return 0
    if len(string)==2:
        if string=="hi":
            return 1
        return 0
    if string[0]=='x' and string[1:3]=='hi':
        return countHi2(string[2:])
    if string[:2]=='hi':
        return 1+countHi2(string[2:])
    return countHi2(string[1:])

# print(countHi2("ahixhi"))
# print(countHi2("ahibhi"))
# print(countHi2("xhixhi"))

'''
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the 
parenthesis and their contents, so "xyz(abc)123" yields "(abc)".

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
'''
def parenBit(string):
    if string[0]!='(':
        return parenBit(string[1:])
    if string[-1]!=')':
        return parenBit(string[:-1])
    return string

# print(parenBit("xyz(abc)123"))
# print(parenBit("x(hello)"))
# print(parenBit("(xy)1"))

'''
Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))".
Suggestion: check the first and last chars, and then recur on what's inside them.

nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
'''
def nestParen(parens):
    if len(parens)==0:
        return True
    if parens[0]=='(' and parens[-1]==')':
        return nestParen(parens[1:-1])
    return False

# print(nestParen("(())")) # True
# print(nestParen("((()))")) # True
# print(nestParen("(((x))")) # False
# print(nestParen("(((x")) # False
# print(nestParen("(((x)))")) # False

'''
Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, 
without the sub strings overlapping.

strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
'''
def strCount(string, sub):
    if len(string)<len(sub):
        return 0
    if string[0:len(sub)]==sub:
        return 1+strCount(string[len(sub):], sub)
    return strCount(string[1:], sub)

# print(strCount("catcowcat", "cat")) # 2
# print(strCount("catcowcat", "cow")) # 1
# print(strCount("catcowcat", "dog")) # 0
# print(strCount("ccc", "cc")) # 1 since we don't count overlaps

'''
Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string
somewhere, possibly with overlapping. N will be non-negative.


strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
strCopies("ccc", "c", 3) → true
strCopies("ccc", "cc", 2) → true
strCopies("ccc", "cc", 3) → false
'''

def strCopies(string, sub, copies):
    if len(string)<len(sub):
        return False
    if string[0:len(sub)]==sub:
        if copies-1 > 0:
            return strCopies(string[1:], sub, copies-1)
        return True
    return strCopies(string[1:], sub, copies)

# print(strCopies("catcowcat", "cat", 2)) # True
# print(strCopies("catcowcat", "cow", 2)) # False
# print(strCopies("catcowcat", "cow", 1)) # True
# print(strCopies("ccc", "c", 3)) # True
# print(strCopies("ccc", "cc", 2)) # True
# print(strCopies("ccc", "cc", 3)) # False

'''
Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub 
and return its length.

strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
'''
def strDist(string, sub):
    if len(string)<len(sub):
        return 0
    if string[0:len(sub)]!=sub:
        return strDist(string[1:], sub)
    if string[-3:]!=sub:
        return strDist(string[:-1], sub)
    return len(string)

# print(strDist("catcowcat", "cat"))
# print(strDist("catcowcat", "cow"))
# print(strDist("cccatcowcatxx", "cat"))
