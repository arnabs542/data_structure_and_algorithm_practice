'''
 sorting and storing

 heap 1 < 6
 quicksort 1 < 6
 mergesort 1 < 6

 empty list
 [ 5, 4, 3, 4, 5, 6 ] N = 6

 [ 1, 2, 4, 6, 5, 5 ] N = 6
                  i

loop through arr asking if each element in current slot is in right spot (if
    while current slot not in correct slot
        see if slot already is taken (duplicate detected, so return it)
        swap it

return 0

 [ 2, 3, 4, 6, 5, 5 ] N = 6

see a val that we've seen before

return first duplicate detected
return 0 if there are no duplicates

[ 4, 2, 3, 4, 5, 6 ]

 slot_number = 0
 slot_it_should_be = 1

clarity of thought process
    tested based on
        competence and skills
        vague/open-ended problem
            detecting ambiguity should be scoped (2-5 min)
        problem solving aptitude
            given all details, you should be able to creatively apply a solution

clarity of expression
    verbal articulation
        !!important
        think outloud
        the perfect interview experience is when you don't know the solution and you can creatively come to it
        creating hypthesis --> failing and iterating is allowed --> repeat until success
    writen communication skills (through code)
        solving it perfectly in code without being able to articulate is not a good interview
        whiteboard, requirements, constraints, visualizations of the problem, pseudo-code --> translated into code
        if you checked in your code to github, it should be clear what you were trying to do

personal feedback
    good thought process, but too slow
    translation skills from pseudo-code to code was good (helped compensate for the long brainstorming session)


'''

def loose_perm(perm):
    for slot_number in range(len(perm)):
        if perm[slot_number] == slot_number+1:
            continue
        while perm[slot_number] != slot_number+1:
            slot_it_should_be = perm[slot_number]-1
            if perm[slot_it_should_be] == perm[slot_number]:      # if slot already has the number in it then it's a duplicate
                return perm[slot_number]
            perm[slot_it_should_be],perm[slot_number] = perm[slot_number],perm[slot_it_should_be]
    return 0

print(loose_perm([4, 2, 3, 4, 5, 6]))
