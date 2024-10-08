class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        if temp is None:
            print("Linked List is empty")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        if self.length == 0:
            return self.append(value)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

my_linked_list = LinkedList(4)
my_linked_list.print_list()
print("Pop:",my_linked_list.pop())
my_linked_list.print_list()
my_linked_list.prepend(5)
my_linked_list.append(3)
my_linked_list.print_list()