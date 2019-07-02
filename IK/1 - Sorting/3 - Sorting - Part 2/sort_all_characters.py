import math
import os
import random
import re
import sys
'''
Sort All Characters
Problem Statement:
You have to sort an array of characters containing alphanumeric characters along with some other characters
- ‘!’, ’@’, ’#’, ’$’, ’%’, ’^’, ’&’, ’*’, ’(‘, ’)’. You are given a character array named arr.

Input/Output Format For The Function:
Input Format:
There is only one argument in input, a character array named arr.

Output Format:
Return a character array result, containing characters in sorted order of their ASCII values. You can overwrite
the existing array.

Input/Output Format For The Custom Input:
Input Format:
The first line contains the size, n, of the character array. Next n lines each contain the characters present in
the array, with each character of the array in a new line.

If arr = {a,z,i,#,&,l,c} then input should be:
7
a
z
i
#
&
l
c

Output Format:
Output each character of the array on a new line, in sorted order of their ASCII values.

For above input - arr = {a,z,i,#,&,l,c}, output will be:
#
&
a
c
i
l
z

Constraints:
1 <= length(arr) <= 100000

Sample Test Case:
Sample Input:
10
a
s
d
f
g
*
&
!
z
y

Sample Output:
!
&
*
a
d
f
g
s
y
z

Explanation:
Ascii values of the characters present in the character array are:
a: 97, s: 115, d: 100, f: 102, g: 103, *: 42, &: 38, !: 33, z: 122, y: 121.
Now sorting them according to their ascii values results in the given output.
'''

#
# Complete the 'sort_array' function below.
#
# The function accepts Character Array arr as parameter.
#

def sort_array(arr):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = sys.stdout

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = input()[0]
        arr.append(arr_item)

    result = sort_array(arr)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

'''
We have provided three solutions and all the solutions contain necessary comments to understand the approach used:

1) brute_force solution.java
Time Complexity (assuming the length of the given character array is “n”, input arguments are already given and 
excluding time used in the declaration of output):
O(n ^ 2).
The algorithm that we are using is selection sort. We are finding the minimum value of character present among 
remaining characters in each iteration. Since the size of the character array is n we will be iterating the entire 
array n times (that is O(n) iterations) to find n such minimum characters (that is O(n) time for finding minimum value 
during each iteration). Hence, it is O(n^2).

Time Complexity:
Time Complexity (assuming the length of the given character array is “n”, input arguments are already given and 
excluding time used in the declaration of output) is O(n ^ 2).
Input is O(n).
Output is also O(n).

Hence, O(n ^ 2) + O(n) + O(n) -> O(n ^ 2).

Auxiliary Space Used:
O(n).

As we are using a character array of the size of the input array to store and sort the characters.  

NOTE: In Java we have to convert from List<Character> to char ch[] = new char[n]; and then back to List<Character>, 
hence auxiliary space used is O(n), but in other languages this is not needed and aux space will be O(1).

Space Complexity:
O(n).

Input is O(n).
Auxiliary space used is O(n).
Output is O(n).

Hence, O(n) + O(n) + O(n) -> O(n).

2) suboptimal_solution.java
Time Complexity (assuming size of the character array is “n”, input arguments are already given and excluding time used 
in the declaration of output):

O(nlogn).
We are using inbuilt sorting function, Collections.sort() which uses randomized quicksort to sort an array. Since the 
average case time complexity of randomized quicksort is O(nlogn), hence it is O(nlogn).

Time Complexity:
Time Complexity (assuming size of the character array is “n”, input arguments are already given and excluding time used
in the declaration of output) is O(nlogn).

Input is O(n).
Output is O(n).
Hence, O(nlogn) + O(n) + O(n) -> O(nlogn).

Auxiliary Space Used:
O(1).

Quicksort is an in place sorting algorithm and hence we do not use any extra space, so auxiliary space used is O(1).

Space Complexity:
O(n).
Input is O(n).
Auxiliary space used is O(1).
Output is O(n).

Hence, O(n) + O(1) + O(n) -> O(n).

3) optimal_solution.java
Time Complexity (assuming size of the character array is “n”, input arguments are already given and excluding time used
in the declaration of output):
O(n).
The algorithm that we are using is counting sort. We create an array named frequency to keep a count of occurrence of 
each character in the input string. The maximum number of different characters possible is 128 so this will be an array
of size 128. We traverse the character array once O(n) and update the frequency array for each character encountered 
during traversal. Finally after the complete iteration of the array, we traverse the frequency array from beginning to 
the end, that is from lowest ascii value to the highest (from index 0 to index 127), and add as many characters to the 
result (which is initially an empty string) as is the frequency of that character. Hence, it is O(n).

NOTE:   We can even use array of length ‘72’ (with some mapping) instead of ‘128’ because in input we are given only 
‘72’ different types of characters, but this is a general solution which works for the input string containing any 
ASCII characters.

Time Complexity:
Time Complexity (assuming size of the character array is “n”, input arguments are already given and excluding time used
in the declaration of output) is O(n).
Input is O(n).
Output is O(n).
Hence, O(n) + O(n) + O(n) -> O(n).

Auxiliary Space Used:
O(1).

We create a frequency array of size 128, which uses extra space O(128). Hence it is O(1).

Space Complexity:
O(n).

Input is O(n).
Auxiliary space used is O(1).
Output is O(n).

Hence, O(n) + O(1) + O(n) -> O(n).
'''

