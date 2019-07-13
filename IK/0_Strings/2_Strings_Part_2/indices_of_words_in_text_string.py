'''
Indices Of Words In Text String
Problem Statement:
You are given a text string and q words. For all q words, You need to find out all words from text string which are matching
 with given word.
Input Format:
Two arguments. First is text string and second is list of words.
Output Format:
Return List of q lists, where ith list contains indices of first character of all the matching words in text string, for
 words[i], in sorted order.
If no word found in text string for given word then have -1 as only element of answer list for that word.
Constraints:
Text string and words of query can contain characters from a-z, A-Z, 0-9 and symbols from set {'$', '#', '@', '?' ,';'}.
 Additionally text string can contain spaces also.
Assume words in text string are single space separated. text string starts
 and ends with a word, not space(s). There will be no consecutive spaces in text string.
1 <= len(text) <= 1000000.
1<=
 q <= 100000.
Length of any word of query and text string l, 1<= l <= 10.
Every query word will be unique.
Consider indexing
 of character in text string from 0.
Returned list of indices must be sorted in increasing order.
Sample Test Case:
Sample Input:
text = “you are very very smart”
words = [“you”, “are”, “very”, “handsome”]
Sample Output:
[
[0],
[4],
[8, 13],
[-1]
]
Explanation:
For given text string = “you are very very smart”. “you” is matching with first word “you” which is starting from index
 0 of text string so answer for “you” will be 0.
Similarly for “are” answer is 4.
“very” is matching with word at index 8 and 13 so answer for “very” will be 8 and 13.
“handsome” is not matching with any word so it’s answer is -1;
'''
import math
import os
import random
import re
import sys


#
# Complete the 'find_words' function below.
#
# The function accepts STRING and STRING ARRAY as parameter.
# Return 2D INTEGER ARRAY.
#
def find_words(text, words):
    pass


if __name__ == '__main__':
    text = input().strip()
    q = int(input().strip())
    words = []
    for _ in range(q):
        words.append(input().strip())
    fptr = sys.stdout
    result = find_words(text, words)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
This approach is very simple and a brute force solution. For every query word find all first index of character of word
 from text string which is matching.
Time Complexity:
O(n*q*l) where n is number of words in text string and q is number of queries of words and l is maximum length of word.

As we are finding solution for each query in O(n*l) and there can be q queries so it will take O(n*q*l) time.
Auxiliary Space Used:
O(q+n) where n is number of words in text string and q is number of queries of words.
As we storing indices of query words which we found and as it is possible that result list can contain all indices of words
 of text string which can be equal to n. (Given that the query words will be unique, hence any word in text string can match
 <= 1 query word. Hence summation of matching indices in returned list of lists can not be more than n .)
Space Complexity:
O((n+q)*l) where n is number of words in text string, q is number of queries of words, l is maximum length of word.
For input we are storing q words of maximum length l in O(q*l) and for storing text string it will be O(n*l) and auxiliary
 space used is O(q+n).
So, O(q*l) + O(n*l) + O(q+n) -> O((n+q)*l).
2) optimal_solution1.java
Description:
In this solution, we are using HashMap to maintain indices list for words. We are populating hashmap while iterating over
 given words of text string. Then for each query we are getting query indices of matching word from maintained hashmap.

Time Complexity:
O((n+q)*l) where n is number of words in text string and q is number of queries of words and l is maximum length of word.

To populate hashmap, time complexity will be O(n*l) and for getting result of q queries time complexity will be O(q*l).

O(n*l) + O(q*l) → O((n+q)*l)
Auxiliary Space Used:
O((n*l)+q) where n is number of words in text string and q is number of queries of words and l is maximum length of word.

As we are maintaining hashmap for indices list of words in O(n*l) and storing indices of query words which we found in O(q
 + n) as it is possible that result list can contain all indices of words of text string which can be equal to n. (Given
 that the query words will be unique, hence any word in text string can match <= 1 query word. Hence summation of matching
 indices in returned list of lists can not be more than n .)
