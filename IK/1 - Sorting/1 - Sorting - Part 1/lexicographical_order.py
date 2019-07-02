import sys
import os

'''
Problem Statement:
Given a string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS and VALUES
can repeat.
Your task is to find, for each unique key, the number of values with that key and the value with the highest
lexicographical order (also called alphabetical order and dictionary order).
(Have a look at the sample test cases for more clarity.)

Input Format:
You will be given one string array named arr of size N containing KEYS and VALUES separated by one space, where KEYS
and VALUES can repeat.

Output Format:
Return a String array with an entry for each unique key. Each entry should contain key, number of values corresponding
to that key and value with the highest lexicographical order in the below format:

"<KEY>:<COUNT>,<HIGHEST_LEXICOGRAPHICAL_VALUE>"

Order of the output does not matter.

Constraints:
1 <= N <= 10^4
1 <= Length(KEYS) <= 256
1 <= Length(VALUES) <= 800

KEYS can repeat.
VALUES can repeat.
Keys and values will contain only small letters and numerics.

Sample Test Case:
Sample Input-1:
arr = [
  “key1 abcd”,
  “key2 zzz”,
  “key1 hello”,
  “key3 world”,
  "key1 hello"
]

Sample Output-1:
One possible output (you can return strings in any order):
[
  "key1:3,hello",
  "key2:1,zzz",
  "key3:1,world"
]

Sample Input-2:
arr = [
  “mark zuckerberg”,
  “tim cook”,
  “mark twain”
]

Sample Output-2:
One possible output (you can return strings in any order):
[
  "mark:2,zuckerberg",
  "tim:1,cook"
]
'''

def lexicographical_order(arr):
    if len(arr) == 0:
        return []
    result = []
    arr.sort()
    occurances = 1
    key,value = arr[0].split(' ')
    for i in range(1, len(arr)):
        k,v = arr[i].split(' ')
        if k == key:
            occurances += 1
            if v > value:
                value = v
        else:
            result.append('{}:{},{}'.format(key,occurances,value))
            occurances = 1
            key = k
            value = v
    result.append('{}:{},{}'.format(key,occurances,value))
    return result

if __name__ == "__main__":
    f = sys.stdout

    arr_count = int(input())

    arr = []

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    res = lexicographical_order(arr)

    f.write('\n'.join(res))
    f.write('\n')

    f.close()


arr =  [
  'key1 abcd',
  'key2 zzz',
  'key1 hello',
  'key3 world',
  'key1 hello'
]
print(lexicographical_order(arr))
arr = [
  'mark zuckerberg',
  'tim cook',
  'mark twain'
]
print(lexicographical_order(arr))



'''
=== EDITORIAL ===
Optimal solution
Optimal solution will be to use two maps, one to maintain the count and other one to maintain max value.

For every entry you get, you increment the count to the corresponding key and put maximum of the current value and the 
value corresponding to that key in the map.

Note:
Comparing two string with length N is O(N) operation.

Space Complexity: O(n*(MAX_LENGTH(KEYS)+MAX_LENGTH(VALUES)))
Time Complexity: O(n*(MAX_LENGTH(VALUE))

import java.util.TreeSet;

public class OptimalSolution {
    /*
     * Space Complexity: O(n*(MAX_LENGTH(KEYS)+MAX_LENGTH(VALUES)))
     * Time Complexity: O(n*(MAX_LENGTH(VALUE))
     */
    private static String[] originalSolution(String[] arr) {
        // Map to store a count for every key
        HashMap<String, Integer> count = new HashMap<>();
        // Map to store maximum String value for each key
        HashMap<String, String> maxValue = new HashMap<>();
        
        for (String x : arr) {
            // Split on space to seperate key and value
            String splits[] = x.split(" ");
            String key = splits[0];
            String value = splits[1];
            
            // If count contains the key, add 1 to it
            if (count.containsKey(key)) {
                count.put(key, count.get(key) + 1);
            }
            // Else put the value in map with count value 1
            else {
                count.put(key, 1);
            }
            
            // If maxValue contains key, put in map max of both values
            if (maxValue.containsKey(key)) {
                String value1 = maxValue.get(key);
                String value2 = value;
                if (value1.compareTo(value2) < 0) {
                    // value2 is greater
                    maxValue.put(key, value2);
                } else {
                    // value1 is greater
                    maxValue.put(key, value1);
                }
            }
            // Else add the new value
            else {
                maxValue.put(key, value);
            }
        }
        
        String answer[] = new String[count.size()];
        int pointer = 0;
        for (String key : count.keySet()) {
            answer[pointer++] = key + ":" + count.get(key) + "," + maxValue.get(key);
        }
        return answer;
    }
}

'''
