from linked_lists.linked_list import Node, LinkedList
'''
Given a Linked List and a value X, sort the linked list so that all values less than X appear first, all values equal
to X (including X) appears next, and all values greater than X appear last.
'''

def dutch_flag(linked_list, x):
    less_than = None
    equal = None
    greater = None

    lt = None
    eq = None
    gt = None
    current = linked_list.root
    while current:
        if current.value < x:
            if less_than == None:
                less_than = LinkedList(Node(current.value))
                lt = less_than.root
            else:
                lt.next = Node(current.value)
                lt = lt.next
        elif current.value == x:
            if equal == None:
                equal = LinkedList(Node(current.value))
                eq = equal.root
            else:
                eq.next = Node(current.value)
                eq = eq.next
        else:
            if greater == None:
                greater = LinkedList(Node(current.value))
                gt = greater.root
            else:
                gt.next = Node(current.value)
                gt = gt.next
        current = current.next

    if equal == None:
        equal = LinkedList(x)
    else:
        equal.append(x)

    current = less_than
    while current:
        current

    lt.next = equal.root
    eq.next = greater.root
    return less_than

ll = LinkedList(Node(0))
ll.append(2)
ll.append(8)
ll.append(6)
ll.append(4)
ll.append(4)
ll = dutch_flag(ll, 5)
ll.print_linked_list()

