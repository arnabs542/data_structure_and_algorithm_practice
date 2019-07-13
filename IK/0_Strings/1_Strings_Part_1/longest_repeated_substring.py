'''
Longest Repeated Substring
Problem Statement:
Given a string inputStr of length n, find the longest repeated substring in it.
- Repeated is occurring more than once. It doesn't matter how many times it occurs as far as it occurs more than once.
- If there are multiple such substrings of the same size, then return any one.
- If there are no repeated substrings, then return an empty string.
Input/Output Format For The Function:
Input Format:
There is only one argument inputStr, denoting input string.
Output Format:
Return a string lrs, denoting longest repeated substring.
Input/Output Format For The Custom Input:
Input Format:
There should be only one line, containing inputStr, denoting input string.
If inputStr = “efabcdhefhabcdiefi”, then input should be:
efabcdhefhabcdiefi
Output Format:
There will be only one line, containing a string lrs, denoting longest repeated substring.
For input inputStr = “efabcdhefhabcdiefi”, output will be:
abcd
Constraints:
2 <= n <= 2*10^5
inputStr may contain only lowercase characters a-z.
Sample Test Cases:
Sample Input 1:
aaaa
Sample Output 1:
aaa
Explanation 1:
aaa is the longest substring which is repeated in aaaa, starting at position 0 and starting at position 1.
Sample Input 2:
efabcdhefhabcdiefi
Sample Output 2:
abcd
Explanation 2:
abcd repeats twice and ef repeats thrice. But as problems asks for longest repeated substring, abcd would be correct result.

Sample Input 3:
abcdefghi
Sample Output 3:
“”
(Empty string in output)
Explanation 3:
As there are no repeated substring in abcdefghi, empty string "" would be returned.
NOTE:
This is purely an exercise in building a Suffix Tree.
Suffix trees are difficult. You'd probably wonder if they really ask those in an interview.
They are in-fact, are rarely asked, which is why we don't cover it in the class. But we've seen them at FB and Uber. In
 all occasions, it's been asked as a follow up question. Once you code up an N^2 algorithm for the problem on hand, there
 are a few minutes left, in which time, the interviewer would wonder if you know of Suffix trees. It is NEVER asked to implement
 one in an interview. That's stupid. If at that time, you do know of suffix trees, then you have a chance to convert that
 interviewer from a 3 (good) to a 4 (advocate). It suggests you have taken a keen interest in your prep work and by extension,
 in general CS.
Another reason we include it in the course: It's possibly one of the hardest data structures. Once you have a handle on
 it, a lot of other things will look easy ;-)
Doing difficult problems like these also has a strong ancillary benefit: it helps you indirectly interview your interviewer/company.
 You want to work for a team that challenges you; not the team that gives you a free pass.
i.e. Don't skimp on it. Take it head on - there are clear benefits.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'getLongestRepeatedSubstring' function below.
#
def getLongestRepeatedSubstring(inputStr):
    pass


if __name__ == '__main__':
    inputStr = input()
    fptr = sys.stdout
    result = getLongestRepeatedSubstring(inputStr)
    fptr.write(result + '\n')
    fptr.close()



'''
Given a string str of length n, find the longest repeated substring in it.
Naive approach would be as follows:
Iterating over all possible non empty substrings, find the no. of occurrences of each substring in inputStr. The longest
 length substring having no. of occurrences greater than 1 is the required substring.
As there are total O(n^2) substrings, and for each substring, we are computing its no. of occurrences in O(n^2), time complexity
 of this approach would be O(n^4)
Time complexity: O(n^4)
Auxiliary Space Used: O(n)
Space Complexity: O(n)
File: brute_force.java
To find the no. of occurrences of substring in inputStr here, we can use any linear order pattern matching algorithm, for
 example KMP. Then, we will be able to compute no. of occurrences for each possible substring in O(n) time complexity. Time
 complexity of the above mentioned approach using this optimization will be O(n^3).
(
Notations:
- lrs => Longest Repeated Substring
- lrslen => length of Longest Repeated Substring
- ith suffix of string str => substring starting at index i and ending at end of string
- lcp => longest common prefix
)
Better approach would be as follows:
Let's say we have lrs of length lrslen, which starts at ith index and jth index of inputStr. That means longest matching
 prefix of ith suffix and jth suffix is lrs. As it is lrs, no other pair of distinct suffixes has longer matching prefix.

