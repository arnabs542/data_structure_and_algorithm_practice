# Given an array of integers, find the max product you can get by multiplying three of the integers

def get_multiple(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0]*arr[1]
    return 1

def highest_product_of_three(numbers):
    highest = float('-inf')
    pos = []
    neg = []

    for num in numbers:
        temp = num
        if num > 0:
            if len(pos) < 2:
                if len(pos) == 0:
                    pos.append(num)
                else:
                    if pos[0] < temp:
                        pos[0], temp = temp, pos[0]
                    pos.append(temp)
            else:
                if temp > pos[0]:
                    temp, pos[0] = pos[0],temp
                if temp > pos[1]:
                    temp, pos[1] = pos[1],temp
        else:
            if len(neg) < 2:
                if len(neg) == 0:
                    neg.append(num)
                else:
                    if neg[0] < temp:
                        neg[0], temp = temp, neg[0]
                    neg.append(temp)
            else:
                if temp > neg[0]:
                    temp, neg[0] = neg[0],temp
                if temp > neg[1]:
                    temp, neg[1] = neg[1],temp

        if len(pos) > 1:
            positive = get_multiple(pos)
            highest = max(highest, positive*num)
        if len(neg) > 1:
            negative = get_multiple(neg)
            highest = max(highest, negative*num)
        if len(pos) > 1 and len(neg) > 1:
            highest = max(highest, pos[0]*neg[0]*num)
    return highest

print("1200 -->" + str(highest_product_of_three([10, 3, 5, 6, 20])))
print("300 -->" + str(highest_product_of_three([-10, -10, 1, 3, 2])))
print("-90 -->" + str(highest_product_of_three([-10, -3, -5, -6, -20])))
print("168 -->" + str(highest_product_of_three([1, -4, 3, -6, 7, 0])))
