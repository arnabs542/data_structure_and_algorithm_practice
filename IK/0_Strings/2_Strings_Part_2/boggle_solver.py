'''
Boggle Solver
Problem Statement:
You are given a dictionary set dictionary that contains dictionaryCount distinct words and a matrix mat of size n*m.
Your task is to find all possible words that can be formed by a sequence of adjacent characters in the matrix mat.
Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell of
 the matrix.
Note: Same dictionary word can be found in the matrix multiple times. We only need to check the existence of the dictionary
 word in the matrix. Hence, for multiple existences for the same word only add it once in the list of all found words.
Input/Output Format For The Function:
Input Format:
The first parameter of the function that is to be implemented is the matrix mat and the second parameter dictionary is a
 list of strings that are to be searched in the matrix mat.
Output Format:
Return array of strings containing all possible words from the dictionary that could be found in the matrix mat.
Input/Output Format For The Custom Input:
Input Format:
The first line contains one single integer denoting the value of dictionaryCount.
Next dictionaryCount lines of input, each line contains one single string denoting the word in the dictionary.
Next two lines contain one integer each denoting n and m respectively. Next, n lines contain one string of length m, denoting
 the matrix mat.
If dictionary = [ ‘’hat”, “world” ] and mat [ “aaa”, “hat”, “ccc”], then the corresponding custom input will be:
2
hat
world
3
3
aaa
hat
ccc
Output Format:
Print all the dictionary words found in the matrix mat in a separate line.
For the above-provided custom input only one word is found and hence the custom output looks like:
hat
Constraints:
1 <= dictionaryCount <= 1000
1<= n*m <= 100000
1<= length(words in dictionary) <= 100
All the characters in mat and words in dictionary are lower case English alphabets.

Sample Test Case:
dictionary = [ “bst” , “heap” , “tree”]
mat = [ “bsh”  , ”tee” , ”arh” ]

Sample Output:
Function returns the list result = [ “bst” , “tree” ]
Explanation:
The input matrix is represented below:
bsh
tee
arh

Assume here top left-most corner is at (0,0) and bottom right-most corner is (2,2).
Presence of “bst” is marked bold in the below representation:
(0,0) -> (0,1) -> (1,0)
bsh
tee
arh

Presence of “tree” is marked bold in the below representation:
(1,0) -> (2,1) -> (1,1) -> (1,2)
bsh
tee
arh
'''
import math
import os
import random
import re
import sys

#
# Complete the 'boggle_solver' function below.
#
#
def boggle_solver(dictionary, mat):
    pass



if __name__ == '__main__':
    dictionary_count = int(input().strip())
    dictionary = []
    for _ in range(dictionary_count):
        word = input().strip()
        dictionary.append(word)
    n = int(input().strip())
    m = int(input().strip())
    mat = []
    for _ in range(n):
        word = input().strip()
        mat.append(word)
    fptr = sys.stdout
    result = boggle_solver(dictionary, mat)
    fptr.write('\n'.join(result))
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution:
Description:
In this approach, we, first of all, insert all the words from the dictionary into a hash map for a linear time lookup operation
 (linear over length of string because it takes linear time to calculate hash of a string). Now, we iterate over all the
 cells of the matrix mat and assume each cell as the first character of the our word and recursively build all the possible
 words by visiting all its neighbouring cells and each we visit its neighbour we keep building the word by appending the
 neighbour’s cell char at the end of our current word. Also, each time we build a word we make a lookup in our hash map.
 If the current state of the word exists in the hash map then we found it in the mat and we add it to the found words set.
 Also, once we found a word we remove it from the HashMap so as to avoid its duplicate match from other words in the mat.
 We repeat this process for all the cells in the matrix mat and keep accumulating all the found words in a common container
 and in the end return this container. Kindly, refer to the solution for a better understanding.
Consider the below example
dictionary = [ “bst” , “abs” , “tab” ]
mat = [ “ast” , “bxt” ]
So, our matrix looks like
a s t
b x r
Now for each cell of the matrix we keep generating all the possible words with max length equal to the max length of word
 in dictionary.
So, we start from mat[0][0] and keep generating all the words in the below manner and at each generation we check its existence
 in the dictionary. The generated words for mat[0][0] are:
a , as , ast ,  asx , asr , asb, abx , abs.
Here we find “abs” in our dictionary so, we add it in our found words container and remove it from the dictionary hashmap.

In similar fashion we generate all possible words considering all other cells of mat as the first character of the word
 and then keep checking their existence in our dictionary hash map.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(max_length_of_string*(n*m)*7^(max_length_of_string)) where n denotes the number of strings in given array mat , m denotes
 the length of a string of given array mat and max_length_of_string is the maximum length of the dictionary word.
