import math
import os
import random
import re
import sys
'''
Nearest Neighbours
Problem Statement:
Given a point p, and other n points in two-dimensional space, find k points out of n points which are nearest to p.
NOTE: Distance between two points is measured by the standard Euclidean method.

Input/Output Format For The Function:
Input Format:
There are 4 arguments in input, an integer p_x, which is the x coordinate of point p, integer p_y, which is the y
coordinate of point p, an integer k and a 2D integer array of points n_points.

Output Format:
Return a 2D integer array result, which contains k points, nearest to point p.

Input/Output Format For The Custom Input:
Input Format:
The first line of input contains x coordinate of point p, p_x. The next line contains y coordinate of point p, p_y.
The next line contains integer k. The next line contains the number of rows n in array points and the following line
contains c, the number of columns in array points. It is guaranteed that c = 2 always. The following n lines contain 2
integers each, the x and y coordinates of a point.

Example:
0
0
2
3
2
1 1
0 1
1 0

Output Format:
Output k lines, each line contains two integers each representing x and y coordinates.

For the above input, the output will be:
0 1
1 0

Constraints:
1 <= n <= 100000
-1000000000 <= coordinates of the points <=1000000000
k <= total number of points in array points.


Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
1
1
1
2
2
0 0
1 0

Sample Output 1:
1 0

Explanation 1:
The distance of point {0,0} from point p{1,1} is sqrt(2) and that of point {1,0} is 1. We need to choose 1(k) point
having the minimum distance from point p. So it is {1,0}.

Sample Test Case 2:
Sample Input 2:
1
1
2
3
2
1 0
2 1
0 1

Sample Output 2:
1 0
2 1

Explanation 2:
Here, we can see that there are all the points are at the same distance from point p. So the answer can be any 2 points.
 Here {{1,0},{0,1}} and {{2,1},{0,1}} are equally acceptable answers.
'''

'''
Complete the 'nearest_neighbours' function below.
The function accepts integer p_x, p_y, k and a 2 D integer array n_points as parameter.
'''

def nearest_neighbours(p_x, p_y, k, n_points):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = sys.stdout

    p_x = int(input().strip())

    p_y = int(input().strip())

    k = int(input().strip())

    n_points_rows = int(input().strip())
    n_points_columns = int(input().strip())

    n_points = []

    for _ in range(n_points_rows):
        n_points.append(list(map(int, input().rstrip().split())))

    result = nearest_neighbours(p_x, p_y, k, n_points)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


