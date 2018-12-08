'''
You are given a string with alpha-numeric characters and parentheses. Your goal is to return a string with balanced
parentheses by removing the fewest characters possible. Note that you cannot add anything to the string.

Examples
() -> ()
b(a)r) -> b(a)r
)( -> empty string
((((( -> empty string
)(())( -> (())

Note that there can be multiple correct results per input

(()()( -> ()() OR (())
(())()) -> (()()) OR (())()
'''
# FIRST ATTEMPT WITH A STACK
# def balance_parens(string):
#     string = list(string)
#     stack = []
#
#     for i in range(len(string)):
#         if string[i] == '(':
#             stack.append(i)
#         elif string[i] == ')':
#             if len(stack) > 0:
#                 stack.pop()
#             else:
#                 string[i] = '#'
#
#     for index in stack:
#         string[index] = '#'
#
#     return ''.join(string).replace('#', '')

def delete_invalid_parenthesis(string):
    string = list(string)
    left = 0
    right = len(string)-1

    while left < right:
        while left <= right and string[left]!='(':
            if string[left]==')':
                string[left]='#'
            left+=1
        while left <= right and string[right]!=')':
            if string[right]=='(':
                string[right]='#'
            right-=1
        left +=1
        right-=1
    if left == right and string[left] in ['(', ')']:
        string[left] = '#'
    return ''.join(string).replace('#', '')

# parens = "()" # ()
# parens = ")(" # empty string
# parens = "())" # ()
# parens = "(()()("  # ()() or (())
parens = "b(a)r)" # b(a)r
# parens = "((((((" # empty string
# parens = "))))))" # empty string
# parens = '((((((((()))))))))' # '((((((((()))))))))'
# parens = "foobar" # foobar
print(delete_invalid_parenthesis(parens))