So, our problem boils down to finding the length of longest matching prefix for all pair of distinct suffixes and the pair
 (xth suffix, yth suffix) with largest length of lcp will lead to the solution.
This is a dynamic programming problem.
Let say lcp[i][j] denotes longest common prefix for a pair of ith suffix and jth suffix. Then,
if inputStr[i] == inputStr[j]
lcp[i][j] = 1 + lcp[i+1][j+1]
else
lcp[i][j] = 0
And lrslen = max(lcp[i][j]), where i!=j, 0 <= i,j <= n-1
And let say, (x,y) is a value of (i,j) for which lrslen = lcp[i][j], then inputStr.substring(x,x+lrslen-1) is the required
 lrs.
As we are finding lcp, in O(1), for all O(n^2) pair of suffixes, time complexity will be O(n^2) and as we need to store
 entire lcp array of size n*n, space complexity will be O(n^2).
Space complexity can be optimized to O(n) with a better implementation of this approach. (Exercise for reader :D )
Time complexity: O(n^2)
Auxiliary Space Used: O(n^2)
Space Complexity: O(n^2)
File: other_solution.java
It can be further optimized using Suffix Tree Data Structure.
Please read about what suffix tree is and its construction from:
https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-1/

(
    - Path length of node here means no. of characters in path from root to this node, unless explicitly mentioned other
    meaning
    - Just to be clear, root node is not considered as an internal node
    - ith suffix is a suffix having start index i
    - ith suffix has suffixIndex = i
    - Each node in Suffix Tree constructed here has fields: begin, end, depth, parent, childrens[], suffixIndex, suffixLink
)

As mentioned in previous approach, our problem of finding longest repeated substring boils down to finding a pair of suffixes
 having longest common prefix.
Rewriting this in context of suffix tree, we need to find node resNode, such that:
- resNode is a maximum path length node such that more than one leaf node in it's subtree, i.e. resNode has more than one
 suffixes ends in resNode's subtree.
That implies resNode is one of the internal nodes.
Now the claim is, the resNode is one of the immediate parent nodes of leaf nodes.
To prove this claim, let's say resNode is not one of the immediate parent nodes of leaf nodes. That implies resNode has
 atleast one internal node iNode as it's child node. Now as iNode is an internal node, it has more than one leaf node in
 it's subtree. Also, as it is child of resNode, pathLength(iNode)>pathLength(resNode) always as edge between resNode and
 iNode must contain atleast one character. CONTRADICTION as we found another node iNode in suffix tree which has more than
 one leaf in it's subtree and it's pathlength is greater that pathlength of resNode. So, our assumption that resNode is
 not one of the immediate parent nodes of leaf nodes can't be true.
So, we are now ready with all subparts to solve this problem.
Here is the pseudoCode.

lrsLength = 0, lrsSuffixIndex=-1
findLRS(Node node){
  isLeaf = true;
  for (Node childNode : node.childrensList) {
    isLeaf = false;
    findLRS(childNode);
  }
  if (isLeaf) {
    currLength = node.parent.pathLength;
    if (currLength > lrsLength) {
      lrsLength = currLength;
      lrsSuffixIndex = node.suffixIndex;
    }
  }
}


Substring starting at (lrsSuffixIndex) and ending at (lrsSuffixIndex+lrsLength-1) is the longest repeated substring
(There maybe multiple lrs in inputStr. Here, we are finding any one.)
As time complexity to construct suffix tree is O(n), and we are traversing all O(n) nodes of suffix tree to find lrs, overall
 time complexity of solution will be O(n).
As there are O(n) nodes in suffix tree, overall space complexity of this approach will be O(n).
There are minor changes in implementation of this approach. See the solution code file for better understanding of approach
 and implementation.
Time complexity: O(n)
Auxiliary Space Used: O(n)
Space complexity: O(n)
File: optimal_solution.java
Reference : https://sites.google.com/site/indy256/algo/suffix_tree
https://en.wikipedia.org/wiki/Ukkonen%27s_algorithm
We note that time and space complexities of suffix tree construction depends on size of allowed set of characters, depending
 on the type of implementation. Ukkonen’s algorithm for suffix tree construction, which we have used here, runs in O(n)
 if size of allowed set of characters is constant and O(n*NO_OF_CHARACTERS) without this assumption. As we have constant
 size of set of allowed characters mentioned in this problem, it is O(n) time and space complexity.
