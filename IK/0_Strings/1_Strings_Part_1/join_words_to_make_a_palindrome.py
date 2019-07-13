'''
Join Words To Make A Palindrome
Problem Statement:
Given a list of strings words, of size n, check if there is any pair of words, that can be joined (in any order) to form
 a palindrome then return the pair of words forming palindrome.
Input Format:
Only argument for function, list of strings words.
Output Format:
Return a pair of words (i.e. list of string result of size 2 such that result[0] + result[1] is a palindrome).
In case of multiple answer return any one of them.
In case of no answer return list [“NOTFOUND”, “DNUOFTON”].
Constraints:
Length l for each word of words list, 1<= l <= 30.
Size of list words n, 2 <= n <= 20000.
Characters for each word can be from [a-z], [A-Z], [0-9].
Sample Test Case:
Sample Input 1:
words = [ “bat”, “tab”, “zebra” ]
Sample Output 1:
result = [ “bat”, “tab” ]
Explanation 1:
As “bat” + “tab” = “battab”, which is a palindrome.
Sample Input 2:
words = [ “ant”, “dog”, “monkey” ]
Sample Output 2:
result = [ “NOTFOUND”, “DNUOFTON” ]
Explanation 2:
As for each 6 combinations of string of words, there is no single generated word which is a palindrome hence result list
 will be [ “NOTFOUND”, “DNUOFTON” ].
'''
import os
import sys


#
# Complete the join_words_to_make_a_palindrome function below.
#
def join_words_to_make_a_palindrome(words):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    words_count = int(input())
    words = []
    for _ in range(words_count):
        words_item = input()
        words.append(words_item)
    res = join_words_to_make_a_palindrome(words)
    fptr.write('\n'.join(res))
    fptr.write('\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be to iterate over all ordered pairs of words from list words, i.e. (words[i], words[j]) such that
 i != j, 0<=i<n, 0<=j<n, check if words[i] + words[j] is palindrome or not. If we found such pair of words of forming palindrome
 then return that pair of words.
Time Complexity:
O((n^2)*l), where n is size of list words and l is the maximum length of words in list words.
As there are total 2*(nC2) ordered pair of words, and for each pair, for finding whether that pair is forming palindrome
 or not will take O(l).So, time complexity of this solution will be O((n^2)*l).
Auxiliary Space Used:
O(l) where l is the maximum length of words in list words.
As we are storing result list of two words of maximum length l.
Space Complexity:
O(n*l) where n is size of list words and l is the maximum length of words in list words.
Input will take space O(n*l) because we are storing n words of list words where maximum possible length of word can be l
 and auxiliary space used is O(l). So, O(n*l) + O(l) -> O(n*l).
2) optimal_solution.java
Description:
A better approach would be as follows from some observations:
Let say there exists a pair of words (words[x], words[y]), such that result = (words[x] + words[y]) is a palindrome.
Two cases are possible here:
CASE 1: words[x].length() >= words[y].length()
Iterating over words, considering the word in the current iteration as xth word in words. Task is to find out if there exists
 some yth word, such that words[x] + words[y] is a palindrome. Now, if such y exists, it must be of the form stringReverse(words[x].substring(0,
 k)), for some 0 <= k < words[x].length().
So, now we only need to find such k, such that (words[y] == stringReverse(words[x].substring(0, k))) and (words[x].substring(k+1,
 words[x].length())) is a palindrome, if (k+1< words[x].length())
CASE 2: words[x].length() < words[y].length()
Iterating over words, considering the word in the current iteration as xth word in words. Task is to find out if there exists
 some yth word, such that words[y] + words[x] is a palindrome. Now, if such y exists, it must be of the form stringReverse(words[x].substring(k,
 words[x].length())), for some 0 <= k < words[x].length().
So, now we only need to find such k, such that (words[y] == stringReverse(words[x].substring(k, words[x].length()))) and
 (words[x].substring(0, k)) is a palindrome, if (k>0)
Both cases requires a quick lookup of words in list words. So, we can use hashset or hashMap here for constant time (amortized
 time) lookup of words. Also, in some cases, for eg. "aaaaa", we need to know the frequency of words so that
same word (same indexed word in list of words) doesn't get picked up as other word to make a palindrome. So, hashmap having
 word as key and frequency of that word as value will work here.
See the implementation for better understanding.
Time Complexity:
O(n*(l^2)) where n is size of list words and l is the maximum length of words in list words.
As while iterating over list of words, considering the word in current iteration as left_word, we have to do two lookups
 and two palindrome check for each k, 0 <= k < length(left_word), time complexity will be O(l^2) for each word left_word.

So, total time complexity will be O(n*(l^2)).
Auxiliary Space Used:
O(n*l) where n is size of list words and l is the maximum length of words in list words.
As we are maintaining a hashmap of frequencies of words for n words of list words, space complexity to maintain this will
 be O(n*l) and we are storing result list of two words of maximum length l.
O(n*l) + O(l) → O(n*l)
Space Complexity:
O(n*l) where n is size of list words and l is the maximum length of words in list words.
Input will take space O(n*l) because we are storing n words of list words where maximum possible length of word can be l
 and auxiliary space used is O(n*l). So, O(n*l) + O(n*l) -> O(n*l).
