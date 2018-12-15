
def dutch_flag_sort(arr):
    r = 0
    g = 0
    b = len(arr) - 1
    i = 0
    while i <=  b:
        if arr[i] == 'R':
            arr[i],arr[r] = arr[r],arr[i]
            r += 1
            i += 1
        elif arr[i] == 'G':
            i += 1
        else:
            arr[i],arr[b] = arr[b],arr[i]
            b -= 1
    return arr

print(dutch_flag_sort(['G','B','G','G','R','B','R','G']))