'''
=== EDITORIAL ===
We have provided three solutions and all the solutions contain necessary comments to understand the approach used:
1) brute force solution.java
Description:
We compute the distance of each and every point present in array n_points from point p. After this, we sort the points 
present in array n_points according to their distances from point p in ascending order. Now we simply take the first k 
points from the array and append them to the result.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*log(n)) where n is the size of array n_points.
As we are computing the distance of each and every point present in array n_points from point p this will take O(n) and 
sorting them takes O(n*log(n)) time.

Time Complexity:
O(n*log(n)) where n is the size of array n_points.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is
 O(n*log(n)), to read input it will take O(n) and to initialise output array it will take O(k) hence total complexity 
 will be O(n*log(n)) + O(n) + O(k) → O(n*log(n)).

Auxiliary Space Used:
O(n) where n is the size of array n_points.
As we create an auxiliary array to store the distances of all the points present in array n_points from point p. It 
will take extra space equal to the number of points hence it will be O(n).
Space Complexity:
O(n+k) where n is the size of array n_points and k is the number of points nearest to point p, to be returned as output.
For storing input it would take O(n), as we are storing the points in array n_points and auxiliary space used is O(n) 
and O(k) to store output, hence total complexity will be O(n) + O(n) + O(k) → O(n+k).
2) suboptimal_solution.java
Description:
We compute the distance of each and every point present in array n_points from point p. Along with this, we create a 
max heap and add the point whose distance we computed into the max heap. After each insertion, we check if the size of
the max heap is less than or equal to k. If it is greater than k, we poll the maximum value out of it. Thus after 
insertion of all the points present in array n_points, and polling as per the condition mentioned, we will be left with
k points having minimum distance.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*log(k)) where n is the size of the array n_points and k is the number of points nearest to point p, to be returned 
as output.
As we compute the distance of each point present in array n_points from point p and also maintain a max heap of size k,
 the complexity is O(n*log(k)).
Time Complexity:
O(n*log(k)) where n is the size of the array n_points and k is the number of points nearest to point p, to be returned 
as output.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is 
O(n*log(k)), to read input it will take O(n) and to initialise output array it will take O(k) hence total complexity 
will be O(n*log(k)) + O(n) + O(k) → O(n*log(k)).

Auxiliary Space Used:
O(k) where k is the number of points nearest to point p, to be returned as output.
As we maintain a max heap of size k to store the k elements having the minimum distance from point P. It will take O(k) 
of extra space.

Space Complexity:
O(n+k) where n is the size of the array n_points and k is the number of points nearest to point p, to be returned as 
output.
For storing input it would take O(n), as we are storing the points in array n_points and auxiliary space used is O(k) 
and O(k) to store output, hence total complexity will be O(n) + O(k) + O(k) → O(n+k).
3) optimal_solution.java

Description:
We compute the distance of each and every point present in array n_points from point p. Now we need to select k points 
having the minimum distance. For this, we use the quickselect algorithm which is a subpart of the quicksort algorithm. 
We randomly shuffle the array to reduce the average case running time of quicksort algorithm. We choose a pivot and 
split the array by the pivot. Now, if the position of pivot decides which array should we split. Note that here we do 
not need to sort each and every subarray, we will only sort the subarrays which we require. This part is commented well 
in the code “optimal_solution.java”. Please refer to it in case of any query.
NOTE: To learn more about the quickselect algorithm, please go through the following link: 
https://www.geeksforgeeks.org/quickselect-algorithm/

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n) where n is the size of the array n_points.
We compute the distance of each point present of array n_points in O(n). On average, the number of operations required 
for sorting (only selective sub arrays and skipping the ones not required) turns out to be 
n + n/2 + n/4 + ... ~ 2*n = O(n).
Time Complexity:
O(n+k) where n is the size of the array n_points and k is the number of points nearest to point p, to be 
returned as output.

As time complexity assuming that input arguments are already given and excluding time used in declaration of 
output is O(n), to read input it will take O(n) and to initialise output array  it will take O(k) hence total 
complexity will be O(n) + O(n) + O(k) → O(n+k).

Auxiliary Space Used:
O(n) where n is the size of the array n_points.

As we create an array to store the distance of each point present in array n_points from point p. It will take extra 
space of O(n).
Space Complexity:
O(n+k) where n is the size of the array n_points and k is the number of points nearest to point p, to be returned as 
output.

For storing input it would take O(n), as we are storing the points in array n_points and auxiliary space used is O(n) 
and O(k) to store output, hence total complexity will be O(n) + O(n) + O(k) → O(n+k).


'''


