'''
Skyline
Problem Statement:
Given n buildings on a 2D plane, find the skyline of these buildings. Each building on the 2D plane has a start coordinate,
 end coordinate, and height. The skyline is defined as a unique representation of rectangular strips of different heights
 which are created after the overlap of multiple buildings in the 2D plane. Refer this image for clarity, on the left are
 multiple buildings and on the right is the skyline for the same. The output skyline is sorted on the x coordinate of the
 rectangular strip.


 https://i.imgur.com/cR1OSj5.png


Input/Output Format For The Function:
Input Format:
The input of buildings is given in a 2D integer array format. The outer array contains multiple buildings where each building
 is an array of integers of size 3. The first integer represents the start coordinate of the building, the second integer
 represents the end coordinate of the building and the third integer represents its height.
Output Format:
Return a 2D integer array. The outer array has different rectangular strips, each element is an array of size two. The first
 element in the inner array is the x coordinate of the strip and the second element is the y coordinate of the strip (red
 dots in the image above).
Input/Output Format For The Custom Input:
Input Format:
The first line in the input contains an integer n, the number of buildings. The next n lines contain three integers: x, y, height representing the buildings.
Output Format:
Each line represents the unique rectangular strip in a sorted format. Each line has 2 integers, x0, and y0 coordinates respectively of the strip.
Constraints:
1 <= n <= 10^5
1 <= x, y, height <= 2 * 10^9

Sample Test Case:
Sample Input:
5
2 9 10
3 7 15
5 12 12
15 20 10
19 24 8

Sample Output:
2 10
3 15
7 12
12 0
15 10
20 8
24 0

Explanation:
From the image referenced above, we see the blue building at the start and the corresponding red dot in the right image
at (2,10). The next change in skyline occurs at an x coordinate of 3 with red building coming up at the height of 15, so
in the output, the next line is printed as 3 15. Similarly, all the buildings are traversed to find the output as given
in the sample output section.
'''
import math
import os
import random
import re
import sys


#
# Complete the 'findSkyline' function below.
#
# The function accepts 2D_INTEGER_ARRAY buildings as parameter.
# The function is expected to return a 2D_INTEGER_ARRAY.
#
def findSkyline(buildings):
    pass



if __name__ == '__main__':
    fptr = sys.stdout
    buildings_rows = int(input().strip())
    buildings_columns = 3
    buildings = []
    for _ in range(buildings_rows):
        buildings.append(list(map(int, input().rstrip().split())))
    result = findSkyline(buildings)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()