Now, consider a cell (i,j) as the first character when we are building our word. Now for first move we can move to 8 directions
 from current cell say (i-1,j) , (i+1,j) , (i,j-1) , (i,j+1) (i-1,j+1) , (i+1,j-1),(i+1,j+1),(i-1,j-1). Now for next moves
 we only have 7 directions as one direction of the 8 possible direction will be the previous visited cell. So, from this
 point on we will be having 7 possible directions to visit for the current cell. So, we can now come-up with a upper bound
 that to form all possible max_length_of_string length words assuming cell (i,j) is the first character it will take O(8
 * 7^(max_length_of_string-1)) ~ O(7 ^ max_length_of_string) time. Therefore, we perform the same operation for all the
 m*n cells in the matrix mat. Now for words that we form from our boggle matrix we do a lookup in our hashmap to check if
 the current word exists in the dictionary. This lookup takes O(max_length_of_string) time. Hence, the total time complexity
 will be O(max_length_of_string*m*n*(7^max_length_of_string)).
Time Complexity:
O(max_length_of_string * ( dictionaryCount + *m*n*(7^max_length_of_string) ) where n denotes the number of strings in given
 array mat , m denotes the length of a string of given array mat , max_length_of_string is the maximum length of the dictionary
 word and dictionaryCount denotes the number of words in dictionary.
The input time is the time taken to read the matrix and the dictionary i.e. O(n*m + dictionaryCount * max_length_of_string).

The output time is the time taken to print the found words in the dictionary which in worst case is O(dictionaryCount*max_length_of_string).
 Hence, the total time complexity is the sum of input time + function time + output time i.e. O(n*m + dictionaryCount *
 max_length_of_string) + O(max_length_of_string*m*n*(7^max_length_of_string)) + O(dictionaryCount*max_length_of_string)
 ~ O(max_length_of_string * ( dictionaryCount + *m*n*(7^max_length_of_string) )
Auxiliary Space Used:
O(dictionaryCount*max_length_of_string) + O(n*m) where dictionaryCount is the number of string in given array dictionary,
 max_length_of_string is the max length of dictionary string and n denotes the number of strings in given array mat and
 m denotes the length of a string of given array mat.
Hash Map consumes O(dictionaryCount*max_length_of_string) space same as the input dictionary. While word building traversals
 we will be also maintaining a 2D visited matrix that tracks the visited cells so as we do not visit it again. This 2D visited
 matrix also consumes O(n*m) space. Recursion stack as we calling the function recursively for any given index (i, j) it
 can be O(n*m).
Hence total auxiliary space used will be O(dictionaryCount*max_length_of_string) + O(n*m).
Space Complexity:
O(dictionaryCount * max_length_of_string) + O(n*m) where dictionaryCount is the number of string in given array dictionary,
 max_length_of_string is the maximum length of strings in array dictionary and n denotes the number of strings in given
 array mat and m denotes the length of a string of given array mat.
For storing input, we are storing dictionaryCount number of string of maximum possible length max_length_of_string and n
 strings of length m each and as auxiliary space used is O(dictionaryCount * max_length_of_string) + O(n*m). Hence total
 complexity will be O(dictionaryCount * max_length_of_string) + O(n*m).
2) optimal_solution:
Description:
In our previous brute force approach we went building our word string cluelessly and each time we build our string any further
 we made a lookup in our hash map to check its existence.
In this approach instead of going blindly in all eight directions from our current cell, we will only visit that neighbour
 that assures that the word with the current prefix exists in the dictionary. Using this we will prune a lot of branches
 in our word building traversal.
Now a few questions/thoughts:
* Which DS to choose to store dictionary words so as it not only gives fast lookups but also suggests the next character to
 look in the matrix for a given prefix word?
We will be choosing Trie as our DS to store all the words from the dictionary. Trie offers same lookup time as that of a
 Hash Map(linear time to calculate hash key) and also suggests the next character for a prefix so as the word formed using
 that char exists in the trie. This feature of the trie is used in autocomplete feature and is widely used in search engines
 to auto-complete your search queries.
 
* Which traversal algorithm to choose for building word(DFS/BFS)?
The optimal solution for this problem also demands the right choice for the traversal algorithm. In case we use a BFS traversal
 we will be building valid words but we will be growing our search branches horizontally which leads to delay in the pruning
 of branches and hence will increase our search space and will affect the time complexity. Whereas in case of DFS we go
 till depth and we are sure that for every depth we step in we are on right child as guided by the trie data structure and
 hence, we will reach our goal word quickly.
Now we will use the same approach as used in the brute force solution. We will iterate over all cells of the matrix mat
 and for each cell we will do a DFS traversal on the matrix assuming that cell as the first character of the word but this
 time we will be using our trie to guide so as we only land on valid neighbours and increase the chance of finding the dictionary
 word.
 
Bonus Optimization Catch
Every time we find a word we simply remove it from the trie. This will ensure that the trie does
 not give a suggestion of the words that are already found in some previous traversals and hence it will prune some more
 DFS branches for us.
 
Consider the below example

dictionary = [ “bst” , “abs” , “tab” ]
mat = [ “ast” , “bxt” ]

So, our matrix looks like
a s t
b x r

Now we iterate on all cells of the above matrix and consider the character as the first character of the word and start
 building our target word. Here unlike the brute force we won’t build all the possible arrangements of words but will only
 build those words which are prefix to any of the dictionary word.
So, here we start from mat[0][0]
    First iteration
word = “a” (prefix of “abs”), now we check if it is in dictionary

    Second iteration , we visit all neighbours and only append that neighbour characters in our word that trie permits( so the
 new word formed is still a prefix of words in dictionary)
 
word = “ab” (prefix of “abs”), now we check if it is in dictionary

Third iteration , again we repeat the same process
word = “abs” (prefix of “abs”), this exists in the dictionary and hence,
 we add this in our found words container and remove the same word from the trie.
We repeat the same process for all other cells of the matrix.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*m*7^(max_length_of_string)) + O(dictionaryCount*max_length_of_string) where dictionaryCount is the number of string
 in given array dictionary, max_length_of_string is the maximum length of strings in array dictionary and n denotes the
 number of strings in given array mat , m denotes the length of a string of given array mat and max_length_of_string denotes
 the maximum length of the dictionary word.