Exercise for readers:
- This problem can also be solved using:
1. Suffix array
2. String hashing, binary search
- Extension of this problem:
Find longest repeated substring for a given string s of length n, which occurs atleast k times. Same constraints.
'''
'''
BRUTE FORCE
package LongestRepeatedSubstring.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string str of length n, find the longest repeated substring in it.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class brute_force {

    // -------------------- START ----------------------

    public static String getLongestRepeatedSubstring(String inputStr) {
        int n = inputStr.length();
        int j;
        String curr;
        // Iterate over all possible substrings in descending order of their length
        for (int len = n - 1; len > 0; len--) {
            for (int i = 0; i + len - 1 < n; i++) {
                j = i + len - 1;
                curr = inputStr.substring(i, j + 1);
                // Check if substring inputStr.substring(i, j + 1) occurs anywhere other than at index i
                // or not
                if (isSubstring(inputStr.substring(i + 1), curr)) {
                    // Found at least one occurrence of inputStr.substring(i, j + 1) at some index ind >= i+1
                    return curr;
                }
                if (isSubstring(inputStr.substring(0, j), curr)) {
                    // Found at least one occurrence of inputStr.substring(i, j + 1) at some index ind <= i-1
                    return curr;
                }
            }
        }
        return "";
    }

    public static boolean isSubstring(String text, String pattern) {
        return text.contains(pattern);
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String inputStr = br.readLine().trim();

        String result = getLongestRepeatedSubstring(inputStr);
        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();

        br.close();
    }

}

/**
 * Time complexity: O(n^4)
 * Space complexity: O(n)
 */
