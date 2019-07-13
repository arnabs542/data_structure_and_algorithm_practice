'''
Generate Numeronyms
Problem Statement:
Given a string word of length n, generate all possible numeronyms.
What is a Numeronym?
A numeronym is a word where a number is used to form an abbreviation.
For a given string word, a numeronym is a string with few or more contiguous letters between the first letter and last letter
 of word replaced with a number representing the count of letters omitted. Only one set of contiguous letters are replaced
 by a number.
e.g. “L10n” is called a numeronym of the word “Localization”, where 10 stands for the count of letters between the first

letter 'L' and the last letter 'n' in the word.
Input Format:
Only one argument denoting input string word.
Output Format:
Return strings array containing all possible numeronyms of given string word.
You need not to worry about order of strings in your output array. For words = "aaaaa", arrays ["a2aa", "aa2a", "a3a"],
 ["a3a", "aa2a", "a2aa"] etc will be considered as valid answer.
In case of no possible numeronym string, return empty list.
Constraints:
String will be composed of characters [a-z], [A-Z], [0-9] only.
1 <= n <= 120 where n is length of given string word.
Sample Test Case:
Sample Input:
word = “nailed”
Sample Output:
["n4d", "na3d", "n3ed", "n2led", "na2ed", "nai2d"]
Explanation:
“n4d” is abbreviated string of given string “nailed” where “aile” string letters are omitted and replaced by count of letters
 i.e. 4.
“na3d” is abbreviated string of given string “nailed” where “ile” string letters are omitted and replaced by count of letters
 i.e. 3.
Similarly for remaining generate numeronyms.
'''
import os
import sys


#
# Complete the neuronyms function below.
#
def neuronyms(word):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    word = input()
    res = neuronyms(word)
    fptr.write('\n'.join(res))
    fptr.write('\n')
    fptr.close()


'''
We have provided solution which contain necessary comments to understand the approach used:
1) optimal_solution.java
Description:
For any given string str, length of omitted characters l can 2 <= l <= n-2 where n is length of string as we can’t omit
 first and last characters and we need to find numeronym in which at least 2 contiguous letters were omitted.
So for any given length l, we iterate over all possible positions from where omission of characters can start, find string
 of length l from that position and replace that with l i.e. count of omitted characters.
Time Complexity:
O(n^3) where n is length of given string str.
As iteration will be in three loops, first over possible lengths then over possible first characters of omitted characters
 and then to find store newly created numeronym.
Auxiliary Space Used:
O(n^3) where n is length of given string str.
Maximum number of possible numeronym generated can be O(n^2) and length of each will be O(n) hence it takes O(n^3) to store
 output.
Space Complexity:
O(n^3) where n is length of given string str.
It will be equal to auxiliary space as in input we are just reading a single input string of length n which takes O(n).

O(n^3) + O(n) → O(n^3)
'''
'''
import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Result {

    // -------------------- START ----------------------
    static String[] neuronyms(String word) {
        int n = word.length();

        List<String> neuronyms_strings = new ArrayList<>();

        String answer[];

        if(n<=3){
            answer = new String[0];
            return answer;
        }

        String temp;
        // Iterating over all possible length of valid substrings that can be omitted
        for (int len = 2; len <= n - 2; len++) {
            // Iterating over all possible starting point of valid substrings of length len that can be omitted
            for (int i = 1; i <= n-1-len; i++) {
                temp = word.substring(0, i) + len + word.substring(i + len, n);
                neuronyms_strings.add(temp);
            }
        }
        
        int size = neuronyms_strings.size();
        answer = new String[size];

        for(int i=0;i<size;i++){
            answer[i] = neuronyms_strings.get(i);
        }

        return answer;
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

        String word = bufferedReader.readLine().trim();

        String [] result = Result.neuronyms(word);

        for(String str: result){
            bufferedWriter.write(str+"\n");
        }
        bufferedWriter.write("\n");
        
        bufferedWriter.close();

        bufferedReader.close();
    }

}
'''
