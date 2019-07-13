'''
Print A String Sinusoidally
Problem Statement:
[This is just a stupid problem, that has no relation to anything else. It's there primarily because we see it on and off.
 It's a string puzzle disguised as a programming problem]
Also called "SnakeString". For example, the phrase "Google Worked" should be printed as follows (where ~ is the word separator):

    o     ~         k
  o  g  e  W   r   e
G     l        o       d

https://i.imgur.com/GKsJofY.png

Input format:
There is only one argument named s denoting the input string.
Output format:
Print the string in sinusoidally. Format is:
→ There will be 3 rows
→ Print ~ for spaces
→ First character is printed in 1st column of 3rd row
→ Second character is printed in 2nd column of 2nd row
→ Third character is printed in 3rd column of 1st row
→ Fourth character is printed in 4th column of 2nd row
→ Fifth character is printed in 5th column of 3rd row
→ Sixth character is printed in 6th column of 2nd row
→ This process goes on…
Constraints:
String consists of alphanumeric characters and spaces
3 <= length_of_input_string <= 10000
Sample Test Case:
Sample Input:
Google Worked
Sample Output:
    o     ~         k
  o  g  e  W   r   e
G     l        o       d

https://i.imgur.com/PKlQd0w.png

'''
import sys
from collections import deque

sys.setrecursionlimit(101000)


# complete the function below
def printStringSinusoidally(s):
    pass



def main():
    s = input()
    printStringSinusoidally(s)

main()

'''
We have provided only optimal solution for this problem. There are few observations:
→ i’th character of input string is placed in i’th column of a row.
→ 0th index character of string is placed in 3rd row. Then 4th, 8th and go on.
→ 1st index character of string is placed in 2nd row. Then 3rd, 5th and go on.
→ 2nd index character of string is placed in 1st row. Then 6th, 10th and go on.
So, we can construct 3 string representing 3 rows using the above information.

Time complexity:
O(N)

Auxiliary space:
O(3*N) because of a 2D array

Space complexity:
Including input, O(3*N).
'''
'''
#include <bits/stdc++.h>

using namespace std;

// ============================ Start ============================

void printStringSinusoidally(string s, ofstream &fout){
    int len = s.length();
    char wavedString[3][len];
    
    for(int i=0;i<len;i++){
        for(int j=0;j<3;j++){
            wavedString[j][i]=' ';
        }
    }

    for(int i = 2; i < s.length(); i += 4){
        wavedString[0][i] = (s[i]==' ')?'~':s[i];
    }

    for(int i = 1; i<s.length(); i += 2){
        wavedString[1][i] = (s[i]==' ')?'~':s[i];
    }

    for(int i=0;i<s.length(); i += 4){
        wavedString[2][i] = (s[i]==' ')?'~':s[i];
    }
    string firstRow = "";
    string secondRow = "";
    string thirdRow = "";
    
    for(int i=0;i<len;i++){
        firstRow += wavedString[0][i];
        secondRow += wavedString[1][i];
        thirdRow += wavedString[2][i];
    }

    fout<<firstRow<<endl;
    fout<<secondRow<<endl;
    fout<<thirdRow<<endl;
}

// ============================ End ============================

void solve(string inputFile, string outputFile){
    ifstream fin(inputFile);
    ofstream fout(outputFile);
    cerr<<"Running "<<inputFile<<endl;
    int testCase;
    fin>>testCase;
    fin.ignore();
    for(int i=0;i<testCase;i++){
        string s;
        getline(fin,s);
        printStringSinusoidally(s, fout);
        fout<<endl;
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}    
'''
