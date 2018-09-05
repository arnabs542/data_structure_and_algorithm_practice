

def num_ways_to_sum(n, numbers):
    ways = 0
    ways += num_ways_to_sum_rec(n, numbers)
    print(ways)

def num_ways_to_sum_rec(n, numbers):
    for num in numbers:
        if n - num == 0:
            return 1
        elif n - num > 0:
            return num_ways_to_sum_rec(n-num, numbers) + num_ways_to_sum_rec(n-num, numbers)

num_ways_to_sum(5, [1,3,4])
