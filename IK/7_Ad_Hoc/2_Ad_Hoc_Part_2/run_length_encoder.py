'''
Run Length Encoder
Problem Statement:
Compress a string (only has alphabet characters), with basic encoding, where you simply count the number of repeated characters.
 Then also write a routine to decompress it.
e.g.
Input: "AAAAA"
Output: "5A"
Input: "BAAAB"
Output: "B3AB"
Input: "ABAB"
Output: "ABAB" [We are not concerned about characters repeating in groups]
Assume that a given character will not repeat more than 127 times.
Input format:
There is only one argument named strInput denoting the input string.
Output format:
Return the compressed string
Constraints:
String consists of alphabetic characters only
1 <= length_of_input_string <= 6500
Sample Test Cases:
Sample Input 1:
AAAAA
Sample Output 1:
5A
Explanation 1:
Character “A” is repeated 5 times consecutively.
Sample Input 2:
ABaaaBCC
Sample Output 2:
AB3aB2C
Explanation 2:
Character “a” is repeated 3 times in consecutively, character “C” is repeated 2 times consecutively.
'''
import sys

sys.setrecursionlimit(101000)

# complete the function below
def RLE(strInput):
    pass



def main():
    s = input()
    result = RLE(s)
    print(result)

main()

'''
We have provided only optimal solution for this problem. The problem asks to encode the input string in such a way so 
that it’s length remain same or decrease. To do so, we counted repeated consecutive characters. If the count is more 
than one, we replaced the repeated portion by the number following the character only.

Time complexity:
O(N)

Auxiliary space:
O(N) because of storing output

Space complexity:
Including input, O(N).
'''
'''
#include <bits/stdc++.h>

using namespace std;

// ============================ Start ============================

string convertToString(int num){
    string ret="";
    while(num>0){
        int rem = num % 10;
        ret+=(char)(rem+'0');
        num/=10;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

string RLE(string strInput){
    string ans="";
    int cnt=1;
    char prev = strInput[0];
    for(int i=1;i<strInput.length();i++){
        if(strInput[i]==prev){
            cnt++;
        } else {
            if(cnt>1){
                ans+=convertToString(cnt);
            }
            ans+=prev;
            cnt=1;
            prev = strInput[i];
        }
    }
    if(cnt>1){
        ans+=convertToString(cnt);
    }
    ans+=prev;
    return ans;
}

// ============================ End ============================

void solve(string inputFile, string outputFile){
    ifstream fin(inputFile);
    ofstream fout(outputFile);
    cerr<<"Running "<<inputFile<<endl;
    int testCase;
    fin>>testCase;
    for(int i=0;i<testCase;i++){
        string s;
        fin>>s;
        string ans = RLE(s);
        fout<<ans<<endl;
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}    
'''


