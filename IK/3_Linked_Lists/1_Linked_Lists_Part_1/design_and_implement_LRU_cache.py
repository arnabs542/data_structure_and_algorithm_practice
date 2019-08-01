'''
Design And Implement LRU Cache
Problem Statement:
The LRU caching scheme removes the least recently used frame, when the cache is full and a new page is referenced which
is not there in the cache.
You are given one integer named capacity, denoting the maximum size possible of the LRU cache. Also you are given three
integer arrays named query_type, key and value, each having size n.
query_type[i], key[i] and value[i] together denotes one query. So there are total n queries.
query_type contains 0 or 1. query_type[i] = 0 means ith query is GET query and query_type[i] = 1 means ith query is SET
query. key and value arrays contain only positive integers.

You have to return an array containing answers for GET queries.
GET query:
For GET query only key[i] matters, do not care what is stored in value[i].

For each GET query append one integer in the array to be returned. Append the value of the key[i], if the key[i] exists
in the cache, otherwise append -1.

SET query:
If key[i] is already present in the cache then update its value to value[i], else add key[i] with value value[i] in the cache.

Input/Output Format For The Function:
Input Format:
There are four arguments in the input. First is integer named capacity. Second is integer array named query_type. Third
is integer array named key. Fourth is integer array named value.

Output Format:
Return an array res containing answers for GET queries.

Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer capacity, denoting capacity of LRU cache.
The second line of input should contain an integer n, denoting the number of queries. In next n lines, ith line should contain
an integer query_type[i], denoting an entry at index i of query_type array. (i=0,1,...,n-1)
In next line, there should be an integer n. In next n lines, ith line should contain an integer key[i], denoting an entry
at index i of key array. (i=0,1,...,n-1)
In next line, there should be an integer n. In next n lines, ith line should contain an integer value[i], denoting an entry
at index i of value array. (i=0,1,...,n-1)

If n = 7,
capacity = 2,

index     query_type     key       value
0              1                    5             11
1              1                    10           22
2              0                    5               1
3              1                    15           33
4              0                    10             1
5              1                    5             55
6              0                    5               1

Then input should be:
2
7
1
1
0
1
0
1
0
7
5
10
5
15
10
5
5
7
11
22
1
33
1
55
1

Output Format:
Let’s denote the total no of read queries in input as nr. Then resultant array res returned by solution function will be
of size nr.
Hence, there will be nr lines, where ith line contains res[i], denoting entry at index i of res.

For input:
n = 7,
capacity = 2,

index     query_type     key       value
0              1                    5             11
1              1                    10           22
2              0                    5               1
3              1                    15           33
4              0                    10             1
5              1                    5             55
6              0                    5               1

Output will be:
11
-1
55

Constraints:
    * 1 <= n <= 10^5
    * 1 <= capacity <= 10^5
    * query_type[i] belongs to {0, 1}
    * 1 <= key[i] <= 10^5
    * 1 <= value[i] <= 10^5

Sample Test Case:
Sample Input:
capacity = 2
index     query_type     key       value
0              1                    5            11
1              1                    10          22
2              0                    5              1
3              1                    15          33
4              0                    10            1
5              1                    5            55
6              0                    5              1
(
this is same as:
query_type = [1 1 0 1 0 1 0]
key = [5 10 5 15 10 5 5]
value = [11 22 1 33 1 55 1]
)
Sample Output:
[11 -1 55]

Explanation:
Initially cache is empty.
Step 1:
    SET: 5 -> 11
    Noe cache contains (5 ->11).
Step 2:
    SET: 10 -> 22
    Now cache contains (5 -> 11) and (10 -> 22).
Step 3:
    GET: 5
    Cache contains (5 ->11), so append 11 to answer.
Step 4:
    SET: 15 -> 33
    Now cache contains (5 -> 11) and (15 -> 33).
    Note that here (10 -> 22) is removed because 10 is the least recently used. 5 was used in the previous query!
Step 5:
    GET: 10
    Cache does not contain key 10 (it was removed in previous step), so append -1 to answer.
Step 6:
    SET: 5 -> 55
    Now cache contains (5 -> 55) and (15 -> 33). Note that (5 -> 11) is updated to (5 -> 55).
Step 7:
    GET: 5
    Cache contains (5 -> 55), so append 55 to answer.

Notes:
Suggested time in interview: 20 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
you are using, coding it, as well as identifying any gaps that you can discuss during a TA session. Take your time, but
limit yourself to 2 one hour sessions for most problems.
'''
#!/bin/python3