'''
'''
BRUTE FORCE
import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Result {

    // -------------------- START ----------------------
    static String[] join_words_to_make_a_palindrome(String words[]) {
        String result[] = new String[2];
        result[0] = "NOTFOUND";
        result[1] = "DNUOFTON";

        int n = words.length;
        // Iterating over all possible pair (i,j), 0<=i<j<n
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // check if (wordsList.get(i) + wordsList.get(j)) is palindrome or not
                if (isPalindrome(words[i] + words[j])) {
                    result[0] = words[i].toString();
                    result[1] = words[j].toString();
                    return result;
                }
                // check if (wordsList.get(i) + wordsList.get(j)) is palindrome or not
                if (isPalindrome(words[j] + words[i])) {
                    result[0] = words[j].toString();
                    result[1] = words[i].toString();
                    return result;
                }
            }
        }
        return result;
    }

    // Check if input string str is palindrome or not
    static boolean isPalindrome(String str) {
        int index = 0;
        int n = str.length();
        while(index<n-index) {
            if(str.charAt(index)!=str.charAt(n-index-1)) {
                return false;
            }
            index++;
        }
        return true;
    }
    // -------------------- END ----------------------
}

class Solution{
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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        String words[] = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = bufferedReader.readLine().trim();
        }
        
        String result[] = Result.join_words_to_make_a_palindrome(words);
        for(String str: result){
            bufferedWriter.write(str+"\n");
        }
        bufferedWriter.close();
        bufferedReader.close();
    }
}
'''
'''
OPTIMAL SOLUTIONS
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static String[] join_words_to_make_a_palindrome(String words[]) {
        String result[] = new String[2];
        result[0] = "NOTFOUND";
        result[1] = "DNUOFTON";

        HashMap<String, Integer> count = new HashMap<String, Integer>();
        for(String word: words){
            if(count.containsKey(word)){
                count.put(word, count.get(word)+1);
            }else{
                count.put(word, 1);
            }
        }
        // To find (left_word + right_word) exist which form palindrome where 
        // left_word and right_word in given list of words
        String current = "";
        
        for(String left_word: words){
            
            current = "";
            // Two cases are possible here:
            // 
            // CASE 1: words[x].length() >= words[y].length()
            
            // Iterating over words, considering the word in the current iteration as xth word in words.
            // Task is to find out if there exists some yth word, such that 
            // words[x] + words[y] is a palindrome. 
            // Now, if such y exists, it must be of the form
            // stringReverse(words[x].substring(0, k)), for some 0 <= k < words[x].length(). 
            // So, now we only need to find such k,
            // such that (words[y] == stringReverse(words[x].substring(0, k))) and 
            // (words[x].substring(k+1,words[x].length())) is a palindrome, if (k+1<words[x].length())
            
            for(int j=0;j<left_word.length();j++){
                // Here, current string denotes stringreverse(left_word.substring(0, j))
                // Check if current string is present in words or not
                current = left_word.charAt(j) + current;
                
                if(count.containsKey(current)){
                    // Handles that case so that same string itself doesn't get picked up as other string in pair to
                    // form a palindrome
                    if(current.equals(left_word)){
                        if(count.get(current)>1){
                            result[0] = left_word;
                            result[1] = current;
                            return result;
                        }
                    }
                    // Check if left_word.substring(j+1, len(left_word)) is a palindrome or not
                    else if(isPalindrome(left_word.substring(j+1))){
                        result[0] = left_word;
                        result[1] = current;
                        return result;
                    }
                }
            }
            
            current = "";
            
            // CASE 2: words[x].length() < words[y].length()
            
            // Iterating over words, considering the word in the current iteration as xth word in words.
            // Task is to find out if there exists some yth word, such that 
            // words[y] + words[x] is a palindrome. 
            // Now, if such y exists, it must be of the form
            // stringReverse(words[x].substring(k, words[x].length())), for some 0 <= k < words[x].length(). 
            // So, now we only need to find such k,
            // such that (words[y] == stringReverse(words[x].substring(k, words[x].length()))) and 
            // (words[x].substring(0, k)) is a palindrome, if (k>0)
            
            for(int j=left_word.length()-1;j>=0;j--){
                // Here, current string denotes stringreverse(left_word.substring(j+1, len(left_word)))
                // Check if current string is present in words or not
                current = current + left_word.charAt(j);
                
                if(count.containsKey(current)){
                    // Handles that case so that same string itself doesn't get picked 
                    // up as other string in pair to form a palindrome
                    if(current.equals(left_word)){
                        if(count.get(current)>1){
                            result[0] = current;
                            result[1] = left_word;
                            return result;
                        }
                    }
                    // Check if left_word.substring(0, j) is a palindrome or not
                    else if(isPalindrome(left_word.substring(0, j))){
                        result[0] = current;
                        result[1] = left_word;
                        return result;
                    }
                }
            }
        }
        return result;
    }
    
    // Check if string str is palindrome or not
    static boolean isPalindrome(String str) {
        int l = 0;
        int n = str.length();
        while(l<n-l){
            if(str.charAt(l)!=str.charAt(n-1-l)){
                return false;
            }
            l++;
        }
        return true;
    }
    // -------------------- END ----------------------
}

class Solution{
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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        
        String words[] = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = bufferedReader.readLine().trim();
        }
        
        String result[] = Result.join_words_to_make_a_palindrome(words);
        for(String str: result){
            bufferedWriter.write(str+"\n");
        }
        bufferedWriter.close();
        bufferedReader.close();
    }
}
'''


