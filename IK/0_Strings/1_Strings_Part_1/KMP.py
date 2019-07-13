'''
KMP
Problem Statement:
Given a text string t of length n and a pattern string p of length m, return start indices of all occurrences of p in t.

You have to answer q such queries.
Input/Output Format For The Function:
Input Format:
There are two arguments, t and p, denoting text string and pattern string respectively.
Output Format:
Return an array of integer pos[], where pos[i] is the start index of ith occurrence of p in t(0-based indexing).
Input/Output Format For The Custom Input:
Input Format:
The first line should contain a string t, denoting text string. Next line should contain an integer q, denoting no. of queries
 to be answered. In the next q lines, ith line contains a string pi, denoting pattern string for ith query, i=(1,2,...,q).

If
t = "Ourbusinessisourbusinessnoneofyourbusiness",
q = 3,
p in 1st query = "business",
p in 2nd query = "our",
p in 3rd query = "daisy",
then input should be:
Ourbusinessisourbusinessnoneofyourbusiness
3
business
our
daisy
Output Format:
Output will be printed in the sequence of queries asked. So, output of 1st query will be printed first, followed by output
 of 2nd query and so on, upto output of qth query.
For ith query, let say length of resultant array posi[] is leni.
Then, for ith query, there will be leni lines, where jth line of these leni lines contains a number posi[j], denoting number
 at jth index of posi.
So, in total, no. of lines will be = (len1 + len2 + len3 + … + lenq)
For input:
t = "Ourbusinessisourbusinessnoneofyourbusiness",
q = 3,
p in 1st query = "business",
p in 2nd query = "our",
p in 3rd query = "daisy",
output will be:
3
16
34
13
31
-1
Note:
If there is no occurrence of p in t, then return array pos of size one with pos[0] = -1.
If there are multiple occurrences of p in t, then return an array of start indices(sorted in increasing order).
Constraints:
1 <= q <= 5
1 <= n <= 2*10^5
1 <= m <= 2*10^5
t and p may contain lower case characters, upper case characters and numeric
 characters.
Sample Test Cases:
Sample Input 1:
t = "Ourbusinessisourbusinessnoneofyourbusiness"
q = 3 (t will be same for all 3 queries)
p in 1st query = "business"
p in 2nd query = "our"
p in 3rd query = "daisy"
Sample Output 1:
4
20
43
16
39
-1
Sample Input 2:
t = "IfyouthinkyouthinktoomuchthenyoumightbewrongThinkaboutit"
q = 4 (t will be same for all 4 queries)
p in 1st query = "aaaa"
p in 2nd query = "think"
p in 3rd query = "you"
p in 4th query = "be"
Sample Output 2:
-1
7
17
3
13
37
47
'''
import math
import os
import random
import re
import sys

# Complete the KMP function below.
def KMP(t, p):
    pass


if __name__ == "__main__":
    fptr = sys.stdout

    t = input()

    q = int(input())

    for _ in range(q):
        p = input()
        res = KMP(t, p)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

    fptr.close()

