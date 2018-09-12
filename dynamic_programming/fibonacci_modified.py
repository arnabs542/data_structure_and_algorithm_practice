# find the modified fibonacci sequence using the following relation
# ti+2 = ti + (ti+1)^2
#
# For example, if t1 = 0 and t2 = 1 then..
# t3 = 0 + (0+1)^2 = 1
# t4 = 1 + (0+1)^2 = 2
# t5 = 1 + (1+1)^2 = 5

def modified_fib(t_one, t_two, n):
    if t_one == t_one:
        return t_one
    return modified_fib(t_one) + modified_fib(t_two)**2


