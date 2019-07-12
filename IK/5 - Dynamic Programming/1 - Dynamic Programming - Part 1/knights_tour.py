'''
Knight's tour!
Problem Statement:
Given a phone keypad as shown below:
1 2 3
4 5 6
7 8 9
- 0 -
How many different phone numbers of given length can be formed starting from the given digit? The constraint is that the
 movement from one digit to the next is similar to the movement of the Knight in a chess game.
For eg. if we are at 1 then the next digit can be either 6 or 8 if we are at 6 then the next digit can be 1, 7 or 0.
Repetition of digits are allowed - 1616161616 is a valid number.
The problem requires us to just give the count of different phone numbers and not necessarily list the numbers.
Find a polynomial-time solution, based on Dynamic Programming.
Input/Output Format For The Function:
Input Format:
You will be given 2 integer values, startdigit and phonenumberlength, denoting starting digit and the required length respectively.

Output Format:
Return a long integer count, denoting the total number of valid phone numbers that can be formed.
Input/Output Format For The Custom Input:
Input Format:
The first line should contain an integer startdigit, denoting the digit from which the phone number should start. The second
 line should contain phonenumberlength, denoting the length of phone number to be formed.
If startdigit = 1 and phonenumberlength = 3, then input should be:
1
3
Output Format:
There will be one line, containing an integer count, denoting result returned by the solution function.
For input startdigit = 1 and phonenumberlength = 3, output will be:
5
Constraints:
0 <= startdigit <= 9
1 <=  phonenumberlength <= 30
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
startdigit = 1
phonenumberlength = 2
Sample Output 1:
2
Explanation 1:
Two possible numbers of length 2: 16, 18
Sample Test Case 2:
Sample Input 2:
startdigit = 1
phonenumberlength = 3
Sample Output 2:
5
Explanation-2:
Possible numbers of length 3: 160, 161, 167, 181, 183
'''
import sys
import os

def numPhoneNumbers(startdigit, phonenumberlength):
    pass



if __name__ == "__main__":
    f = sys.stdout

    startdigit = int(input())

    phonenumberlength = int(input())

    res = numPhoneNumbers(startdigit, phonenumberlength);
    f.write(str(res) + "\n")


    f.close()

'''
Recursive solution
Think of it recursively like this: How many numbers can I construct using 10 digits starting from 1?
Answer is
[number of 9-digit numbers starting from 8] + [number of 9-digit numbers starting from 6]
So how many "9-digit numbers starting from 8" are there? Well,
[number of 8-digit numbers starting from 1] + [number of 8-digit numbers starting from 3]
Hence, we can recursively build this as
f(len, i) = sum(f(len-1, knight neighbours of i))
Base case would be f(0, num), where
f(0, num) = 1, if num = starting digit
f(0, num) = 0, otherwise
Optimal solution
We can memoize the recurrence relationship mentioned above or build an iterative version for the same problem.
Space Complexity: O(phonenumberlength)
Time Complexity: O(phonenumberlength)
'''
'''
import java.util.TreeSet;

public class OptimalSolution {
    /*
     * Space Complexity: O(phonenumberlength)
     * Time Complexity: O(phonenumberlength)
     */
    public static long numPhoneNumbers(int startdigit, int phonenumberlength) {
        
        // List of where integers where you can go from a particular integer
        ArrayList<ArrayList<Integer>> listOfNext = new ArrayList<>();
        
        // 0
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(0).add(4);
        listOfNext.get(0).add(6);
        
        // 1
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(1).add(6);
        listOfNext.get(1).add(8);
        
        // 2
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(2).add(7);
        listOfNext.get(2).add(9);
        
        // 3
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(3).add(4);
        listOfNext.get(3).add(8);
        
        // 4
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(4).add(3);
        listOfNext.get(4).add(9);
        listOfNext.get(4).add(0);
        
        // 5
        listOfNext.add(new ArrayList<Integer>());
        
        // 6
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(6).add(1);
        listOfNext.get(6).add(7);
        listOfNext.get(6).add(0);
        
        // 7
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(7).add(2);
        listOfNext.get(7).add(6);
        
        // 8
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(8).add(1);
        listOfNext.get(8).add(3);
        
        // 9
        listOfNext.add(new ArrayList<Integer>());
        listOfNext.get(9).add(4);
        listOfNext.get(9).add(2);
        
        long numTill[][] = new long[phonenumberlength][10];
        // First digit is already given. So we can only form one number of length 1.
        numTill[0][startdigit] = 1;
        
        for(int i = 1; i < phonenumberlength; i++){
            for(int num = 0; num < 10; num++){
                for(int to:listOfNext.get(num)){
                    // We can come to num from all its neighbours.
                    // So we will add all possible numbers of length i-1 that are neighnours of num.
                    numTill[i][num] += numTill[i-1][to];
                }
            }
        }
        
        long ans = 0;
        // Sum all possible ending of length phonenumberlength
        for(int num = 0; num < 10; num++){
            ans += numTill[phonenumberlength-1][num];
        }
        return ans;
    }
}
'''
