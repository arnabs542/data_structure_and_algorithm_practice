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