import sys
import os

# Complete the function below.

def implement_LRU_cache(capacity, query_type, key, value):
    pass

if __name__ == "__main__":
    f = sys.stdout

    capacity = int(input())

    query_type_cnt = 0
    query_type_cnt = int(input())
    query_type_i = 0
    query_type = []
    while query_type_i < query_type_cnt:
        query_type_item = int(input())
        query_type.append(query_type_item)
        query_type_i += 1

    key_cnt = 0
    key_cnt = int(input())
    key_i = 0
    key = []
    while key_i < key_cnt:
        key_item = int(input())
        key.append(key_item)
        key_i += 1

    value_cnt = 0
    value_cnt = int(input())
    value_i = 0
    value = []
    while value_i < value_cnt:
        value_item = int(input())
        value.append(value_item)
        value_i += 1

    res = implement_LRU_cache(capacity, query_type, key, value);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()

'''
In actual world key = page number and value = actual page content.
First let's think how we can use single array (or linked list etc.), which will store {key, value} pairs to design LRU cache:

When cache is full we want to remove the least recently used {key, pair}. To keep track of new and old pairs, always we
will add new/recently used value at the beginning of the array. Hence {key, value} at the end of the array will be least
recently used.
When any set query comes:
Go through the array and search for the key.
1) If key is already present with some value: Remove already present {key, value} from the array. Add {key, new value} at
 the front of the array.
2) If key is not present: If cache is full then remove one least recently used {key, value} i.e. remove last {key, value}
 pair. Now add {key, value} at the front of the array.  
When any get query comes:
Go through the array and search for the key.
1) If key is already present with some value: Move {key, value} pair to the front of the array (don't forget this!), then
 return its value.
2) If key is not present: return -1. 
This will give correct answer, but time complexity of the set and get will be O(capacity). So time complexity of the code
 will be O(n * capacity). 
Problem with this approach is, in each query we have to traverse the array to find the key. Search can be reduced from O(capacity)
 to O(1) if we use hash map to store the position of the key in array!
Now we can use linked list with hash map to speed up the process. Linked list to maintain the order of least recently used
 {key, value} pairs, and hash map for quick search!
Have a look at the optimal_solution1.cpp (solution using built in list) and optimal_solution2.cpp (solution using custom
 linked list).
Time Complexity:
O(n).
As each get and set query is O(1), and we have total n queries.
Auxiliary Space Used:
O(min(capacity, number of set queries)).
As each set query will increase the size of hash map and list, till we have reached the capacity of the cache. 
Space Complexity: 
O(n).
Input is O(n) and auxiliary space used is O(min(capacity, number of set queries)).
Now number of set queries <= number of total queries. So number of set queries <= n.
So O(n) + O(min(capacity, number of set queries)) -> O(n) + O(min(capacity, n)) -> O(n). 
Slightly slower solution using hash map + max heap is also possible.
In hash map we can store {key, {time stamp, value}} pairs. And in max heap we can store {time stamp, key} pair. {time stamp,
 key} having largest time stamp will be at the root of the max heap.
We will start with time stamp = 0 and in each query it will be decremented it by 1. (Generally we should increment it, but
 in C++ built in heap is max heap so we are decrementing time stamp. Suppose one key has time stamp = -5 and other has time
 stamp = -10, then least recently used key will be the key having larger value (-5) and it should be removed.)
When get query comes:
Check if key is present in hash map or not.
1) If key is not present: return -1.
2) If key is present: Update the time stamp in hash map. Return the value of the key present in hash map. (We are not making
 any changes in max heap, not even time stamp! Time stamp in hash map will be updated but in max heap it will be the older
 one. We will do lazy updates when cache is full!)
When set query comes:
Check if key is present in hash map or not.
1) If key is not present: If cache is full then remove least recently used element from hash map and max heap. To find which
 element to be removed we will use the max heap. We will start looking at the root of the max heap i.e. elements having
 largest time stamp. We will check if time stamp in max heap and in hash map are same or not. If they are not same then
 it means the element was accessed, so remove it from top of max heap and insert again with new time stamp that is in hash
 map. If time stamps are same then that element is least recently used and it should be removed. (Try some examples to understand
 it more clearly.)  
Now add {key, {time stamp, value} in hash map. Also add {time stamp, key} in max heap.
2) If key is present: Update the new value in hash map. Update the time stamp in hash map. (We are not making any changes
 in max heap, not even time stamp! Time stamp in hash map will be updated but in max heap it will be the older one. We will
 do lazy updates when cache is full!)
Have a look at other_solution.cpp for solution using hash map + max heap.
Time Complexity:
O(n * log(capacity)).
This solution uses max heap's insert and delete operations, both having time complexity O(log(size of the max heap)), hence
 time complexity of the solution will become O(n * log(capacity)).
Auxiliary Space Used:
O(min(capacity, number of set queries)).
As each set query will increase the size of hash map and list, till we have reached the capacity of the cache. 
Space Complexity: 
O(n).
Input is O(n) and auxiliary space used is O(min(capacity, number of set queries)).
Now number of set queries <= number of total queries. So number of set queries <= n.
So O(n) + O(min(capacity, number of set queries)) -> O(n) + O(min(capacity, n)) -> O(n). 
Time complexity of solution using (linked list + hash map) is O(n) and time complexity of solution using (max heap + hash
 map) is O(n * log(capacity)), but when you will run the code, you will not observe the running time difference! 
When we ran solutions on some test cases, optimal_solution1.cpp was taking 1.81 seconds, optimal_solution2.cpp was taking
 1.80 second and other_solution.cpp was taking 1.81 seconds.
We can see that there is not much difference in optimal_solution1.cpp (built-in linked list) and optimal_solution2.cpp (custom
 implementation of linked list), but code for optimal_solution2.cpp is complex, so better to use built-in list than implementing
 own linked list to reduce unnecessary errors. 
Some of the reasons together, why other_solution.cpp was not slower are:
1) Caching. This is the most imp thing, affecting the run time. In heap we are using array and hence elements will be stored
 in continuous memory, but in linked list it will not be the case. Hence other_solution.cpp will better use the caching.
 
2) Limitations of input size. If we can run code on too many queries (much more than 10^5) with appropriate cache capacity
 in input, then in worst case optimal_solution1.cpp and optimal_solution2.cpp will be faster (as expected)! (If we can provide
 too many queries with appropriate cache capacity in input, then we can design input such that other_solution.cpp can not
 use the caching well, leading optimal_solution1.cpp and optimal_solution2.cpp to be faster.)
There are some limitations ( https://docs.google.com/document/d/1LY31OCgeVpez2k7EcvGO1SyTqcpTljyRoN19n8QK38A/edit?ts=5a4f2404#heading=h.g3c5yh5a2aoo
 ) of online judges, hence we can given ~ 10^5 queries in one test case. (You will see many times that constraints has something
 like 1 <= n <= 10^5.) There are some reasons for that 1) Time: Online judges also have limitied resources and hence allow
 only few seconds for one submission, hence we can not give input that takes minutes to run. 2) Memory: Input having array
 of size 10^5 will be ~1 MB, now if we give 10^8 in one test case then input file will be ~ 1 GB for one test case! And
 for one problem we want to test your solution over multiple test cases (to take care of all corner cases and worst cases).
 Hence generating input files in GBs and uploading it on online judge is not feasible. Also many languages like python are
 slow to read files, hence it will take more time to read input!
We suggest you to implement both type of solutions and experiment with different inputs.
For other_solution.cpp worst case example with n = 15: 
capacity: 7 
n = 15
query_type = [1 1 1 1 1 1 1 0 0 0 0 0 0 0 1]
key = [1 2 3 4 5 6 7 1 2 3 4 5 6 7 8]
val = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
First we will add 7 key with values. After this cache will be full. 
Then we will access all of them hence time stamp will be updated for all keys. 
Now we will add one new key. We have accessed all 7 keys, hence in set function call for {8 -> 15}, while lopp will run
 7 times (all previous keys), with each taking log(capacity) = log(7) time to run. Hence we will get overall O(n * log(k))
 time complexity. 
In optimal_solution1.cpp and optimal_solution2.cpp each query will be O(1), but constant hidden is large due to linked list,
 but with variable change it will not change more, but here with variable change log(k) can change, hence with large number
 of queries and appropriate cache capacity in input, other_solution.cpp can be made slower than optimal_solution1.cpp and
 optimal_solution2.cpp. (But it is not possible to provide such large input on online judges, so you will never encounter
 that other_solution.cpp is much slower!) 
'''
'''
OTHER SOLUTION
#include<bits/stdc++.h>

using namespace std;

const int MAX_CAPACITY = 100000, MAX_N = 100000, MAX_KEY = 100000, MAX_VAL = 100000;

// -------------------------- START --------------------------

class LRU_cache
{
	// Maximum size of the cache.
	int capacity = 0;
	int time_stamp = 0;
	// Heap storing {time_stamp, key} pairs.
	vector<pair<int, int>> lru_heap;
	// Hash map storing {key, {time_stamp, value}} pairs.
	unordered_map<int, pair<int, int>> cache;

public:
	
	// Constructor.
	LRU_cache(int _capacity) 
	{
		capacity = _capacity;
	}

	// Return value of the key, if key is present, else return -1.
	int get(int key) 
	{
		// If the key is already present.
		if(cache.find(key) != cache.end()) 
		{
			// Update the timestamp in the hash map to current timestamp.
			cache[key].first = time_stamp--;
			return cache[key].second;
		} 
		else 
		{
			return -1;
		}
	}

	// If key is present in cache then updates its values, else add {key, value} pair in cache.
	void set(int key, int value) 
	{
		// Take care of the case where key is already in the cache.
		if(cache.find(key)!=cache.end()) 
		{
	  		cache[key]={time_stamp--, value};
	  		return;
		}
		// Remove least recently used element if cache is full.
		if(lru_heap.size() == capacity)
		{
			// Loop till we have removed one element from cache.
		  	while(true) 
		  	{
			    // Remove from heap. Removed element will be at the back of vector.
			    pop_heap(lru_heap.begin(), lru_heap.end());
			    // Get the removed element from back.
			    auto& top = lru_heap.back();
			    // Check timestamp in hash map.
			    if(cache[top.second].first == top.first) 
			    {
			    	/*
				    Element has same time stamp in heap and hash map hence we have found the 
				    element to be removed.
				    */
				    // Remove it from hash map.
				    cache.erase(top.second);
				    // Remove from heap.
				    lru_heap.pop_back();
				    break;
			    }
			    else 
			    {
			    	// This key was updated, hence push it back in heap with updated time stamp.
			    	top.first = cache[top.second].first;
			    	push_heap(lru_heap.begin(), lru_heap.end());
			    }
		  	}
		}
		// Add the new key into hash map and heap with the appropriate timestamp.
		cache[key] = {time_stamp, value};
		lru_heap.push_back({time_stamp, key});
		push_heap(lru_heap.begin(), lru_heap.end());
		time_stamp--;
	}
};

vector<int> implement_LRU_cache(int capacity, vector<int> query_type, vector<int> key, 
	vector<int> value)
{
	int n = query_type.size();
	// Setup cache. 
	LRU_cache* cache = new LRU_cache(capacity);
	vector<int> ans;
	for (int i = 0; i < n; i++)
	{
		if (query_type[i] == 0)
		{
			ans.push_back(cache->get(key[i]));
		}
		else
		{
			cache->set(key[i], value[i]);
		}
	}
	return ans;
}

// -------------------------- STOP ---------------------------

int main()
{
	clock_t start, end;
	start = clock();

	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int capacity;
		cin >> capacity;
		assert(1 <= capacity);
		assert(capacity <= MAX_CAPACITY);

		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> query_type(n);
		int no_of_get_queries = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> query_type[i];
			no_of_get_queries += (query_type[i] == 0);
			assert(query_type[i] == 0 || query_type[i] == 1);
		}

		int temp_n;
		cin >> temp_n;
		assert(n == temp_n);
		vector<int> key(n);
		for (int i = 0; i < n; i++)
		{
			cin >> key[i];
			assert(1 <= key[i]);
			assert(key[i] <= MAX_KEY);
		}

		cin >> temp_n;
		assert(n == temp_n);
		vector<int> value(n);
		for (int i = 0; i < n; i++)
		{
			cin >> value[i];
			assert(1 <= value[i]);
			assert(value[i] <= MAX_VAL);
		}

		vector<int> ans = implement_LRU_cache(capacity, query_type, key, value);
		int len = ans.size();
		assert(len == no_of_get_queries);
		for (int i = 0; i < len; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	end = clock();
    cout << ((double) (end - start)) / CLOCKS_PER_SEC << endl;

	return 0;
}
'''
'''
OPTIMIAL SOLUTION 1
#include<bits/stdc++.h>

using namespace std;

const int MAX_CAPACITY = 100000, MAX_N = 100000, MAX_KEY = 100000, MAX_VAL = 100000;

// -------------------------- START --------------------------

class LRU_cache
{
	// Maximum size of the cache.
	int capacity;
	/*
	Stores the {key, value} pair.
	Implementing own linked list will give some speedup than using built-in list, but it will 
	affect the readibility of the code, hence we have used built in list.
	If you are getting time limit exceeded, than try to use linked list instead of built in list.
	*/
	list<pair<int, int>> actual_storage;
	// key -> pointer to where it is stored in actual storage.
	unordered_map<int, list<pair<int, int>>::iterator> key_to_actual_storage_mapping;

public:

	// Constructor.
	LRU_cache(int _capacity)
	{
		capacity = _capacity;
	}

	/*
	Add {key, value} pair at the front of actual_storage. 
	Also add the mapping (key -> pointer to where it is stored in actual storage).
	That is (key -> beginning of the actual_storage).
	*/
	void add_to_front(int key, int value)
	{
		actual_storage.push_front({key, value});
		key_to_actual_storage_mapping[key] = actual_storage.begin();
	}

	/*
	Remove one {key, value} pair from the end of actual_storage.
	Also remove the mapping (key -> pointer to where it is stored in actual storage).
	*/
	void remove_least_recently_used()
	{
		int key = actual_storage.back().first;
		key_to_actual_storage_mapping.erase(key);
		actual_storage.pop_back();
	}

	// Return value of the key, if key is present, else return -1.
	int get(int key)
	{
		unordered_map<int, list<pair<int, int>>::iterator>::iterator it = 
			key_to_actual_storage_mapping.find(key);

		// If key is not present in mapping then return -1.
		if (it == key_to_actual_storage_mapping.end())
		{
			return -1;
		}
		/*
		it->second points to {key, value} in the actual_storage.
		So it->second->second will give value.
		*/
		int value = it->second->second;
		// Remove from the original position.
		actual_storage.erase(it->second);
		// Add to the front.
		add_to_front(key, value);
		return value;
	}

	// If key is present in cache then updates its values, else add {key, value} pair in cache.
	void set(int key, int value)
	{
		unordered_map<int, list<pair<int, int>>::iterator>::iterator it = 
			key_to_actual_storage_mapping.find(key);

		// If key is not present in mapping then add {key, value} and setup the mapping.
		if (it == key_to_actual_storage_mapping.end())
		{
			// If cache is full then remove the least recently used {key, value}.
			if (key_to_actual_storage_mapping.size() == capacity)
			{
				remove_least_recently_used();
			}
			// Add to the front.
			add_to_front(key, value);
			return;
		}
		// Remove from the original position.
		actual_storage.erase(it->second);
		// Add to the front.
		add_to_front(key, value);
	}
};

vector<int> implement_LRU_cache(int capacity, vector<int> query_type, vector<int> key, 
	vector<int> value)
{
	int n = query_type.size();
	// Setup cache. 
	LRU_cache* cache = new LRU_cache(capacity);
	vector<int> ans;
	for (int i = 0; i < n; i++)
	{
		if (query_type[i] == 0)
		{
			ans.push_back(cache->get(key[i]));
		}
		else
		{
			cache->set(key[i], value[i]);
		}
	}
	return ans;
}

// -------------------------- STOP ---------------------------

int main()
{
	clock_t start, end;
	start = clock();

	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int capacity;
		cin >> capacity;
		assert(1 <= capacity);
		assert(capacity <= MAX_CAPACITY);

		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> query_type(n);
		int no_of_get_queries = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> query_type[i];
			no_of_get_queries += (query_type[i] == 0);
			assert(query_type[i] == 0 || query_type[i] == 1);
		}

		int temp_n;
		cin >> temp_n;
		assert(n == temp_n);
		vector<int> key(n);
		for (int i = 0; i < n; i++)
		{
			cin >> key[i];
			assert(1 <= key[i]);
			assert(key[i] <= MAX_KEY);
		}

		cin >> temp_n;
		assert(n == temp_n);
		vector<int> value(n);
		for (int i = 0; i < n; i++)
		{
			cin >> value[i];
			assert(1 <= value[i]);
			assert(value[i] <= MAX_VAL);
		}

		vector<int> ans = implement_LRU_cache(capacity, query_type, key, value);
		int len = ans.size();
		assert(len == no_of_get_queries);
		for (int i = 0; i < len; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	end = clock();
    cout << ((double) (end - start)) / CLOCKS_PER_SEC << endl;

	return 0;
}
'''
'''
OPTIMAL SOLUTION 2
#include<bits/stdc++.h>

using namespace std;

const int MAX_CAPACITY = 100000, MAX_N = 100000, MAX_KEY = 100000, MAX_VAL = 100000;

// -------------------------- START --------------------------

class LRU_cache
{
	// Maximum size of the cache.
	int capacity;
	class ListNode
	{
	public:
		int key;
		int value;
		ListNode *prev;
		ListNode *next;

		ListNode(int _key = 0, int _value = 0)
		{
			key = _key;
			value = _value;
			prev = NULL;
			next = NULL;
		}
	};
	// Linked list whose nodes store {key, value}.
	ListNode *head = NULL, *tail = NULL;
	// key -> pointer to where it is stored in linked list.
	unordered_map<int, ListNode *> key_to_actual_storage_mapping;

public:

	// Constructor.
	LRU_cache(int _capacity)
	{
		capacity = _capacity;
	}

	/*
	Add {key, value} at the front of linked list. 
	Also add the mapping (key -> pointer to where it is stored in linked list).
	That is (key -> head of the linked list).
	*/
	void add_to_front(int key, int value)
	{
		ListNode *temp = new ListNode(key, value);
		// If linked list is empty, set head and tail.
		if (head == NULL)
		{
			head = temp;
			tail = temp;
		}
		else
		{
			temp->next = head;
			head->prev = temp;
			head = temp;
		}
		key_to_actual_storage_mapping[key] = head;
	}

	/*
	Remove one {key, value} from the end of linked list.
	Also remove the mapping (key -> pointer to where it is stored in linked list).
	*/
	void remove_least_recently_used()
	{
		int key = tail->key;
		key_to_actual_storage_mapping.erase(key);
		// If only one node, set head and tail. 
		if (head == tail)
		{
			delete tail;
			head = tail = NULL;
			return;
		}
		// Set tail.
		tail = tail->prev;
		delete tail->next;
		tail->next = NULL;
	}

	// Remove node from linked list.
	void erase_node(ListNode *cur_node)
	{
		ListNode *prev_node = cur_node->prev;
		ListNode *next_node = cur_node->next;
		// Connect previous node with next node.
		if (prev_node != NULL)
		{
			prev_node->next = next_node;
		}
		if (next_node != NULL)
		{
			next_node->prev = prev_node;
		}
		// If node to be removed is the only node in linked list, set head and tail.
		if (head == tail)
		{
			head = tail = NULL;
		}
		// If node to be removed is head, set head.
		else if (head == cur_node)
		{
			head = next_node;
		}
		// If node to be removed is tail, set tail.
		else if (tail == cur_node)
		{
			tail = prev_node;
		}
		delete cur_node;
	}

	// Return value of the key, if key is present, else return -1.
	int get(int key)
	{
		unordered_map<int, ListNode *>::iterator it = key_to_actual_storage_mapping.find(key);
		// If key is not present in mapping then return -1.
		if (it == key_to_actual_storage_mapping.end())
		{
			return -1;
		}
		// it->second points to node in the linked list.
		int value = it->second->value;
		// Remove from the original position.
		erase_node(it->second);
		// Add to the front.
		add_to_front(key, value);
		return value;
	}

	// If key is present in cache then updates its values, else add {key, value} pair in cache.
	void set(int key, int value)
	{
		unordered_map<int, ListNode*>::iterator it = key_to_actual_storage_mapping.find(key);
		// If key is not present in mapping then add {key, value} and setup the mapping.
		if (it == key_to_actual_storage_mapping.end())
		{
			// If cache is full then remove the least recently used {key, value}.
			if (key_to_actual_storage_mapping.size() == capacity)
			{
				remove_least_recently_used();
			}
			// Add to the front.
			add_to_front(key, value);
			return;
		}
		// Remove from the original position.
		erase_node(it->second);
		// Add to the front.
		add_to_front(key, value);
	}
};

vector<int> implement_LRU_cache(int capacity, vector<int> query_type, vector<int> key, 
	vector<int> value)
{
	int n = query_type.size();
	// Setup cache. 
	LRU_cache* cache = new LRU_cache(capacity);
	vector<int> ans;
	for (int i = 0; i < n; i++)
	{
		if (query_type[i] == 0)
		{
			ans.push_back(cache->get(key[i]));
		}
		else
		{
			cache->set(key[i], value[i]);
		}
	}
	return ans;
}

// -------------------------- STOP ---------------------------

int main()
{
	clock_t start, end;
	start = clock();

	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int capacity;
		cin >> capacity;
		assert(1 <= capacity);
		assert(capacity <= MAX_CAPACITY);

		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> query_type(n);
		int no_of_get_queries = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> query_type[i];
			no_of_get_queries += (query_type[i] == 0);
			assert(query_type[i] == 0 || query_type[i] == 1);
		}

		int temp_n;
		cin >> temp_n;
		assert(n == temp_n);
		vector<int> key(n);
		for (int i = 0; i < n; i++)
		{
			cin >> key[i];
			assert(1 <= key[i]);
			assert(key[i] <= MAX_KEY);
		}

		cin >> temp_n;
		assert(n == temp_n);
		vector<int> value(n);
		for (int i = 0; i < n; i++)
		{
			cin >> value[i];
			assert(1 <= value[i]);
			assert(value[i] <= MAX_VAL);
		}

		vector<int> ans = implement_LRU_cache(capacity, query_type, key, value);
		int len = ans.size();
		assert(len == no_of_get_queries);
		for (int i = 0; i < len; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	end = clock();
    cout << ((double) (end - start)) / CLOCKS_PER_SEC << endl;

	return 0;
}
'''