So, O(n*l) + O(q+n) → O((n*l)+q)
Space Complexity:
O((n+q)*l) where n is number of words in text string, q is number of queries of words, l is maximum length of word.
For input we are storing q words of maximum length l in O(q*l) and for storing text string it will be O(n*l) and auxiliary
 space used is O((n*l)+q).
So, O(q*l) + O(n*l) + O((n*l)+q) -> O((n+q)*l).
3) optimal_solution2.java
Description:
In this solution, we are using Trie tree. First we will iterate over all the words in text string and inserting them to
 Trie tree. Now whenever we need to find matching words from text string we search it in Trie and return result indices.

optimal_solution2 (using trie tree) will be better than optimal_solution1 (using hashmap) in cases where prefix of strings
 are overlapping. Because space will be less to store n number of strings where some strings prefixes are overlapping.
In actual interview, interviewer will expect a Trie solution from you instead of hashmap one.
For more information on when to use hashmap and when to use trie tree. Look at this stackoverflow answer.
https://stackoverflow.com/questions/245878/how-do-i-choose-between-a-hash-table-and-a-trie-prefix-tree
Time Complexity:
O((n+q)*l) where n is number of words in text string and q is number of queries of words and l is maximum length of word.

As Insert and search in Trie tree will be O(l).
To populate trie tree, it will iterate over all words in text string hence will take O(n*l).
And, to search for q queries, it will iterate over all q queries hence will take O(q*l)
So, O(n*l) + O(q*l) → O((n+q)*l)
Auxiliary Space Used:
O(n*l + q) where n is number of words in text string, l is maximum length of word and q is number of queries of words.
As we are storing n words of maximum length l in trie tree and storing indices of query words which we found in O(q + n)
 as it is possible that result list can contain all indices of words of text string which can be equal to n. (Given that
 the query words will be unique, hence any word in text string can match <= 1 query word. Hence summation of matching indices
 in returned list of lists can not be more than n .)
O(n*l) + O(q+n) → O(n*l + q)
Space Complexity:
O((n+q)*l) where n is number of words in text string, q is number of queries of words, l is maximum length of word.
For input we are storing q words of maximum length l in O(q*l) and for storing text string it will be O(n*l) and auxiliary
 space used is O(n*l + q).
So, O(q*l) + O(n*l) + O(n*l + q) -> O((n+q)*l).
'''
'''
BRUTE FORCE
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
    * Complete the 'find_words' function below.
    *
    * The function accepts STRING and STRING ARRAY as parameter.
    * Return 2D INTEGER ARRAY.
    */
    // ============================ Start ============================
    public static ArrayList<ArrayList<Integer>> find_words(String text, List<String> words){
        // To store indexes for the given words
        ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>();
        String words_in_file[] = text.split(" ");
        for(String word: words) {
            ArrayList<Integer> indexes = new ArrayList<Integer>();
            // Iterating over the complete list of words in file
            int sum_index = 0;
            for(int i=0; i<words_in_file.length; i++) {
                // If word matches with word of file then we add index of first character of that word in list
                if(words_in_file[i].compareTo(word)==0) {
                    indexes.add(sum_index);
                }
                sum_index += words_in_file[i].length() + 1;
            }
            // If we found no word matching with what we were looking for then we add -1 in list of indexes
            if(indexes.size()==0) {
                indexes.add(-1);
            }
            answer.add(indexes);
        }
        return answer;
    }
    // ============================= End ==============================
}


