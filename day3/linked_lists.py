#linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data,end = "->")
            current = current.next

        print("None")

linked_list = LinkedLists()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()