'''
// BRUTE FORCE
import java.io.*;
import java.util.*;

public class brute_force_solution{

    public static void main(String[] args) throws IOException{
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Character> arr = new ArrayList<>();

        for (int i = 0; i < arrCount; i++) {
            char arrItem = bufferedReader.readLine().charAt(0);
            arr.add(arrItem);
        }

        List<Character> ch = Result.sort_array(arr);

        for (int i = 0; i < ch.size(); i++) {
            bufferedWriter.write(String.valueOf(ch.get(i)));

            if (i != ch.size() - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
class Result {


    /*====================START========================*/
    public static List<Character> sort_array(List<Character> arr) {
        int n = arr.size();
        char ch[] = new char[n];
        for(int i = 0; i<n; i++) ch[i] = arr.get(i);
        for(int i = 0; i<n; i++){
            char min = ch[i]; // stores minimum character encountered so far
            int temp = i; // stores the position of the minimum character
            for (int j = i+1; j<n; j++){
                if(ch[j]<min){
                    min = ch[j]; /*updating the min value whenever we 
                                 encounter a character having a lower ascii value.*/
                    temp = j; /*updating the temp value with the position 
                              of the character having a lower ascii value.*/
                }
            }
            char c = ch[i];
            ch[i] = min;
            ch[temp] = c; 
        }
        List<Character> result = new ArrayList<>();
        for(char c: ch) result.add(c); 
        return result;
    }
    /*====================END========================*/
}
'''

'''
// OPTIMAL SOLUTION
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class optimal_solution{


    public static void main(String[] args) throws IOException{
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Character> arr = new ArrayList<>();

        for (int i = 0; i < arrCount; i++) {
            char arrItem = bufferedReader.readLine().charAt(0);
            arr.add(arrItem);
        }

        List<Character> result = Result.sort_array(arr);

        for (int i = 0; i < result.size(); i++) {
            bufferedWriter.write(String.valueOf(result.get(i)));

            if (i != result.size() - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }

}
class Result {

    /*====================START========================*/
    public static List<Character> sort_array(List<Character> arr) {
        int frequency[] = new int[128]; /*an array to store the number of 
                                        occurence of each character in the string*/
        for(char c : arr){
            frequency[c]++;
        }
        arr.clear();
        for(int i  = 0; i<128;i++){ /*traversing from charcter having 
                              lowest ascii value to that of highest ascii value*/
            for(int j = 0; j<frequency[i]; j++){
                arr.add((char)i); /*appending the result with the 
                        number of occurences of character in the string*/
            }
        }
        return arr;
    }
    /*====================END========================*/
}
'''
