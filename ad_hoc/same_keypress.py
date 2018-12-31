'''
Given two strings with either alpha-characters or *'s in it (where *'s represent a backspace)
determine if the two strings evaluate to the same thing
'''

def same_keypress(string_one, string_two):
    one_index = len(string_one)-1
    two_index = len(string_two)-1

    while one_index >= 0 and two_index >= 0:
        one_index = process_string(string_one, one_index)
        two_index = process_string(string_two, two_index)
        if string_one[one_index] != string_two[two_index]:
            return False
        one_index -= 1
        two_index -= 1

    if process_string(string_one, one_index) != process_string(string_two, two_index):
        return False
    return True

def process_string(string, index):
    '''
    returns the index of the next alpha character after accounting for backspaces (*)
    returns -1 if there are no valid characters left to process in the string
    example:
        s = 'aab*c**'
        process_string(s, len(s)-1) # returns 0 because the c, b, and a all get deleted

        s = 'aa****b**'
        process_string(s, len(s)-1) # returns -1
    '''
    backspace_count = 0
    while index >= 0:
        if string[index] == '*':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index

print(same_keypress('abcd**', 'ab')) # True
print(same_keypress('**abc', 'ab')) # False
print(same_keypress('**ab', 'ab')) # True
print(same_keypress('aa*b**c', 'c')) # True
print(same_keypress('abc***', '')) # True
print(same_keypress('', '')) # True
print(same_keypress('abc', 'abc')) # True
print(same_keypress('abc', 'cba')) # False
print(same_keypress('abc**', 'cba')) # False
print(same_keypress('a*b*c*', 'c*b*a*')) # True
print(same_keypress('a****bc*', 'b')) # True

