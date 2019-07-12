'''
Word Break
Problem Statement:
You are given a dictionary set dictionary that contains dictionaryCount distinct words and another string txt. Your task
 is to segment the txt string in such a way that all the segments occur in a continuous manner in the original txt string
 and all these segments (or words) exists in our dictionary set dictionary.
In short you have to split the string txt using ‘ ‘(single white space delimiter) in such a way that every segment(or word
 exists in our dictionary.
Same word from the dictionary can be used multiple times when splitting the given string.
Example: Suppose our Dictionary is {“to”, “do”, “todo”}
and txt is “totodo” then it can also be segmented as
“to to do”. Here the word “to” from the dictionary is being used twice.
Input Format:
First parameter of the function that is to be implemented is an integer dictionaryCount denoting, the number of words in
 our dictionary. Second parameter is a vector(array) of strings dictionary, denoting the list of words in our dictionary
 and the last parameter is a string txt, denoting the text string that is to be segmented.
Output Format:
Return array of strings containing all different possible segmentation arrangements for the txt string.
Constraints:
1 <= dictionaryCount <= 500
1 <= |txt| <= 19
1<= lengths of words in dictionary <= 19
All the characters in txt and words in dictionary are lower case English alphabets.
Sample Test Case:
7
kick
start
kickstart
is
awe
some
awesome
kickstartisawesome
Sample Output:
kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
Explanation:
There are only 4 possible segmentations possible for the given txt. All of which are mentioned above.
Consider first segmented string: “kick start is awe some”
Here all the words: kick, start, is, awe and some exists in our dictionary and these words are continuous substrings of
 the txt string “kickstartisawesome”.
Similarly, other three segmentations satisfy the same conditions and hence are valid segmentations of the given string
Note:
This problem asks to print ALL different possible segmentation arrangements, hence solution will be exponential. But, if
 we are just asked to find count or one such possibility, then its time complexity will be much lower (better). We are working
 on one new problem which asks only to find count.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'solver' function below.
#
# The function accepts STRING_ARRAY dictionary as parameter
# and the original STRING txt on which segmentation is to be
# performed.
# The function returns the list of all possible segmentation
#


def solver(dictionary, txt):
    return []


if __name__ == '__main__':
    dictionary_count = int(input().strip())
    dictionary = []
    for _ in range(dictionary_count):
        word = input().strip()
        dictionary.append(word)
    txt = input().strip()
    fptr = sys.stdout
    result = solver(dictionary, txt)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()


'''
Problem Overview:
Given a string and a dictionary of words, the problem asks to add single whitespaces between two characters in the string
 such that every word exists in the given dictionary.
Suppose let our Dictionary be: [“all”, “in”, “into”, “to”].
And our string txt is “allinto”.
So, only two arrangements are possible and are listed below:
all in to
all into
Brute-force Solution:
The brute-force approach is pretty simple like all other brute force approaches. Let’s keep creating all substrings of the
 string txt starting at the index 0 and simultaneously, checking if the created substring exists in our dictionary. If the
 substring exists in our dictionary we will segment it and recursively perform the same thing remaining part of the string
 txt. Doing so if we end up with an empty string then it is a success. We will then backtrack our way and keep storing the
 segments we made.
Time Complexity for this approach is O(n * Len + n * L * 2^L) in the worst case, where n is the number of words in the dictionary,
 Len is the maximum length of word in the dictionary and L is the length of the string txt. To visualize this upper bound
 on the time complexity let’s think this way:
Time taken to read the input is O(n * Len).
In worst case, there are O(2^L)  arrangements possible. For each arrangement total cost is: cost of building the arrangement
 + checking if substrings are present in the dictionary or not. Length of any arrangement will be O(L), hence cost for building
 any arrangement will be O(L). Now let's see the cost of checking if substrings are present in the dictionary or not. Suppose
 in ith arrangement = txt1 + " " + txt2 + " " + txt3 + ... + txtx. Now for each substring txt1, txt2,...txtx we are checking,
 if all these substrings exists in our dictionary. To do so, we are linearly searching our substring in the dictionary.
 For txt1 it will take O(n * len(txt1)) time ... for txtx it will take O(n * len(txtx)) time. So in total, it will take
 O(n * len(txt1)) + ... + O(n * len(txtx)) time. Now len(txt1) + ... + len(txtx) = L. Hence total time for checking if substrings
 are present in the dictionary or not will be O(n * L). So, the total time for processing part will be O(n * L * 2^L).
