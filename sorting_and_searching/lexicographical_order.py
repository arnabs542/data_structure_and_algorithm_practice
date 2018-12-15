'''
Problem Statement:
Given a string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS and VALUES
can repeat.
Your task is to find, for each unique key, the number of values with that key and the value with the highest
lexicographical order (also called alphabetical order and dictionary order).
(Have a look at the sample test cases for more clarity.)

Input Format:
You will be given one string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS
and VALUES can repeat.

Output Format:
Return a String array with an entry for each unique key. Each entry should contain key, number of values corresponding
to that key and value with the highest lexicographical order in the below format:

"<KEY>:<COUNT>,<HIGHEST_LEXICOGRAPHICAL_VALUE>"

Order of the output does not matter.

Constraints:
1 <= N <= 10^4
1 <= Length(KEYS) <= 256
1 <= Length(VALUES) <= 800

KEYS can repeat.
VALUES can repeat.
Keys and values will contain only small letters and numerics.

Sample Test Case:
Sample Input-1:
arr = [

  “key1 abcd”,

  “key2 zzz”,

  “key1 hello”,

  “key3 world”,

  "key1 hello"

]

Sample Output-1:
One possible output (you can return strings in any order):
[

  "key1:3,hello",

  "key2:1,zzz",

  "key3:1,world"

]

Sample Input-2:
arr = [

  “mark zuckerberg”,

  “tim cook”,

  “mark twain”

]

Sample Output-2:
One possible output (you can return strings in any order):
[

  "mark:2,zuckerberg",

  "tim:1,cook"

]
'''

def lexicographical_order(arr):
    if len(arr) == 0:
        return []
    result = []
    arr.sort()
    occurances = 1
    key,value = arr[0].split(' ')
    for i in range(1, len(arr)):
        k,v = arr[i].split(' ')
        if k == key:
            occurances += 1
            if v > value:
                value = v
        else:
            result.append('{}:{},{}'.format(key,occurances,value))
            occurances = 1
            key = k
            value = v
    result.append('{}:{},{}'.format(key,occurances,value))
    return result

arr =  [
  'key1 abcd',
  'key2 zzz',
  'key1 hello',
  'key3 world',
  'key1 hello'
]
print(lexicographical_order(arr))
arr = [
  'mark zuckerberg',
  'tim cook',
  'mark twain'
]
print(lexicographical_order(arr))