'''
1) optimal_solution.java
Description:
A BuildingIndex class is defined in the solution consisting of three members:
index: it is the value of x-coordinate of the potential skyline point.
startEnd: it is a character that denotes if this
 particular index is a start point or an end point of the building.
height: it is the height of the building.
A priority queue named priorityQ is created. All the start and end points of all the buildings as objects of BuildingIndex
class are added in this queue with the following insertion constraints:
    A lower value of index gets priority.
    If the index values are the same, then 'start' point gets priority.
    If two buildings are starting at the same index, then BuildingIndex with higher height gets priority.
    If two buildings are ending at the same index, then BuildingIndex with smaller height gets priority.
A binary search tree named heightCountQ is created which stores the count of heights ordered by the heights of buildings.

Also, a variable named maxHeight is initialized with 0 which stores the current max height of the skyline.
Now pop elements from the priorityQ, one by one, till it is empty.
    If the popped element is the starting index, then check if it is greater than maxHeight, if so add the start index and height pair to the ans list.
If the popped element is the end index, then check if it was the maxHeight till now, if yes, then update the ans list with
 the current index and height from next tallest building from the heightCountQ. And decrease the count in heightCountQ,
 if the count is 1, then the node is removed from the tree.
Time Complexity (assuming that input arguments are already given and excluding time used in the declaration of output):

Sorting all the buildings as per the given constraints in the description would take O(2n*log(2n)), where n is the number
 of buildings in the given array and 2*n is the BuildingIndex. Also maintaining the count of heights take O(n*log(n)), since
 each insertion and deletion is O(log(n)) in a BST.
So, the total time complexity is O(n*log(n)).
Time Complexity:
Time to read the input is O(3*n) since for each line we have 3 integer values. For output, we can have 2*n skyline points
 in worst case scenario. Each output line will have 2 integer values, so the output time complexity is 2*O(2*n).
Overall time complexity is O(n*log(n)) + O(n) + O(n) ~= O(n*log(n))
Auxiliary Space Used:
The priorityQ and heightCount both require O(n) auxiliary space to store n buildings. So, total auxiliary space complexity
 is O(n).
Space Complexity:
Input and output arrays both require 3*n and 2*n amount of space respectively. Total space complexity including auxiliary
space comes out to be O(n).
'''
'''
import java.util.*;

public class optimal_solution {

    public static class BuildingIndex {
        int index;
        char startEnd;
        Integer height;

        public BuildingIndex(int index, char startEnd, int height) {
            this.index = index;
            this.startEnd = startEnd;
            this.height = height;
        }

        @Override
        public String toString() {
            return index + " " + startEnd + " ";
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numOfTestCases = in.nextInt();
        for (int n = 0; n < numOfTestCases; n++) {
            int numOfBuildings = in.nextInt();
            List<List<Integer>> buildings = new ArrayList<>();
            for (int i = 0; i < numOfBuildings; i++) {
                List<Integer> building = new ArrayList<>();
                building.add(in.nextInt());
                building.add(in.nextInt());
                building.add(in.nextInt());
                buildings.add(building);
            }
            List<List<Integer>> skyline = findSkyline(buildings);

            for(List<Integer> point : skyline){
                System.out.println(point.get(0) + " " + point.get(1));
            }
            System.out.println("");
        }
    }

    private static List<List<Integer>> findSkyline(List<List<Integer>> buildings) {

        List<List<Integer>> ans = new ArrayList<>();
        int numOfBuildings = buildings.size();
        TreeSet<BuildingIndex> priorityQ = new TreeSet<>(new Comparator<BuildingIndex>() {
            @Override
            public int compare(BuildingIndex o1, BuildingIndex o2) {
                if (o1.index != o2.index) {
                    return o1.index - o2.index;
                }
                if (o2.startEnd != o1.startEnd) {
                    // start index is higher priority than end index
                    if (o2.startEnd == 'e') {
                        return -1;
                    } else {
                        return 1;
                    }
                }
                // If two buildings start at the same point, then building with higher height should be higher priority.
                if (o1.startEnd == 's') {
                    return o2.height - o1.height;
                }
                // If two buildings end at the same point, then building with smaller height should be looked at first.
                else {
                    return o1.height - o2.height;
                }
            }
        });

        // Creating the priority queue of starting and end indices of all buildings
        for (List<Integer> building : buildings) {
            BuildingIndex buildingIndex1 = new BuildingIndex(building.get(0), 's', building.get(2));
            priorityQ.add(buildingIndex1);
            BuildingIndex buildingIndex2 = new BuildingIndex(building.get(1), 'e', building.get(2));
            priorityQ.add(buildingIndex2);
        }

        // A map (heightCountQ) which keeps track of all buildings so far in decreasing order of their heights.
        TreeMap<Integer, Integer> heightCountQ = new TreeMap<>();
        heightCountQ.put(0, 1);
        Integer maxHeight = 0;

        while (!priorityQ.isEmpty()) {
            BuildingIndex buildingIndex = priorityQ.pollFirst();
            // starting index signifies start of a buiding, so check if highest.
            if (buildingIndex.startEnd == 's') {
                heightCountQ.putIfAbsent(buildingIndex.height, 0);
                heightCountQ.put(buildingIndex.height, heightCountQ.get(buildingIndex.height) + 1);
                // if tallest buiding detected then update the skyline.
                if (buildingIndex.height > maxHeight) {
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(buildingIndex.index);
                    list.add(buildingIndex.height);
                    maxHeight = buildingIndex.height;
                    ans.add(list);
                }
            }
            // end index signifies end of a buiding, so remove it from the heightCountQ, and update skyline if highest.
            else {
                if (heightCountQ.get(buildingIndex.height) == 1) {
                    heightCountQ.remove(buildingIndex.height);
                } else {
                    heightCountQ.put(buildingIndex.height, heightCountQ.get(buildingIndex.height) - 1);
                }
                // update skyline, if tallest buiding ends.
                if (maxHeight.equals(buildingIndex.height)) {
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(buildingIndex.index);
                    Map.Entry<Integer, Integer> val = heightCountQ.pollLastEntry();
                    if (!maxHeight.equals(val.getKey())) {
                        list.add(val.getKey());
                        ans.add(list);
                    }

                    heightCountQ.put(val.getKey(), val.getValue());
                    maxHeight = val.getKey();
                }
            }
        }
        return ans;
    }
}
'''

