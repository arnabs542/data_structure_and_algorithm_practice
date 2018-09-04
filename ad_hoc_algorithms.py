# given a range (start, end) and a sorted list of integer values, display the missing items from the list for the given
# range. when displayed use shorthand notation when possible (e.g. 4-5, 4-10, but only 4 if no consecutive number is
# missing).
#
# [3,7,8,9,10]
# [1,3,5,7,8,9,13]   start = 5   end = 12

def print_missing_nums(list, start, end):
    if start < list[0]:
        print_numbers(start, list[0])

    i = 0
    while i < len(list)-1:
        print_numbers(list[i], list[i+1])
        i+=1

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
        print(str(start+1))

list = [1,3,5,7,8,9,13,1000]
start = -4
end = 12000
print_missing_nums(list, start, end)