As we are storing each string of array dictionary into trie, it will take O(dictionaryCount*max_length_of_string) as to
 store a string in trie it will take O(max_length_of_string).
The time complexity of the DFS word building step for this approach will also be the same as the brute force approach for
 worst case(kindly refer to the brute force time complexity section). As we are still doing the same DFS traversal as in
 the brute force approach but with some intelligent choices while choosing the direction from the current cell, so as we
 form the target word more quickly. But for worst case we will end up forming all possible words even after the guiding
 given by the trie.
Consider below example :
When our 2D matrix is of size 5*10 and looks like below:
mat = [
“aaaaaaaaaa”,
“aaaaaaaaaa”,
“aaaaaaaaaa”,
“aaaaaaxxxx”,
“aaaaaaxbcd”
]
And now consider our dictionary as
dictionary = [ “aaaaaaaaab” , “aaaaaaaaac”, “aaaaaaaaad”]
As it is evident that the letter ‘b’,’c’ and ‘d’ and being shielded by the cover of ‘x’ layer.
Hence and unfortunately total time complexity  still will be O(n*m*7^(max_length_of_string)) + O(dictionaryCount*max_length_of_string),
 but this is only in worst case. In average and ideal cases this approach performs much better.
Time Complexity:
O(n*m*7^(max_length_of_string) + dictionaryCount*max_length_of_string)) where dictionaryCount is the number of string in
 given array dictionary, max_length_of_string is the maximum length of strings in array dictionary and n denotes the number
 of strings in given array mat , m denotes the length of a string of given array mat
The input time is the time taken to read the matrix and the dictionary i.e. O(n*m + dictionaryCount * max_length_of_string).

The output time is the time taken to print the found words in the dictionary which in worst case is O(dictionaryCount*max_length_of_string).
 Hence, the total time complexity is the sum of input time + function time + output time i.e. O(n*m + dictionaryCount *
 max_length_of_string) + O(n*m*7^(max_length_of_string)) + O(dictionaryCount*max_length_of_string) + O(dictionaryCount*max_length_of_string)
 ~
O(n*m*7^(max_length_of_string) + dictionaryCount*max_length_of_string))
Auxiliary Space Used:
O(n*m) + O(dictionaryCount*max_length_of_string) where dictionaryCount is the number of string in given array dictionary,
 max_length_of_string is the maximum length of strings in array dictionary and n denotes the number of strings in given
 array mat and m denotes the length of a string of given array mat.
