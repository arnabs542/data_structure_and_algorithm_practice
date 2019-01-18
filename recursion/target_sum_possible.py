#
# def check_if_sum_possible_rec(arr, current_target, index):
#     if index == len(arr):
#         return current_target == 0
#     if arr[index])<= current_target and check_if_sum_possible_rec(arr, current_target - arr[index], index+1):
#         return True
#     elif check_if_sum_possible_rec(arr, current_target, index+1):
#         return True
#     return False
#
# def check_if_sum_possible(arr, k):
#     if k == 0 and array_contains_a_zero(arr):
#         return True
#     return check_if_sum_possible_rec(arr, k, 0)
#
# def array_contains_a_zero(arr):
#     for num in arr:
#         if num == 0:
#             return True
#     return False
#
# print(check_if_sum_possible([-5, -10], -15))
