from copy import deepcopy
'''
Problem Statement:
You are given a string s, containing only numerical characters ('0' - '9'). You are also given a non-negative number 
target. You have to put between each pair of numerical characters, one of ("", "*", "+") operators such that the 
expression you get will evaluate to the target value.

Putting "" (an empty string) operator between two numerical characters means, that the they are joined (e.g. 1""2 = 12).
 Also the join can be extended further (e.g. 1""2""3 = 123).

Precedence of the operators matters. In higher to lower precedence:
Join ("") > Multiplication ("*") > Addition ("+")

Input Format:
There are two arguments.
1) String s.
2) Long integer target. 

Output Format:
Return array of strings containing ALL possible strings that evaluate to the target value. 
You need not to worry about the order of strings in your output array. Like for s = "22" and target = 4, 
arrays ["2+2", "2*2"] and ["2*2", "2+2"] both will be accepted.  

Any string in the returned array should not contain any spaces. In the above example string "2+2" is expected, other 
strings containing any space like " 2+2", "2 + 2", "2 +2" etc. will give wrong answer. 

Constraints:
1 <= |s| <= 13
s only contains numerical characters ('0' - '9').
0 <= target < 10^13
You have to return ALL possible strings that evaluate to target value.

Sample Input:
s = "222"
target = 24

Sample Output:
["22+2", "2+22"]

Explanation:
1) 22 + 2 = 24 (Here, we put "" operator between the first two characters and then put "+" operator between the 
last two characters.)

2) 2 + 22 = 24 (Here, we put "+" operator between the first two characters and then put "" operator between the 
last two characters.)
'''

def evaluate(expression):
    atomlist = []
    for atom in expression.split():
        if "+" not in atom and "*" not in atom:
            atomlist.append(int(atom))
        else:
            atomlist.append(atom)
    #print atomlist
    evalstring = ""
    for atom in atomlist:
        evalstring+=str(atom)
    #print evalstring
    num = eval(evalstring)
    return num

# evaluate('0022 + 022 * 04')

def generate_all_expressions_rec(soFar, rest, target, results):
    if len(rest) == 0:
        if evaluate(''.join(soFar))==target:
            soFar = ''.join(soFar).replace(' ', '')
            results.append(''.join(soFar))
        return
    joint = deepcopy(soFar)
    remaining = deepcopy(rest)
    num = remaining[0]
    del remaining[0]
    joint.append(num)
    generate_all_expressions_rec(joint, deepcopy(remaining), target, results)

    plus = deepcopy(soFar)
    plus.append(' +')
    plus.append(' ' + num)
    generate_all_expressions_rec(plus, deepcopy(remaining), target, results)

    multiply = deepcopy(soFar)
    multiply.append(' *')
    multiply.append(' ' + num)
    generate_all_expressions_rec(multiply, deepcopy(remaining), target, results)


def generate_all_expressions(string, target):
    result = []
    generate_all_expressions_rec(list(string[0]), list(string[1:]), target, result)
    return result

# print(generate_all_expressions('050505', 5))
# print(generate_all_expressions('555', 555))
# print(generate_all_expressions('0000000001', 0))
# print(len(generate_all_expressions('0000000001', 0)))
print(len(generate_all_expressions('5957515355821', 30210504)))