Trie consumes O(dictionaryCount*max_length_of_string) space to store dictionaryCount of strings in worst case. While word
 building traversals we will be also maintaining a 2D visited matrix that tracks the visited cells so as we don’t visit
 it again. This 2D visited matrix also consumes O(n*m) space and the recursive stack would take O(max_length_of_string)
 space. So, overall auxiliary space is O(n*m) + O(dictionaryCount*max_length_of_string).
Space Complexity:
O(n*m) + O(dictionaryCount*max_length_of_string) where dictionaryCount is the number of string in given array dictionary,
 max_length_of_string is the maximum length of strings in array dictionary and n denotes the number of strings in given
 array mat and m denotes the length of a string of given array mat.
For storing input, we are storing dictionaryCount number of string of maximum possible length max_length_of_string and n
 strings of length m each and as auxiliary space used is O(n*m) + O(dictionaryCount*max_length_of_string) hence total complexity
 will be O(dictionaryCount*max_length_of_string) + O(n*m).
'''
'''
BRUTE FORCE
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

// ------------------------- START ------------------------------

// validates cell (x,y) of mat
bool ok(int x, int y, vector<string> &mat) {
    // mat dimensions
    int n = mat.size();
    int m = mat[0].size();
    // boundary conditions check
    if (x < 0 or y < 0 or x >= n or y >= m) {
        return false;
    }
    return true;
}

void solveforPosition(int length, int maxLength, int x, int y, vector<string> &mat,
    vector<vector<int>> &vis, unordered_set<string> &dict, vector<string> &result, string &s) {
    // if length of current formed word is greater than max length
    // of dictionary word - we break our recursion
    if (length > maxLength) {
        return;
    }
    // marked current position as visited
    vis[x][y] = 1;
    // build current word s by appending current cell
    s.push_back(mat[x][y]);
    // if current word exists in dictionary
    if (dict.find(s) != dict.end()) {
        // push current word in the result array
        result.push_back(s);
        // remove the current word from dictionary
        dict.erase(s);
    }
    // iterate on all 8 directions
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 and j == 0) {
                continue;
            }
            // if cell (x+i,y+j) is valid and not visited
            if (ok(x + i, y + j, mat) and !vis[x + i][y + j]) {
                // recursively keep building current word
                solveforPosition(length + 1, maxLength, x + i, y + j, mat, vis, dict, result, s);
            }
        }
    }
    // remove current char from the current word built so for
    s.pop_back();
    // mark current cell as non-visited
    vis[x][y] = 0;
}

// @param : dictionary : set of words to be looked in mat
// @param : mat : input matrix
// @return : list of all words found in mat
vector<string> boggle_solver(vector<string> &dictionary, vector<string> &mat) {
    // insert all words from dictionary into hash set dict
    unordered_set<string> dict(dictionary.begin(), dictionary.end());

    // getting maximum length word in dictionary
    int maxWordLength = 0;
    for (auto word : dictionary) {
        maxWordLength = max(maxWordLength, (int)word.length());
    }

    // stores all words found in mat
    vector<string> ret;
    // mat dimensions
    int rows = mat.size();
    int cols = mat[0].size();
    // tracks visited cells of mat
    vector<vector<int>> visited(rows, vector<int>(cols, 0));
    // iterate over all cells of mat
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            vector<string> result;
            string tmp = "";
            // build word for current position and match with dict
            solveforPosition(1, maxWordLength, i, j, mat, visited, dict, result, tmp);
            // add all found words for this cell to overall result ret
            ret.insert(end(ret), begin(result), end(result));
        }
    }
    // return all words found in mat
    return ret;
}
// ------------------------------- STOP ----------------------------------

int main() {
    int dictionary_count;
    cin >> dictionary_count;

    vector<string> dictionary(dictionary_count);

    for (int i = 0; i < dictionary_count; i++) {
        string dictionary_item;
        cin >> dictionary_item;
        dictionary[i] = dictionary_item;
    }

    int n, m;
    cin >> n >> m;
    vector<string> mat;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        mat.push_back(tmp);
    }
    string txt;
    cin >> txt;

    ostream &fout = cout;

    vector<string> result = boggle_solver(dictionary, mat);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != (result.size() - 1)) {
            fout << "\n";
        }
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}
'''
'''
#include "bits/stdc++.h"
using namespace std;

// -------------------------- START -----------------------------
// TrieNode structure
struct TrieNode {
    // stores presence of current node in trie
    int cnt;
    // marks true if current node is end of word in trie
    bool isEnd;
    // stores references to all its children
    TrieNode *child[26];
    // paramtrized constructor
    TrieNode() : cnt(1), isEnd(false) {
        for (int i = 0; i < 26; i++) {
            child[i] = NULL;
        }
    }
};