Time complexity = O(n * Len) + O(n * L * 2^L) -> O(n * Len + n * L * 2^L).
Talking of Space Complexity, let’s first see the auxiliary space used by this approach. It is the final result container
 that stores all the different arrangements of the txt string. So, the auxiliary space is equal to the number of different
 arrangements possible that in worst case is 2^L multiply by the length of the individual arrangement that in worst case
 is (2* L-1). Hence, the auxiliary space adds up to an order of O(L*2^L).
The initial input space of the program is the dominated by the dictionary array i.e. O(N*Len),  here Len is the max length
 of word in our dictionary. So, our Space Complexity is O(L*2^L + N*Len).
Optimal Solution:
Just by thinking the brute force way, we could have sight that we were recalculating many results over again and hence tells
 us that the problem has overlapping subproblems property. Consider the below representation for better visualization of
 overlapping cases:
Txt: { hellomynameisjack }
hello Txt: { mynameisjack }
hello my Txt: { nameisjack }
hello my name Txt: { isjack }
hello my name is Txt: { jack }
hello my name is jack Txt: { }
Here, we can easily visualize that at every step we are solving the same problem over again for the string in the curly
 braces.
Also, one thing worth noticing is that the segmentation for each text in the curly braces can be appended with its preceding
 substring. So, this also tells that the problem has an optimal sub-structure.
Hence, we can use dynamic programming to solve this problem.
So, let’s first calculate the number of different segmentations possible for the given string txt.
We will deal with the dp solution in steps:
Step 1: Decide if it is dp problem
We have already done this.
Step 2: Define the state of the dp
Let’s start thinking of the states. It is clear that we need to uniquely identify a substring through our state. So, we
 can take two integers denoting the start and end point of our substring.
Hence, now our dp state will be a 2-dimensional array.
So, our dp is something like dp[start][end]. Here, dp[start][end] tells us the number of segmented arrangements possible
 for the substring starting at start and ending at end. Hence, if we want to know the total arrangements possible for our
 txt string, we simply ask the dp[0][L-1] state ( L is the length of txt string ).
Wait, let’s take a break and re-examine our state. Do we really need the end index in our state? No, we can directly omit
 it to redefine our dp state as dp[start], where dp[start] tells us the number of total segmented arrangements possible
 for substring starting at start index and ending at L-1. So, if we now want to know the total number of arrangements for
 the string txt, we simply go and ask the dp state dp[0].  Take a breath and re-read this current paragraph till you understand
 the significance of it.
Hurray! we reduced our state space from 2 dimension to a linear dimension. This process is called state-space reduction.

Step 3: Deciding state transaction
So far now we have a state like dp[start] which tells us the number of all segmented arrangements possible for the substring
 starting at index 0 and ending at L-1.
Now, let’s see how we can compute value of state(idx)
Here, state(idx) means same as dp[idx].
You can consider state(idx) as the computation and dp[idx] as the result of the computation.
Like the brute approach we will keep on generating all the substring that start at idx and check if it exists in dictionary.
 If it exists in dictionary we solve the same problem again for the remaining string
Pseudo code:
state(idx):
result = 0
for end = idx to L-1:
If substring[idx,end] exists in Dictionary:
Result += state(end+1)
Above was the pseudo code for the state transition. The variable result stores the total number of arrangements for the
 state(idx).
Step 4: Adding Memorization:
Do you find anything fishy in our state transitions. Yes, we were over again recalculating for each state. Hence, we apply
 memorization and store the computed value of each state so that next time if we need that state information we do not recalculate
 it but directly return it from our Memorization.
We do that by simply storing the value of the result variable in our dp[idx] array. Next time the sate info is required
 we first check our dp[] array for that state, if it has the result we simply return it or else we compute it, memorize
 it and then return it.
The time complexity of the above optimal solution is O(L^3 + N*Len) , where L is the length of the txt and Len is the max
 length of the word in the dictionary. We can justify it as following: there are only L states and we are visiting all L
 states only once because of memorization. Now at each state we are first generating all its substring starting from the
 leftmost index and then checking its presence in the dictionary. This process is O(L^2). O(L) iterations to generate the
 substrings and another nested O(L) iteration to check its presence in the dictionary. So, the Time Complexity of this dp
 solution will be:
