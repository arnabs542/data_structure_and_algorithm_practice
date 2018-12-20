'''
Wildcard Pattern Matching
Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if wildcard pattern is
matched with text. The matching should cover the entire text (not partial text).

The wildcard pattern can include the characters ‘.’ and ‘*’
‘.’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

For example,
Text = "baaabab",
Pattern = “*****ba*****ab", output : true
Pattern = "baaa.ab", output : true
Pattern = "ba*a.", output : true
Pattern = "a*ab", output : false
'''

def match(string, pattern, s_i= 0, p_i=0):
    if s_i == len(string) and p_i == len(pattern): # both empty
        return True

    if p_i == len(pattern): # pattern empty
        return False
    if s_i == len(string): # string empty
        if pattern[p_i] != '*':
            return False
        return match(string, pattern, s_i, p_i+1)

    if pattern[p_i].isalpha() and string[s_i]==pattern[p_i]:
        return match(string, pattern, s_i+1, p_i+1)
    elif pattern[p_i] == '.' and match(string, pattern, s_i+1, p_i+1):
        return True
    elif pattern[p_i] == '*':
        if match(string, pattern, s_i, p_i+1):
            return True
        elif match(string, pattern, s_i+1, p_i):
            return True
        return False
    return False

string = list('abcde')
pattern = list('****')
print(match(string, pattern))