// inserts key "k" in the trie
void insert(TrieNode *root, string &k) {
    TrieNode *tmp = root;
    int l = k.length();
    for (int i = 0; i < l; i++) {
        int idx = k[i] - 'a';
        if (!tmp->child[idx]) {
            tmp->child[idx] = new TrieNode();
        }
        else {
            tmp->child[idx]->cnt++;
        }
        tmp = tmp->child[idx];
    }
    tmp->isEnd = true;
}

// removes key "s" from the trie
void removeKey(string &s, TrieNode *root) {
    int l = s.length();
    TrieNode *curr = root;
    for (int i = 0; i < l; i++) {
        int idx = s[i] - 'a';
        if (!curr->child[idx]) {
            break;
        }
        TrieNode *tmp = curr->child[idx];
        tmp->cnt--;
        if (tmp->cnt == 0) {
            curr->child[idx] = NULL;
        }
        curr = tmp;
    }
}

bool ok(int x, int y, vector<string> &mat, TrieNode *rt) {
    // mat dimension
    int n = mat.size();
    int m = mat[0].size();
    // basic boundary checks
    if (x < 0 or y < 0 or x >= n or y >= m) {
        return false;
    }
    // basic sanity check
    if (rt == NULL) {
        return false;
    }
    // checking if mat[x][y] exists as child for rt
    if (rt->child[mat[x][y] - 'a'] == NULL) {
        return false;
    }
    return true;
}

void dfs(int x, int y, vector<string> &mat, vector<vector<int>> &vis, TrieNode *root, 
    TrieNode *rt, vector<string> &result, string &res) {
    // check if rt node is end of any word in trie
    if (rt and rt->isEnd == true) {
        // unmark the end node
        rt->isEnd = false;
        // push the current word in the result array
        result.push_back(res);
        // remove the current word from the trie
        removeKey(res, root);
    }

    // mark current node as visited
    vis[x][y] = 1;

    // iterate in all 8 - directions from current cell
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 and j == 0) {
                continue;
            }
            // if this cell(x+i,y+j) is valid and not visited
            if (ok(x + i, y + j, mat, rt) and !vis[x + i][y + j]) {
                int idx = mat[x + i][y + j] - 'a';
                // building the word further
                res.push_back(mat[x + i][y + j]);
                // extend dfs traversal to cell(x+i,y+j)
                dfs(x + i, y + j, mat, vis, root, rt->child[idx], result, res);
                // pop current char from the end of current word
                res.pop_back();
            }
        }
    }
    // mark current cell as non - visited
    vis[x][y] = 0;
}

// @param : dictionary : set of words to be looked in mat
// @param : mat : input matrix
// @return : list of all words found in mat
vector<string> boggle_solver(vector<string> &dictionary, vector<string> &mat) {
    // create a trie
    TrieNode *root = new TrieNode();
    // insert all words from dict in trie
    for (auto word : dictionary) {
        insert(root, word);
    }
    // mat dimensions
    int n = mat.size();
    int m = mat[0].size();
    // visited 2d array to mark visited cells of mat
    vector<vector<int>> vis(n, vector<int>(m, 0));
    // stores all dictionary words found in mat
    vector<string> allFoundWords;

    // iterate over all cells of mat
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // calculate the child to be looked in root trie node
            int idx = mat[i][j] - 'a';

            // check if the respective child node is present in trie
            if (root->child[idx]) {
                // stores words found with first char as mat[i][j]
                vector<string> foundWords;
                string word = "";
                // initializing word's first char
                word.push_back(mat[i][j]);
                // do a dfs traversal at location (i,j)
                dfs(i, j, mat, vis, root, root->child[idx], foundWords, word);
                // insert all words found in current dfs to overall result
                allFoundWords.insert(end(allFoundWords), begin(foundWords), end(foundWords));
            }
        }
    }
    // return the overall list of all found words
    return allFoundWords;
}

// -------------------------------- STOP --------------------------------

int main() {
    int dictionary_count;
    cin >> dictionary_count;

    vector<string> dictionary(dictionary_count);

    for (int i = 0; i < dictionary_count; i++) {
        string dictionary_item;
        cin >> dictionary_item;
        dictionary[i] = dictionary_item;
    }

    int n, m;
    cin >> n >> m;
    vector<string> mat;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        mat.push_back(tmp);
    }
    string txt;
    cin >> txt;

    ostream &fout = cout;

    vector<string> result = boggle_solver(dictionary, mat);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != (result.size() - 1)) {
            fout << "\n";
        }
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}
'''


