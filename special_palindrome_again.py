# A string is said to be a special palindromic string if either of two conditions is met:
#
# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special palindromic substring is any substring of a string which meets one of those criteria. Given a string,
# determine how many special palindromic substrings can be formed from it.
# For example, given the string s = mnonopoo, we have the following special palindromic substrings:
#   {m,n,o,n,o,p,o,o,non,ono,opo,oo}

def special_palindrome_again(s):
    words = dict()
    num_special_palindromes = 0
    word_length = 1

    while word_length <= len(s):
        for i in range(len(s)):
            word = s[i:i+word_length]
            if len(word) < word_length:
                break
            print(word)
            if word in words:
                num_special_palindromes += words[word]
            else:
                words[word] = is_special_palindrome(word)
                num_special_palindromes += words[word]
        word_length += 1
    return num_special_palindromes

def is_special_palindrome(word):
    if len(word) % 2 == 0:
        return all_letters_are_same(word)
    else:
        return all_letters_are_same(word) or all_but_middle_are_same(word)

def all_but_middle_are_same(word):
    mid_point = (len(word)//2)
    word = word[:mid_point] + word[mid_point+1:]
    return all_letters_are_same(word)

def all_letters_are_same(word):
    l = word[0]
    for letter in word:
        if letter != l:
            return 0
    return 1

# print(is_special_palindrome("aaaaa"))
print(special_palindrome_again("asasd"))
print(special_palindrome_again("abcbaba"))
print(special_palindrome_again("aaaa"))