class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String text = bufferedReader.readLine().trim();
        int q = Integer.parseInt(bufferedReader.readLine().trim());
        List<String> words = new ArrayList<String>();
        
        for(int i=0;i<q;i++){
            words.add(bufferedReader.readLine().trim());
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<ArrayList<Integer>> result = Result.find_words(text, words);
        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            }); 
        bufferedWriter.close();
    }
}
'''
'''
OPTIMAL SOLUTION 1
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
    * Complete the 'find_words' function below.
    *
    * The function accepts STRING and STRING ARRAY as parameter.
    * Return 2D INTEGER ARRAY.
    */
    // ============================ Start ============================
    public static ArrayList<ArrayList<Integer>> find_words(String text, List<String> words){
        String words_in_file[] = text.split(" ");
        
        // For storing all the words in file along with list of indices of there occurring
        HashMap<String, ArrayList<Integer>> map = new HashMap<String, ArrayList<Integer>>();
        int sum_index = 0;
        for(int i=0; i<words_in_file.length; i++) {
            String word = words_in_file[i];
            ArrayList<Integer> indexes = new ArrayList<Integer>();
            if(map.containsKey(word)) {
                indexes = map.get(word);
            }
            indexes.add(sum_index);
            sum_index += word.length() + 1;
            map.put(word, indexes);
        }

        ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();
        for(String word: words){
            ArrayList<Integer> indexes = new ArrayList<Integer>();
            if(map.containsKey(word)){
                indexes = map.get(word);
            }
            else{
                indexes.add(-1);
            }
            ans.add(indexes);
        }

        return ans;
    }
    // ============================= End ==============================
}


class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String text = bufferedReader.readLine().trim();
        int q = Integer.parseInt(bufferedReader.readLine().trim());
        List<String> words = new ArrayList<String>();
        
        for(int i=0;i<q;i++){
            words.add(bufferedReader.readLine().trim());
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<ArrayList<Integer>> result = Result.find_words(text, words);
        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });
        bufferedWriter.close();
    }
}
'''
'''
OPTIMAL SOLUTION 2
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
    * Complete the 'find_words' function below.
    *
    * The function accepts STRING and STRING ARRAY as parameter.
    * Return 2D INTEGER ARRAY.
    */
    // ============================ Start ============================
    public static ArrayList<ArrayList<Integer>> find_words(String text, List<String> words){
        root = new TrieNode();
        String words_in_file[] = text.split(" ");
        int sum_index = 0;
        for(int i=0;i<words_in_file.length;i++) {
            // Inserting all the words of file in trie
            insert_trie(words_in_file[i], sum_index);
            sum_index += words_in_file[i].length() + 1;
        }
        ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>();
        for(String word: words) {
            // Searching for word in trie
            ArrayList<Integer> indexes = search_trie(word);
            // If no word found in file matching with our word then list of indices will have -1
            if(indexes.size()==0) {
                indexes.add(-1);
            }
            answer.add(indexes);
        }
        return answer;
    }
    // Root is for maintaining the root of trie
    public static TrieNode root;
    public static class TrieNode{
        // To maintain data, children information, indices and information that any word ending at this node or not
        char data;
        HashMap<Character, TrieNode> children;
        ArrayList<Integer> indexes;
        
        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
            indexes = new ArrayList<Integer>();
        }
    }
    public static void insert_trie(String word, int index) {
        // To insert word in the trie
        TrieNode head = root;
        for(char c: word.toCharArray()) {
            if(head.children.containsKey(c)) {
                // If child of current trie node have data matching with the character then we will make that child as current node
                head = head.children.get(c);
            }else {
                // If current trie does not have any child matching to the character then we create new child and make that as current node
                TrieNode new_node = new TrieNode();
                new_node.data = c;
                head.children.put(c, new_node);
                head = new_node;
            }
        }
        head.indexes.add(index);
    }
    public static ArrayList<Integer> search_trie(String word) {
        // To search for the word in the trie
        TrieNode head = root;
        for(char c: word.toCharArray()) {
            if(head.children.containsKey(c)) {
                // If child of current trie node's data matching with the character then we will make that child as current node 
                head = head.children.get(c);
            }else {
                // If child of current trie node's data not matching then will return blank list of indices
                return new ArrayList<Integer>();
            }
        }
        return head.indexes;
    }
    // ============================= End ==============================
}


class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String text = bufferedReader.readLine().trim();
        int q = Integer.parseInt(bufferedReader.readLine().trim());
        List<String> words = new ArrayList<String>();
        
        for(int i=0;i<q;i++){
            words.add(bufferedReader.readLine().trim());
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<ArrayList<Integer>> result = Result.find_words(text, words);
        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });
        bufferedWriter.close();
    }
}
'''
