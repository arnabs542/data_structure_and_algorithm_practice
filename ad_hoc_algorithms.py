# given a range (start, end) and a sorted list of integer values, display the missing items from the list for the given
# range. when displayed use shorthand notation when possible (e.g. 4-5, 4-10, but only 4 if no consecutive number is
# missing).
#
# [1,3,5,7,8,9,13]   start = 5   end = 12

def print_missing_nums(list, start, end):
    if start < list[0]:
        print_numbers(start, list[0])

    for i in range(len(list)-1):
        print_numbers(list[i], list[i+1])

    if list[-1] < end:
        print_numbers(list[-1], end)

def print_numbers(start, end):
    if start >= end:
        print(start)
    elif end - start > 3:
        print(str(start+1) + "-" + str(end-1))
    elif end - start == 3:
        print(str(start+1) + ", " + str(start+2))
    elif end - start == 2:
        print(start+1)

list = [-10, 3]
start = -4
end = 12000
print_missing_nums(list, start, end)





'''
SECOND SOLUTION

/*
c++ solution
void printNumber(int start, int end) {
    if (start == end) {
        cout << start << endl;
    } else {
        if (start < 0) {
            cout << "(" << start << ")-";
        } else {
            cout << start << "-";
        }
        if (end < 0) {
            cout << "(" << end << ")" << endl;
        } else {
            cout << end << endl;
        }
    }
}

void printTheRangeWithHyphens(vector<int> &nums, int start, int end) {
    if (start > end) return;
    if (nums.size() == 0) {
        printNumber(start, end);
    }

    int next = start;

    for (int n : nums) {
        if (n < start) {
            continue;
        }
        if (n > end) {
            printNumber(next, end);
            return;
        }
        if (n > next) {
            printNumber(next, n - 1);
        }
        next = n + 1;
    }
    if (next <= end) {
        printNumber(next, end);
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> nums = {0,1,3,5,7,8,9,13};
    int start = -5;
    int end = 90;
    printTheRangeWithHyphens(nums, start, end);
    return 0;
}

*/
'''

def printNumbers(start, end):
    if start==end:
        print(start)
    else:
        if start < 0:
            print('(' + str(start) + ')-')
        else:
            print(start + '-')
        if end < 0:
            print('(' + str(end) + ')-')
        else:
            print(end)

def printRangeWithHyphens(nums, start, end):
    if start > end:
        return

    if len(nums) == 0:
        printNumbers(start, end)

    next = start
    for num in nums:
        if num < start:
            continue
        if num > end:
            printNumbers(next, end)
            return
        if num > next:
            printNumbers(next, num-1)
        next = num+1

    if next <= end:
        printNumbers(next, end)


