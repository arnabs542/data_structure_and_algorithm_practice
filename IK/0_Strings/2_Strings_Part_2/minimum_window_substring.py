'''
Minimum Window Substring
Problem Statement:
You are given an alphanumeric string ‘s’ and an alphanumeric string ‘t’. Find the minimum window (substring) in s which
 will contain all the characters of t.
Input/Output Format For The Function:
Input Format:
There are 2 arguments in the input, a string named s and a string named t.
Output Format:
Return a string result, which is the minimum window (substring) in string s that contains all characters of string t.
If no such window exists, then return an “-1” string and if there are multiple minimum windows of the same length, then
 return leftmost window.
Input/Output Format For The Custom Input:
Input Format:
The first line of input contains string s. The next line contains string t.
If s = “azisdflc” and t = “zsd” then input should be:
azisdflc
zsd
Output Format:
Output in a single line a string which is the minimum window that contains all the characters of string t.
For input s = “azisdflc” and t = “zsd”, output will be:
zisd
Constraints:
1 <= lenght(s) <= 100000
1 <= length(t) <=100000
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
AYZABOBECODXBANC
ABC
Sample Output 1:
BANC
Explanation 1:
The minimum window is "BANC", which contains all letters - A B and C. We cannot find a window of smaller length than “BANC”.

Sample Test Case 2:
Sample Input 2:
BACRDESDFBAER
BAR
Sample Output 2:
BACR
Explanation 2:
Here, we can see that there are 2 smallest windows - “BACR” and “BAER”. However, the output is “BACR” because it is the
 leftmost one.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'minimum_window' function below.
#
# The function accepts STRING s and STRING t as parameter.
#
def minimum_window(s, t):
    pass


if __name__ == '__main__':
    fptr = sys.stdout
    s = input()
    t = input()
    result = minimum_window(s, t)
    fptr.write(result + '\n')
    fptr.close()


'''
We have provided two solutions and both the solutions contain necessary comments to understand the approach used:
1) brute force solution.java
Description:
This is a brute force approach. We check whether each substring of string s is a valid window or not. If we find it to be
 a valid window, we update our result accordingly.
Time Complexity:
O(n^3) where n is the length of string s.
As we are checking for all substrings and as there are O(n^2) substrings and we take O(n) time to check whether the particular
 substring can be a valid window, so total complexity is O(n^3).
Auxiliary Space Used:
O(1).
We create frequency arrays of size O(128) to count the occurrence of each character present in strings t and s. So overall
 complexity is O(1).
Space Complexity:
O(n+m) where n is the length of string s and m is the length of string t.
For storing input it will take O(n+m), as we are storing two strings of length n and length m and auxiliary space used is
 O(1) hence total complexity will be O(n+m).
NOTE: We can even use an array of length 62 (with some mapping) instead of 128, but this is a general solution which works
 for the input string containing any ASCII characters.
2) optimal_solution.java
Description:
In this approach, We create an array named frequency to keep a count of occurrence of each character in string t (O(length
 of t)). Now we start traversing the string S and keep a variable “cnt” which increases whenever we encounter a character
 present in string t. When the value of count reaches the length of t, this substring contains all the characters present
 in string t. We try removing extra characters as well as unwanted characters from the beginning of the obtained string.
 The resultant string is checked whether it can become the minimum window, and the answer is updated accordingly.
Note: This algorithm uses the 2 pointer method, which is widely used in solving various problems. You can refer https://www.geeksforgeeks.org/two-pointers-technique/
 article to get an idea about this method as well as see related problems where this method can be applied.
Time Complexity:
O(n) where n is the length of string s.
Since each character of string s is traversed at most 2 times, the time complexity of the algorithm is O(n) + O(m).
Auxiliary Space Used:
O(1).
We are creating 2 frequency arrays of size 128, which use extra space O(128) + O(128). Hence it is O(1).
Space Complexity:
O(n+m) where n is the length of string s and m is the length of string t.
For storing input it will take O(n+m), as we are storing two strings of length n and length m and auxiliary space used is
 O(1) hence total complexity will be O(n+m).
NOTE: We can even use an array of length 62 (with some mapping) instead of 128, but this is a general solution which works
 for the input string containing any ASCII characters.
'''
'''
import java.io.*;

class Result {

    /*==================================START===================================*/
    public static String minimum_window(String s, String t){
        
        String result = "";

        if(t.length()>s.length()) {
            return "-1";
        }
        
        int freq1[] = new int[128]; //creating a frequency array to store the frequencies of the characters in string t
        int n = s.length();
        for(int i=0;i<t.length();i++) {
            freq1[(int)t.charAt(i)]++;
        }
        int len = n+1;

        //looping over every substring of string s
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                int freq2[] = new int[128]; //creating a frequency array to store the frequencies of the characters in the substring
                for(int k = i; k <= j; k++){
                    freq2[s.charAt(k)]++;
                }
                //checking if a substring contains all the letters in string t
                for(int k = 0; k < 128; k++){
                    if(freq2[k]<freq1[k]) {
                        break;
                    }
                    if(k == 127){
                        // if the substring contains all the characters, we check if it can 
                        // become the smallest one and update the result accordingly
                        if(len>(j-i)){
                            len = j-i;
                            result = s.substring(i,j+1);
                        }
                    }
                }
            }
        }
        return result.length()==0?"-1":result;
    }
    /*==================================END===================================*/
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

        String s = bufferedReader.readLine().trim();
    
        String t = bufferedReader.readLine().trim();

        String result = Result.minimum_window(s,t);
    
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();
    }

}
'''
'''
import java.io.*;

class Result {

    /*==================================START===================================*/
    public static String minimum_window(String s, String t){

        String result = "";

        if(t.length()>s.length()) {
            return "-1";
        }
        int n = s.length(), m = t.length();   
        int freq1[] = new int[128]; /*creating a frequency array to store the 
                                    frequencies of the characters in string t*/
        int freq2[] = new int[128]; /*creating a frequency array to store the 
                                    frequencies of the characters in string s*/
        for (char c : t.toCharArray()) {
            freq1[c]++;
        }
        int l = 0, len = n+1; 
        int cnt = 0;
        /*This part uses "2 pointer method." You can find a link 
        for the same in the editorial of this problem.*/
        for (int i = 0; i < n ; i++){
            char temp = s.charAt(i);
            freq2[temp]++;
            //if a character is present in string t we increment the count of cnt variable.
            if (freq1[temp]!=0 && freq2[temp]<=freq1[temp]) {
                cnt++; 
            }
            /*if we match all the characters present in string t, 
            we try to find the minimum window possible*/
            if (cnt==m) {
                /*if any character is occuring more than the required times, we try to remove it
                from the starting and also try to remove the unwanted characters that are 
                not a part of string t from the starting. We check the remainder string if it 
                can become the smallest window.*/
                while (freq2[s.charAt(l)]>freq1[s.charAt(l)] || freq1[s.charAt(l)]==0) { 
                    if (freq2[s.charAt(l)]>freq1[s.charAt(l)]) { 
                        freq2[s.charAt(l)]--; 
                    }
                    l++; 
                }
                //check if this can become the smallest window and update the result accordingly.
                if (len > i-l+1) { 
                    len = i-l+1;
                    result = s.substring(l,l+len);
                } 
            } 
        } 
        return result.length()==0?"-1":result;
    }
    /*==================================END===================================*/
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

        String s = bufferedReader.readLine().trim();
    
        String t = bufferedReader.readLine().trim();

        String result = Result.minimum_window(s,t);
    
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();
    }

}
'''