'''
Given a text string t of length n and a pattern string p of length m, return start indices of all occurrences of p in t.

A naive approach would be iterate over all possible substrings of text t having length m and compare it with pattern p.

As there are total (n-m+1) such substrings, each of length m, total no of comparisons would be O(n*m)
Time Complexity: O(n*m) for each query
Over all time complexity: O(q*n*m)
Auxiliary Space Used (excluding output space): O(1)
Space Complexity: O(n+m)
File: brute_force.java
An optimal approach would be as follows:
KMP (Knuth Morris Pratt) Pattern Matching Algorithm
The Naive pattern searching algorithm doesn’t work well in many cases as we slide the pattern by one and compare all
characters at each shift untill we find a mismatch.
Following are some examples.
t = "CCCCCCCCCCCCCCCCCCCCCCCCCCCCB"
p = "CCCCCB"
t = "CDCDCDECDCDCDECDCDCDE"
p = "CDCDCE"
The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after one or more matches), we already know
some of the characters are going to match in the text of next window. We take advantage of this information to avoid
matching the characters that we know will anyway match and thus avoiding redundant comparisons.
Example:
t = "CCCCCDCCCDC"
p = "CCCC"
We compare first window of text t with pattern p: (i.e. starting with 1st char of t)
t = "CCCCCDCCCDC"
p = "CCCC"  [Initial position]
We find a match. This is same as naive algorithm.
In the next step, we compare next window of t with p (i.e. starting with 2nd char of t)
t = "CCCCCDCCCDC"
p =  "CCCC" (Pattern shifted one position)
This is where KMP does optimization over naive. In this second window, we only compare 4th A of pattern with 4th
character of current window of text to decide whether current window matches or not. Since we know first three
characters will anyway match, we skipped matching first three characters.
How to know how many characters to be skipped?
To know this, we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be
skipped. To be precise, lps[i] = x shows that if first un-matched character is found at (i+1)th char of p, then for
next comparison, you can skip first x chars of p.
Preprocessing:
KMP algorithm preprocesses p[] and constructs an auxiliary array lps[] of size m (same as size of pattern) which is
used to skip characters while matching.
Name lps indicates longest proper prefix which is also suffix. A proper prefix is prefix with whole string not allowed.

For example, prefixes of “ABC” are “”, “A”, “AB” and “ABC”. Proper prefixes are “”, “A” and “AB”.
Suffixes of the string are “”, “C”, “BC” and “ABC”.
For each substring p[0..i] where i = 0 to m-1, lps[i] stores length of the maximum matching proper prefix which is
also a suffix of the substring pat[0..i].
lps[i] = the longest proper prefix of pat[0..i]
which is also a suffix of pat[0..i].
Note : lps[i] could also be defined as longest prefix which is also proper suffix. We need to use "proper" at atleast
one place to make sure that the whole string is not considered.
Examples of lps[] construction:
For the pattern “CCCC”,
lps[] is [0, 1, 2, 3]
For the pattern “CDEFG”,
lps[] is [0, 0, 0, 0, 0]
For the pCttern “CCDCCECCDCC”,
lps[] is [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
For the pCttern “CCCDCCCCCD”,
lps[] is [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
For the pCttern “CCCDCCC”,
lps[] is [0, 1, 2, 0, 1, 2, 3]
To build lps array, for lps[i], we keep track of the length of the longest proper prefix suffix value for the previous
index(let call it 'len'). We initialize lps[0] and len as 0. If p[len] and p[i] matches, we increment len by 1 and
assign the incremented value to lps[i]. If p[i] and p[len] do not match and len is not 0, we update len to lps[len-1].
See the implementation for better understanding.
We use a value from lps[] to decide the next characters to be matched. As mentioned before, the idea is to not match a
character that we know will anyway match.
How to use lps[] to know a number of characters to be skipped?
We start comparison of p[j] with j = 0 with characters of current window of text.
We keep matching characters t[i] and p[j] and keep incrementing i and j while pat[j] and txt[i] keep matching.
When we see a mismatch, we know that characters p[0,1,..,j-1] match with t[i-j,..,i-1]
(Note that j starts with 0 and increment it only when there is a match).
We also know that lps[j-1] is count of characters of p[0,1,..,j-1] that are both proper prefix and suffix.
From above two points, we can conclude that we do not need to match these lps[j-1] characters with txt[i-j,..,i-1]
because we know that these characters will anyway match.
See the implementation for better understanding.
Time Complexity: O(n) for each query
Over all time complexity: O(q*n)
Auxiliary Space Used (excluding output space): O(m)
Space Complexity: O(n+m)
File: optimal_solution.java
'''
'''
BRUTE FORCE
package KMP.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a text string t of length n and a pattern string p of length m, return start indices of all
 * occurrences of p
 * in t.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class brute_force {

    // -------------------- START ----------------------

    static int[] KMP(String t, String p) {
        // l will contain indices of text t where we find the occurrences of pattern p
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < t.length(); i++) {
            // In this loop, we are trying to find how many characters are matching between substring of
            // text t starting at i and pattern p. Let say no of character matched here is j. Then if j is
            // equal to length of p, then it can be said that there is an occurrence of p starting at
            // position
            // i of t.

            int j = 0;
            for (; j < p.length() && i + j < t.length(); j++) {
                if (t.charAt(i + j) != p.charAt(j)) {
                    break;
                }
            }

            // Checking if j, no of character matched, is equal to length of p or not.
            if (j == p.length()) {
                // p is occurring in t at index i
                l.add(i);
            }
        }

        // If no occurrence of p is found in t, then as asked in problem, return array having an element -1
        if (l.size() == 0) {
            l.add(-1);
        }
        int[] res = new int[l.size()];
        for (int i = 0; i < l.size(); i++) {
            res[i] = l.get(i);
        }
        return res;
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String t = br.readLine().trim();

        int q = Integer.parseInt(br.readLine().trim());
        while (q-- > 0) {
            String p = br.readLine().trim();
            int[] res = KMP(t, p);

            for (int i = 0; i < res.length; i++) {
                bufferedWriter.write(String.valueOf(res[i]));

                if (i != res.length - 1) {
                    bufferedWriter.write("\n");
                }
            }
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        br.close();
    }

}

/**
 * Time Complexity: O(n*m) for each query
 * Over all time complexity: O(q*n*m)
 * Auxiliary Space Used (excluding output space): O(1)
 * Space Complexity: O(n+m)
 */
'''
'''
package KMP.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a text string t of length n and a pattern string p of length m, return start indices of all
 * occurrences of p
 * in t.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class optimal_solution {

    // -------------------- START ----------------------

    public static int[] KMP(String t, String p) {
        if (t.length() < p.length()) {
            return new int[]{-1};
        }
        List<Integer> l = new ArrayList<>();

        // For each substring p[0..i] where i = 0 to m-1, lps[i] stores length of the maximum matching
        // proper prefix which is
        // also a suffix of the substring pat[0..i]. A proper prefix is prefix with whole string not allowed.

        int[] lps = getLPSArray(p);

        // We use a value from lps[] to decide the next characters to be matched. The idea is to not match
        // a character
        // that we know will anyway match.
        int ti = 0, pi = 0;
        while (ti < t.length() && pi < p.length()) {
            if (t.charAt(ti) == p.charAt(pi)) {
                ti++;
                pi++;

                // If pi is equal to length of p, then it can be said that there is an occurrence of p
                // starting at
                // position ti-pi, as we know that pi starts with 0 and get incremented only when there is
                // a match
                if (pi == p.length()) {
                    l.add(ti - pi);
                    pi = lps[pi - 1];
                }
            } else {
                // When we see a mismatch, we know that characters p[0,1,..,pi-1] match with t[ti-pi,..,ti-1]
                // We also know that lps[j-1] is count of characters of p[0,1,..,j-1] that are both proper
                // prefix and
                // suffix. From above two points, we can conclude that we do not need to match these
                // lps[pi-1]
                // characters with txt[ti-pi,..,ti-1] because we know that these characters will anyway
                // match.
                if (pi > 0) {
                    pi = lps[pi - 1];
                } else {
                    // If mismatch on first character of p
                    ti++;
                }
            }
        }
        // If no occurrence of p is found in t, then as asked in problem, return array having an element -1
        if (l.size() == 0) {
            l.add(-1);
        }
        int[] res = new int[l.size()];
        for (int i = 0; i < l.size(); i++) {
            res[i] = l.get(i);
        }
        return res;
    }

    public static int[] getLPSArray(String p) {
        // To build lps array, for lps[i], we keep track of the length of the longest proper prefix suffix
        // value for the previous
        // index.
        int[] lps = new int[p.length()];
        // We initialize lps[0] and len as 0
        lps[0] = 0;
        int len = 0;
        for (int i = 1; i < lps.length; ) {
            if (p.charAt(len) == p.charAt(i)) {
                // If p[len] and p[i] matches, we increment len by 1 and assign the incremented value to
                // lps[i]
                len++;
                lps[i] = len;
                i++;
            } else {
                // If p[i] and p[len] do not match and len is not 0, we update len to lps[len-1] if len>0
                if (len > 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String t = br.readLine().trim();

        int q = Integer.parseInt(br.readLine().trim());
        while (q-- > 0) {
            String p = br.readLine().trim();
            int[] res = KMP(t, p);

            for (int i = 0; i < res.length; i++) {
                bufferedWriter.write(String.valueOf(res[i]));

                if (i != res.length - 1) {
                    bufferedWriter.write("\n");
                }
            }
            bufferedWriter.newLine();
//            bufferedWriter.write("\n");
        }

        bufferedWriter.close();

        br.close();
    }

}

/**
 * Time Complexity: O(n) for each query
 * Over all time complexity: O(q*n)
 * Auxiliary Space Used (excluding output space): O(m)
 * Space Complexity: O(n+m)
 */
'''

