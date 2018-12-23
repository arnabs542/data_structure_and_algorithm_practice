from linked_lists.linked_list import Node, LinkedList

ll = LinkedList(Node(0))
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(8)
ll.append(10)

# creating a cycle
ll.root.next.next.next.next.next.next = ll.root.next.next.next

def hasCycle(ll):
    slow = ll.root
    fast = ll.root

    if fast.next != None and fast.next.next != None:
        fast = fast.next.next

    while fast and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False

print(hasCycle(ll))

ll = LinkedList(Node(0))
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(10)

print(hasCycle(ll))