number of states * computation time of each state i.e. L * L^2. Hence, it summarizes to O(L^3) plus the extra time taken
 to insert the words into the Dictionary Set i.e. O(N*Len).
The Space Complexity is the space taken by the dp memorization table i.e. O(L^2) plus the space taken by the dictionary
 set i.e. O(N*Len). Hence, Total Space Complexity is O(L^2 + N*Len).
Oops! Wait till now we have only calculated the total number of arrangements, but we also need to print those arrangements.
 Well that’s not a big deal. We will maintain an extra vector for each state that stores the indexes where we can segment
 the current state substring. This can be done within the state computation transition.
Kindly, refer to the solution for implementation.
Once, we have this index split data for all the states then it is just one DFS traversal to print all the arrangements.
 Again, kindly refer to the solution code for the implementation.
As in the above calculation we are building every possible arrangement by directly segmenting at the correct index. Hence,
 the time complexity will be time taken to build an arrangement*total number of arrangements. Time taken to build a string
 in worst case is O(2*L) (because max length of the arrangement string can be 2L-1).
So, the Time Complexity is O(L*2^L) for building all the arrangements.
Now, let’s calculate the auxiliary space used for this computation. As we are storing the split indexes for each state.
 So, in worst case we will end up storing L*(L-1) / 2 split indexes for the case when all the substrings of our text is
 present in the dictionary. Hence, the space complexity for the storing the segmentation indexes is O(L^2). Also, like in
 the brute force approach we are also maintaining a final container to store all the possible arrangements having the same
 space complexity of O(L*2^L).  So, the total auxiliary space taken by our program will be O(L^2) + O(L*2^L) ~ O(L*2^L).
 Also, the space complexity from the initial input is the dictionary array that takes O(N*Len) space ( same as in brute
 force approach).
Hence, Total Space Complexity for this calculation is O(N*Len + L*2^L).
'''
'''
word_problem.cpp
#include<bits/stdc++.h>

using namespace std;

const int MIN_N = 1, MAX_N = 500;
const int MIN_WORD_LEN = 1, MAX_WORD_LEN = 19;

// ------------------------------ START ----------------------------------

vector<string> solver(int n, vector<string> dict, string text){
    unordered_set<string> dict_hash_set(dict.begin(), dict.end());
    int text_len = text.length();

    vector<vector<string>> ans(text_len, vector<string>(0));

    for (int i = 0; i < text_len; i++){
        for (int j = 0; j <= i; j++){
            string sub_text = text.substr(j, i - j + 1);

            if (dict_hash_set.find(sub_text) != dict_hash_set.end()){
                if (j == 0){
                    ans[i].push_back(sub_text);
                }else{
                    for (const string& s : ans[j - 1]){
                        ans[i].push_back(s + " " + sub_text);
                    }
                }
            }
        }
    }

    return ans[text_len - 1];
}

// ------------------------------ STOP ----------------------------------

void assert_lower_case_letters(string& s){
    for (const char& ch : s){
        assert('a' <= ch);
        assert(ch <= 'z');
    }
}

int main(){
    freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//generated_medium_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_medium_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//ignore.txt", "w", stdout);

    int test_cases;
    cin >> test_cases;
    assert(0 <= test_cases);

    while (test_cases--){
        int n;
        cin >> n;
        assert(MIN_N <= n);
        assert(n <= MAX_N);

        vector<string> dict(n);
        for (int i = 0; i < n; i++){
            cin >> dict[i];
            assert(MIN_WORD_LEN <= dict[i].length());
            assert(dict[i].length() <= MAX_WORD_LEN);
            assert_lower_case_letters(dict[i]);
        }

        unordered_set<string> dict_set(dict.begin(), dict.end());
        assert(dict_set.size() == n);

        string text;
        cin >> text;
        assert(MIN_WORD_LEN <= text.length());
        assert(text.length() <= MAX_WORD_LEN);
        assert_lower_case_letters(text);

        vector<string> ans = solver(n, dict, text);

        cout << ans.size() << endl;
        for (const string& s: ans){
            cout << s << endl;
        }
    }

    return 0;
}
'''
'''
BRUTE FORCE
#include "bits/stdc++.h"

using namespace std;

// ------------------------------ START ------------------------------

string rtrim(const string &str)
{
    string s(str);
    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());
    return s;
}

