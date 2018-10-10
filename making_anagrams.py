# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# find the minimum number of character deletions required to make string 'a' an anagram of string 'b'
# Problems I had with this problem...
#    I wasn't iterating over a COPY of the list while I was removing errors and it left a difficult bug to find.

def make_anagram(a, b):
    a = list(a)
    b = list(b)

    for letter in a[:]:
        if letter in b:
            a.remove(letter)
            b.remove(letter)


    for letter in b[:]:
        if letter in a:
            a.remove(letter)
            b.remove(letter)

    return len(a)+len(b)

print(make_anagram("aaa","aaa"))
print(make_anagram("cde","abc"))
print(make_anagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
print(make_anagram("bugexikjevtubidpulaelsbcqlupwetzyzdvjphn","lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk"))