'''
// BRUTE FORCE

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

    /*============================== START =========================================*/
    public static List<List<Integer>> nearest_neighbours(int p_x, int p_y, int k, List<List<Integer>> n_points) {
        int len = n_points.size();
        /*Point is a class with two attributes for each point 
        present n_points- index and distance from point P.*/
        Point[] pnt = new Point[len]; 
        /*We fill the values in pnt array accordingly*/
        for(int i = 0; i<len; i++) {
            int x = n_points.get(i).get(0), y = n_points.get(i).get(1);
            pnt[i] = new Point(i, Math.sqrt((p_x-x)*1l*(p_x-x) + (p_y-y)*1l*(p_y-y)));
        }
        /*We sort the point array according to distance, that means the point
        having least distance from point P would be at the lowest index (index 0) and the
        point with the maximum distance would be at the last index.*/
        Arrays.sort(pnt);
        List<List<Integer>> result = new ArrayList<>();
        /*We simply take the top k points and return them as the answer*/
        for(int i = 0; i < k; i++){
            int index = pnt[i].index;
            result.add(n_points.get(index));
        }
        return result;
    }

    static class Point implements Comparable<Point>{
        int index;
        double dist;

        public Point(int i, double dist){
            this.index = i;
            this.dist = dist;
        }

        public int compareTo(Point p){
            return Double.compare(this.dist,p.dist);
        }
    }
/*============================== END =========================================*/
}


class Solution {
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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int p_x = Integer.parseInt(bufferedReader.readLine().trim());

        int p_y = Integer.parseInt(bufferedReader.readLine().trim());

        int k = Integer.parseInt(bufferedReader.readLine().trim());

        int n_pointsRows = Integer.parseInt(bufferedReader.readLine().trim());
        int n_pointsColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> n_points = new ArrayList<>();

        IntStream.range(0, n_pointsRows).forEach(i -> {
            try {
                n_points.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<List<Integer>> result = Result.nearest_neighbours(p_x, p_y, k, n_points);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }
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
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
    /*============================== START =========================================*/
    public static List<List<Integer>> nearest_neighbours(int p_x, int p_y, int k, List<List<Integer>> n_points) {
        int len = n_points.size();
        /*Point is a class with two attributes for each point 
        present n_points- index and distance from point P.*/
        Point[] pnt = new Point[len];
        for(int i = 0; i<len; i++){
            int x = n_points.get(i).get(0), y = n_points.get(i).get(1);
            pnt[i] = new Point(i, Math.sqrt((p_x-x)*1l*(p_x-x) + (p_y-y)*1l*(p_y-y)));
        }
        /*Shuffle the array points*/
        pnt = shuffle(pnt,new Random());
        List<List<Integer>> result = new ArrayList<>();
        topK(pnt,k);
        for(int i = 0; i<k; i++){
            result.add(n_points.get(pnt[i].index));
        }
        return result;
    }

    /* Get k points having least distance from point P.*/
    public static void topK(Point[] points, int k){
        int left = 0, right = points.length - 1;
        /*We just need the k smallest points. We dont care whether they are 
        sorted or not. Similarly once we get the smallest possible k elements, 
        we can skip sorting of unnecessary sub arrays.*/
        while(left<right){
            int part = split(points, left, right);
            if (part==k) {
                return;
            } 
            else if(part<k) {
                left=part+1;
            } 
            else{
                right=part-1;
            }
        }
    }

    /*Shuffles the array randomly*/
    public static Point[] shuffle(Point[] a, Random gen){
        for (int i = 0, n = a.length; i < n; i++){
            int ind = gen.nextInt(n - i) + i;
            Point d = a[i];
            a[i] = a[ind];
            a[ind] = d;
        }
        return a;
    }

    /*Similar to the partition function of quicksort. It partitions the array along the pivot 
    such that elements left to the pivot are smaller than it and to the right are larger than it.*/
    public static int split(Point[] points, int left, int right) {
        Point piv = points[left];
        int i = left, j = right + 1;
        while (true) {
            while (i < right && points[++i].compareTo(piv) < 0);
            while (j > left && points[--j].compareTo(piv) > 0);
            if (i >= j) {
                break;
            }
            Point temp = points[i];
            points[i] = points[j];
            points[j] = temp;
        }
        Point temp = points[j];
        points[j] = points[left];
        points[left] = temp;
        return j;
    }
    static class Point implements Comparable<Point>{
        int index;
        double dist;

        public Point(int i, double dist){
            this.index = i;
            this.dist = dist;
        }

        public int compareTo(Point part){
            return Double.compare(this.dist,part.dist);
        }
    }
    /*============================== END =========================================*/
}


class Solution {
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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int p_x = Integer.parseInt(bufferedReader.readLine().trim());

        int p_y = Integer.parseInt(bufferedReader.readLine().trim());

        int k = Integer.parseInt(bufferedReader.readLine().trim());

        int n_pointsRows = Integer.parseInt(bufferedReader.readLine().trim());
        int n_pointsColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> n_points = new ArrayList<>();

        IntStream.range(0, n_pointsRows).forEach(i -> {
            try {
                n_points.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<List<Integer>> result = Result.nearest_neighbours(p_x, p_y, k, n_points);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }
}
'''