// backtrack function to compute all the valid segmentation
// @param txt: string whose segmentation is to be computed
// dict: vector containing the list of words in our dictionary
// trailingPrefix: segmented strings that is to added before the
// segmentation of the current string txt.
void computeAllArrangements(string txt, vector<string> &dict, string trailingPrefix,
                            vector<string> &allArrangements)
{

    int len = txt.length();
    // breaking condition, as now we have reached the end
    // of the string
    if (len == 0)
    {
        // adding the segmentation arrangement to the result
        allArrangements.push_back(rtrim(trailingPrefix));
        return;
    }

    // looping on all substring of the string txt starting from index 0
    for (int i = 0; i < txt.length(); i++)
    {
        // current segment ( substring [0,i] )
        string segment = txt.substr(0, i + 1);
        // checking if it exists in the dictionary
        if (find(dict.begin(), dict.end(), segment) != dict.end())
        {
            // appending current segment to the trailing prefix so far
            string newPrefix = trailingPrefix + segment + " ";
            // recursively computing for substring of txt [i+1,len)
            computeAllArrangements(txt.substr(i + 1, txt.length() - i - 1), dict,
                                   newPrefix, allArrangements);
        }
    }
}

vector<string> solver(vector<string> &dictionary, string &txt)
{
    // container to store all segmentations
    vector<string> allArrangements;
    // computing all the arrangements
    computeAllArrangements(txt, dictionary, "", allArrangements);
    // return computed arrangements
    return allArrangements;
}

// ------------------------------ STOP -------------------------------

int main(int argc, char *argv[])
{
    // freopen(
    //     "..//test_cases//generated_medium_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_expected_output.txt", "w",
    //     stdout);

    // int t;
    // cin >> t;
    // while (t--)
    // {
    int n;
    cin >> n;

    string txt;
    vector<string> dictionary;

    for (int i = 0; i < n; i++)
    {
        string word;
        cin >> word;
        dictionary.push_back(word);
    }

    cin >> txt;

    vector<string> result = solver(dictionary, txt);

    if (result.size() > 0)
    {
        for (int i = 0; i < result.size(); i++)
        {
            cout << result[i];
            if (i != (result.size() - 1))
                cout << "\n";
        }
    }
    // else {
    //     cout << "NA";
    // }
    // }
    return 0;
}
'''
'''
OPTIMAL SOLUTION 1
#include "iostream"
#include "unordered_set"
#include "vector"
#include "string"

using namespace std;

// ------------------------------ START ------------------------------

const int MAXN = 1000;

void rstrip(string &s)
{
    int l = s.length();
    int cnt = 0;
    for (int i = l - 1; i > 0; i--)
    {
        if (s[i] == ' ')
            cnt++;
        else
            break;
    }
    while (cnt--)
        s.pop_back();
}

// @param idx : start point of the sub-string in the text
// @return number of segmentation arrangements possible for
// substring [idx,len)
// additionaly marks the word segmenting index in the
// substring [idx,len)
int solve(int idx, unordered_set<string> dict, string text, int *dp,
          vector<vector<int>> &splitIndex)
{
    int len = text.length();

    // break condition if no substring possible
    if (idx == len)
        return true;

    // return if already memoized current state
    if (dp[idx] != -1)
        return dp[idx];

    // stores computation result for current state
    int result = 0;

    // initializing current segment starting from idx
    string segment = "";

    for (int i = idx; i < len; i++)
    {
        // adding ith character to the segment
        segment.push_back(text[i]);

        // checking if segment exists in the dictionary
        if (dict.find(segment) != dict.end())
        { // segmenting at this index
            // and getting number of possible segmentation arrangements
            // for  substring [i+1,len)
            int numOfArrangements = solve(i + 1, dict, text, dp, splitIndex);

            // checking if segmention arrangement possible for current split
            if (numOfArrangements > 0)
            {
                // add current index as split-pivot for substring [idx,len)
                splitIndex[idx].push_back(i);
            }

            // update result for current state
            result += numOfArrangements;
        }
    }

    // memoize current state , so can be reused next time
    dp[idx] = result;

    // return current computed state
    return dp[idx];
}

