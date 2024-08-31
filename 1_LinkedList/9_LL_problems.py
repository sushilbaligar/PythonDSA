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
        print()

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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = prev

# 1. Implement the find_middle_node method for the LinkedList class.
    def find_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

# Write a method called has_loop that is part of the linked list class.
# The method should be able to detect if there is a cycle or loop present in the linked list.
# You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
# Given this LinkedList:
# 1 -> 2 -> 3 -> 4
# If k=1 then return the first node from the end (the last node) which contains the value of 4.
# If k=2 then return the second node from the end which contains the value of 3, etc.
# If the index is out of bounds, the program should return None.
    def find_kth_from_end(self, ll, k):
        if k <= 0:
            return None
        slow = fast = ll.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.value

# Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.
    def partition_list(self, x):
        lstart = less = Node(0)
        gstart = great = Node(0)
        temp = self.head
        while temp is not None:
            if temp.value < x:
                less.next = temp
                less = less.next
            else:
                great.next = temp
                great = great.next
            temp = temp.next
        less.next = gstart.next
        self.head = lstart.next
        return self.head

# Implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
    def remove_duplicates(self):
        values = set()
        prev = None
        temp = self.head
        while temp is not None:
            if temp.value in values:
                prev.next = temp.next
                self.length -= 1
            else:
                values.add(temp.value)
                prev = temp
            temp = temp.next

# Implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.
    def binary_to_decimal(self):
        num = 0
        temp = self.head
        while temp is not None:
            num = num * 2 + temp.value
            temp = temp.next
        return num

# Write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.
    def reverse_between(self, start_index, end_index):
        dummy = Node(0)
        dummy.next = self.head
        pre = dummy
        temp = self.head
        for _ in range(start_index):
            pre = pre.next
        temp = pre.next
        for _ in range(end_index - start_index):
            after = temp.next
            temp.next = after.next
            after.next = pre.next
            pre.next = after
        self.head = dummy.next

my_linked_list = LinkedList(1)
my_linked_list.insert(0, 2)
my_linked_list.insert(1, 3)
my_linked_list.insert(2, 4)
my_linked_list.insert(2, 5)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
print("Middle Node is:",my_linked_list.find_middle_node())
print("Has Loop:", my_linked_list.has_loop())
print("Kth Node from End 1:", my_linked_list.find_kth_from_end(my_linked_list, 1))
print("Kth Node from End 4:", my_linked_list.find_kth_from_end(my_linked_list, 4))
my_linked_list.partition_list(5)
my_linked_list.append(5)
my_linked_list.print_list()
my_linked_list.remove_duplicates()
my_linked_list.print_list()

rbll = LinkedList(1)
rbll.append(2)
rbll.append(3)
rbll.append(4)
rbll.append(5)
rbll.reverse_between(1, 4)
rbll.print_list()


binaryll = LinkedList(1)
binaryll.append(0)
binaryll.append(1)
print(binaryll.binary_to_decimal())