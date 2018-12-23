class Node():
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList():
    def __init__(self, Node):
        self.root =  Node

    def append(self, v):
        new_node = Node(v)
        self.add_to_end(self.root, new_node)

    def add_to_end(self, current, node_to_add):
        if current != None:
            if current.next == None:
                current.next = node_to_add
            else:
                current = current.next
                self.add_to_end(current, node_to_add)

    def print_linked_list(self):
        current = self.root
        while current != None:
            print(current.value, end=" -> ")
            current = current.next
        print('NULL')

    def add_to_beginning(self, v):
        new_node = Node(v)
        new_node.next = self.root
        self.root = new_node

    def insert_in_order(self, v):
        if self.root.value > v:
            self.add_to_beginning(v)
            return

        new_node = Node(v)
        current = self.root

        while current.next != None and current.next.value <= new_node.value:
            current = current.next

        # 1 -> 3 -> 5 -> NULL
        # 2
        new_node.next = current.next
        current.next = new_node

# ll = LinkedList(Node(1))
# ll.insert_in_order(3)
# ll.insert_in_order(2)
# ll.insert_in_order(2)
# ll.insert_in_order(0)
# ll.insert_in_order(4)
# ll.insert_in_order(4)
# ll.insert_in_order(5)
# ll.print_linked_list()