// performs a dfs traversal on the text string using the
// splitIndex values that we calculated in the above function
// @param idx: start index for substring
// s : segments formed till current index with delimiters
void getValidStrings(int idx, string &s, string &text, vector<string> &result,
                     vector<vector<int>> &splitIndex)
{
    int len = text.length();

    // stores index of characters appended
    int ptr = idx;
    // initial length of the segmented string
    int initialLen = s.length();

    // breaking condition
    if (idx == len)
    {
        rstrip(s);
        result.push_back(s);
        return;
    }

    // iterate on every split index location
    for (int i = 0; i < splitIndex[idx].size(); i++)
    {
        // append chars till ith split index
        for (; ptr <= splitIndex[idx][i]; ptr++)
        {
            s.push_back(text[ptr]);
        }
        // delimit with white space
        s.push_back(' ');
        // recursively append segments for further substring
        getValidStrings(splitIndex[idx][i] + 1, s, text, result, splitIndex);
        // remove the delimiter, to acomodate next segment starting
        // from idx
        s.pop_back();
    }

    // resizing the segment string to its initial length
    while (s.length() != initialLen)
        s.pop_back();
}

vector<string> solver(vector<string> dictionary, string text)
{
    // hashmap to store to dictionary words
    unordered_set<string> dict;

    // adding all dictionary words to an hash map
    // for faster searching.
    for (int i = 0; i < dictionary.size(); i++)
    {
        dict.insert(dictionary[i]);
    }

    int dp[MAXN];
    vector<vector<int>> splitIndex;
    for (int i = 0; i < MAXN; i++)
    {
        vector<int> tmp;
        splitIndex.push_back(tmp);
    }
    // initializing the dp states
    // here -1 means uncomputed state
    memset(dp, -1, sizeof(dp));

    // check if segmentation is possible
    int totalArrangements = solve(0, dict, text, dp, splitIndex);

    vector<string> results;

    if (totalArrangements > 0)
    {
        string segments = "";
        getValidStrings(0, segments, text, results, splitIndex);
    }

    return results;
}

// ------------------------------ STOP -------------------------------

int main(int argc, char *argv[])
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);

    // int t; cin >> t;
    // while(t--) {
    int n;
    cin >> n;

    string txt;
    vector<string> dictionary;

    for (int i = 0; i < n; i++)
    {
        string word;
        cin >> word;
        dictionary.push_back(word);
    }

    cin >> txt;

    vector<string> result = solver(dictionary, txt);
    // cout << result.size() << "\n";
    if (result.size() > 0)
    {
        for (int i = 0; i < result.size(); i++)
        {
            cout << result[i];
            if (i != (result.size() - 1))
                cout << endl;
        }
    }
    // // if(t)
    // //     cout << endl;
    // }
    return 0;
}
'''
'''
OPTMIAL SOLUTION 2
#include "iostream"
#include "unordered_set"
#include "vector"
#include "string"

using namespace std;

// ------------------------------ START ------------------------------

const int MAXN = 1000;

void rstrip(string &s)
{
    int l = s.length();
    int cnt = 0;
    for (int i = l - 1; i > 0; i--)
    {
        if (s[i] == ' ')
            cnt++;
        else
            break;
    }
    while (cnt--)
        s.pop_back();
}

vector<string> solver(vector<string> dict, string text)
{
    unordered_set<string> dict_hash_set(dict.begin(), dict.end());
    int text_len = text.length();

    vector<vector<string>> ans(text_len, vector<string>(0));

    for (int i = 0; i < text_len; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            string sub_text = text.substr(j, i - j + 1);

            if (dict_hash_set.find(sub_text) != dict_hash_set.end())
            {
                if (j == 0)
                {
                    ans[i].push_back(sub_text);
                }
                else
                {
                    for (const string &s : ans[j - 1])
                    {
                        ans[i].push_back(s + " " + sub_text);
                    }
                }
            }
        }
    }

    return ans[text_len - 1];
}

// ------------------------------ STOP -------------------------------

int main(int argc, char *argv[])
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);

    // int t; cin >> t;
    // while(t--) {
    int n;
    cin >> n;

    string txt;
    vector<string> dictionary;

    for (int i = 0; i < n; i++)
    {
        string word;
        cin >> word;
        dictionary.push_back(word);
    }

    cin >> txt;

    vector<string> result = solver(dictionary, txt);
    // cout << result.size() << "\n";
    if (result.size() > 0)
    {
        for (int i = 0; i < result.size(); i++)
        {
            cout << result[i];
            if (i != (result.size() - 1))
                cout << endl;
        }
    }
    // // if(t)
    // //     cout << endl;
    // }
    return 0;
}
'''
