'''
Valid Expression
Problem Statement:
You have to check whether a given string is a valid mathematical expression or not. The given string is considered to be
 valid if it contains matching opening and closing parenthesis as well as valid mathematical operations. The string contains
 the following set of parentheses ‘(‘, ’)’, ’[’, ’]’, ’{’, ’}’, numbers from 0 to 9 and following operators ‘+’, ’-’ and
 ‘*’. A expression containing only parentheses is considered to be valid if it contains correct opening and closing parenthesis.
 Example: “{()}” is considered valid.
Input/Output Format For The Function:
Input Format:
There is a single argument in the input, a string named expression.
Output Format:
Return a Boolean value of true if the expression is valid else return the value false.
Input/Output Format For The Custom Input:
Input Format:
The first line of input contains string expression.
If expression = “(1+2)*3” then input should be:
(1+2)*3
Output Format:
Output in a single line an integer value which is either 1 or 0 if the result is true and false respectively.
For input expression = “(1+2)*3”
1
Constraints:
    * 1 <= length(expression) <= 100000
    * Characters in expression string can be from ‘+’, ‘-’, ‘*’ and [0-9].

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
{(1+2)*3}+4
Sample Output 1:
1
Explanation 1:
We can clearly see that the above expression is a valid mathematical expression, as well as the parentheses, are valid.

Sample Test Case 2:
Sample Input 2:
((1+2)*3*)
Sample Output 2:
0
Explanation 2:
Here the parentheses are valid but the mathematical expression is not valid. There is an operator ‘*’ without any operand after it.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_valid' function below.
#
# The function accepts STRING expression as parameter.
#

def is_valid(expression):
    pass


if __name__ == '__main__':
    fptr = sys.stdout
    expression = input()
    result = is_valid(expression)
    fptr.write(str(int(result)) + '\n')
    fptr.close()

'''
We have provided a solution and the solutions contain necessary comments to understand the approach used:
1) solution.java
Description:
We traverse the string from left to right and maintain 2 stacks – one for numbers and the other one for operators and parentheses.
 When we encounter a number we push it to the integer stack and similarly, in case of an operator or an open bracket, we
 push it to the character stack. When we encounter a closed bracket, we remove characters from the character stack until
 we encounter the corresponding open parentheses. Also, when we get an operator we remove 2 integers from the integer stack.
 In case we are not able to perform any of the operations, we return false, thus considering the expression invalid.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n) where n denotes the length of the expression string.
As each character of the string enters one of the stacks at most 1 time and is removed from it at most one time, the complexity
 of the algorithm turns out to be O(n).
Time Complexity:
O(n) where n denotes the length of the expression string.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(n),
 to read input it will take O(n) and to store output it will take O(1) hence total complexity will be O(n) + O(n) + O
(1) → O(n).
Auxiliary Space Used:
O(n) where n denotes the length of the expression string.
We create 2 stacks for storing the appropriate characters and numbers respectively, so the auxiliary space used is O(n)
 + O(n) = O(n).
Space Complexity:
O(n) where n denotes the length of the expression string.
We will require O(n) space to store input and auxiliary space used is O(n) and O(1) to store output, hence total complexity
 will be O(n).
'''
'''
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
    //----------------------------START--------------------------------
    public static boolean is_valid(String expression) {
        boolean result = true;
        /*stores digits*/
        Stack<Integer> st1 = new Stack<>();
        /*stores operators and parantheses*/
        Stack<Character> st2 = new Stack<>();
        boolean isTrue = true;
        for (int i = 0; i < expression.length(); i++) {
            char temp = expression.charAt(i);
            /*if the character is a digit, we push it to st1*/
            if (isDigit(temp)) {
                st1.push(temp - '0');
                if(isTrue) {
                    isTrue = false;
                }
                else {
                    return false;
                }
            } 
            /*if the character is an operator, we push it to st2*/
            else if (isOperator(temp)) {
                st2.push(temp);
                isTrue = true;
            } 
            else {
                /*if the character is an opening parantheses we push it to st2*/
                if(isBracketOpen(temp)) {
                    st2.push(temp);
                } 
                /*If it is a closing bracket*/
                else {
                    boolean flag = true;
                    /*we keep on removing characters until we find the corresponding
                    open bracket or the stack becomes empty*/
                    while (!st2.isEmpty()) {
                        char c = st2.pop();
                        if (c == getCorrespondingChar(temp)) {
                            flag = false;
                            break;
                        } 
                        else {
                            if (st1.size() < 2) {
                                return false;
                            }
                            else {
                                st1.pop();
                            }
                        }
                    }
                    if (flag) {
                        return false;
                    }

                }
            }
        }
        while (!st2.isEmpty()) {
            char c = st2.pop();
            if (!isOperator(c)) {
                return false;
            }
            if (st1.size() < 2) {
                return false;
            }
            else {
                st1.pop();
            }
        }
        if (st1.size() > 1 || !st2.isEmpty()) {
            return false;
        }
        return result;
    }
    /*method to get corresponding opening and closing bracket.*/
    public static char getCorrespondingChar(char c) {
        if (c == ')') {
            return '(';
        }
        else if (c == ']') {
            return '[';
        }
        return '{';
    }

    /*checks if the given bracket is open or not.*/
    public static boolean isBracketOpen(char c) {
        if (c == '(' || c == '[' || c == '{') {
            return true;
        }
        return false;
    }

    /*checks if the given character is a digit.*/
    public static boolean isDigit(char c) {
        if (c >= '0' && c <= '9') {
            return true;
        }
        return false;
    }

    public static boolean isOperator(char c) {
        if (c == '+' || c == '-' || c == '*') {
            return true;
        }
        return false;
    }
    //----------------------------END--------------------------------
}

class Solution {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while(t-->0) {
            String expression = sc.nextLine();
            if(Result.is_valid(expression) == true) {
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        }
    }
}
'''