'''
'''
OPTIMAL SOLUTION
package LongestRepeatedSubstring.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string str of length n, find the longest repeated substring in it.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class optimal_solution {

    // -------------------- START ----------------------

    static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz\1";

    public static class Node {
        int begin;
        int end;
        int depth; // distance in characters from root to this node
        Node parent;
        Map<Byte, Node> children;
        Node suffixLink;

        Node(int begin, int end, int depth, Node parent) {
            this.begin = begin;
            this.end = end;
            this.parent = parent;
            this.depth = depth;
            children = new HashMap();
        }
    }

    public static Node buildSuffixTree(CharSequence s) {
        int n = s.length();
        byte[] a = new byte[n];
        Map<Character, Byte> map = new HashMap<>();
        for (int i = 0; i < ALPHABET.length(); i++) {
            map.put(ALPHABET.charAt(i), (byte) i);
        }
        // Converting CharSequence s to byte array a, using index of that char in universal string ALPHABET
        for (int i = 0; i < n; i++) a[i] = map.get(s.charAt(i));
        Node root = new Node(0, 0, 0, null);
        Node node = root;
        for (int i = 0, tail = 0; i < n; i++, tail++) {
            Node last = null;
            while (tail >= 0) {
                Node ch = node.children.get(a[i - tail]);
                while (ch != null && tail >= ch.end - ch.begin) {
                    tail -= ch.end - ch.begin;
                    node = ch;
                    ch = ch.children.get(a[i - tail]);
                }
                if (ch == null) {
                    node.children.put(a[i], new Node(i, n, node.depth + node.end - node.begin, node));
                    if (last != null) last.suffixLink = node;
                    last = null;
                } else {
                    byte t = a[ch.begin + tail];
                    if (t == a[i]) {
                        if (last != null) last.suffixLink = node;
                        break;
                    } else {
                        Node splitNode = new Node(ch.begin, ch.begin + tail,
                                node.depth + node.end - node.begin, node);
                        splitNode.children.put(a[i], new Node(i, n, ch.depth + tail, splitNode));
                        splitNode.children.put(t, ch);
                        ch.begin += tail;
                        ch.depth += tail;
                        ch.parent = splitNode;
                        node.children.put(a[i - tail], splitNode);
                        if (last != null) last.suffixLink = splitNode;
                        last = splitNode;
                    }
                }
                if (node == root) {
                    --tail;
                } else {
                    node = node.suffixLink;
                }
            }
        }
        return root;
    }

    static int lrsLength;
    static int lrsSuffixIndex;
    static String s;

    static void findLRS(Node node) {
        boolean isLeaf = true;
        for (Byte b : node.children.keySet()) {
            isLeaf = false;
            findLRS(node.children.get(b));
        }
        // As name suggests, isLeaf will be true at this point, if it has no child

        // If node is a leaf, then suffix string formed by path from root to it's parent node is a
        // repeated substring
        // and a candidate for longest repeated substring
        if (isLeaf) {
            int currLength = node.depth;
            // currLength here denotes path length of node.parent. i.e. node.parent.pathLength == node.depth
            if (currLength > lrsLength) {
                lrsLength = currLength;
                lrsSuffixIndex = s.length() - (node.depth + node.end - node.begin);
                // For a leaf node, suffixIndex(i.e. index of suffix that ends here) is nothing but (
                // (length of given
                // string s) - path length of current node)
            }
        }
    }

    public static String getLongestRepeatedSubstring(String inputStr) {
        // Adding a special character('\1' here) in the end of string to make it explicit suffix tree.
        // In explicit suffix tree, all the suffixes ends at a leaf
        s = inputStr + "\1";
        Node tree = buildSuffixTree(s);
        lrsLength = 0;
        lrsSuffixIndex = -1;
        // findLRS will find the LRS and will populate the results in lrsLength and lrsSuffixIndex
        findLRS(tree);
        String lrs = "";
        if (lrsLength > 0) {
            lrs = s.substring(lrsSuffixIndex, lrsSuffixIndex + lrsLength);
        }
        return lrs;
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String args[]) {
        // Launching a thread with larger allowed stack memory to avoid StackOverflowException
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    new optimal_solution();
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (StackOverflowError e) {
                    System.out.println("RTE");
                }
            }
        }, "1", 1 << 26).start();
    }

    optimal_solution() throws IOException {
        solve();
    }

    static void solve() throws IOException {
        long beforeUsedMem = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String inputStr = br.readLine().trim();

        String result = getLongestRepeatedSubstring(inputStr);
        bufferedWriter.write("" + result.length());
        bufferedWriter.newLine();
        long afterUsedMem = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        System.out.println((afterUsedMem - beforeUsedMem) / 1000000);
        bufferedWriter.close();

        br.close();

    }

}

/**
 * Time complexity: O(n)
 * Space complexity: O(n)
 * Reference : https://sites.google.com/site/indy256/algo/suffix_tree
 */
'''
'''
package LongestRepeatedSubstring.solutions; /**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string str of length n, find the longest repeated substring in it.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class other_solution {

    // -------------------- START ----------------------

    public static String getLongestRepeatedSubstring(String inputStr) {
        int n = inputStr.length();
        int[][] lcp = new int[n][n];
        // lcp[i][j] = k means length of longest common prefix between suffix starting at i and suffix
        // starting at j is k

        for (int i = 0; i < n; i++) {
            lcp[i][n - 1] = (inputStr.charAt(i) == inputStr.charAt(n - 1) ? 1 : 0);
        }

        for (int i = 0; i < n; i++) {
            lcp[n - 1][i] = (inputStr.charAt(n - 1) == inputStr.charAt(i) ? 1 : 0);
        }

        int lrsLen = 0, lrsIndex = -1;
        for (int i = n - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                if (inputStr.charAt(i) == inputStr.charAt(j)) {
                    lcp[i][j] = 1 + lcp[i + 1][j + 1];
                } else {
                    lcp[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (lcp[i][j] > lrsLen) {
                    lrsIndex = i;
                    lrsLen = lcp[i][j];
                }
            }
        }

        String lrs = "";
        if (lrsIndex > -1) {
            lrs = inputStr.substring(lrsIndex, lrsIndex + lrsLen);
        }

        return lrs;
    }

    // -------------------- END ----------------------

    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new PrintWriter(System.out));

        String inputStr = br.readLine().trim();

        String result = getLongestRepeatedSubstring(inputStr);
        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();

        br.close();
    }

}

/**
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */
'''
