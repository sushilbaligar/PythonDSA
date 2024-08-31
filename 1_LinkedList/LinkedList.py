class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print("\n")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

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
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
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
        return True
    
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
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # finding middle node of linked list - use fast n slow pointers
    def find_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # find if ll has loop. use fast n slow pointers
    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    # find kth node from end of ll. use fast n slow pointers. 
    # Move fast by K nodes first.Then keep both at same pace till fast reaches end. 
    # Slow will k nodes behind giving us the answer
    def find_kth_from_end(self, k):
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    # partition ll around value x. All values <x will be at start and >=x at end and in place
    # Use 2 dummy and 2 prev nodes to achieve this
    def partition_list(self,x):
        if self.head == None:
            return None
        p1 = d1 = Node(0)
        p2 = d2 = Node(0)
        curr = self.head
        while curr:
            if curr.value < x:
                p1.next = curr
                p1 = curr
            else:
                p2.next = curr
                p2 = curr                
            curr = curr.next
        p1.next = p2.next = None
        p1.next = d2.next
        self.head = d1.next
        return self.head

    # remove duplicates from ll using set
    def remove_duplicates_set(self):
        s = set()
        prev = None
        curr = self.head
        while curr:
            if curr.value in s:
                prev.next = curr.next
                self.length -= 1
            else:
                s.add(curr.value)
                prev = curr
            curr = curr.next
    
    #remove duplicates from ll without using set
    def remove_duplicates_without_set(self):
        if self.head == None:
            return None
        curr = self.head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.value == curr.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            curr = curr.next

    def binary_to_decimal(self):
        num = 0
        curr = self.head
        while curr:
            num = num * 2 + curr.value
            curr = curr.next
        print(num)

    def reverse_between(self,m,n):
        if self.length <= 1:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next
        curr = prev.next
        for _ in range(n - m):
            after = curr.next
            curr.next = after.next
            after.next = prev.next
            prev.next = after
        dummy.next = self.head



linked_list = LinkedList(11)
linked_list.append(3)
linked_list.append(23)
linked_list.prepend(1)
linked_list.insert(2, 44)

linked_list.print_list()
print("Middle node:", linked_list.find_middle_node().value)
print("Reversing linked list",linked_list.reverse())
linked_list.print_list()
print("Remove at index 2:",linked_list.remove(2).value)
linked_list.print_list()
print("Set value at index 2 as 50")
linked_list.set_value(2,50)
linked_list.print_list()
print("Get value at index 2:",linked_list.get(2).value)

print("Has loop:", linked_list.has_loop())
print("Kth k=2 value from end:", linked_list.find_kth_from_end(2).value)

print("pop first",linked_list.pop_first())
print("pop ",linked_list.pop())
print("pop ",linked_list.pop())
print("pop ",linked_list.pop())
print("pop ",linked_list.pop())

linked_list = LinkedList(11)
linked_list.append(3)
linked_list.append(23)
linked_list.prepend(1)
linked_list.insert(2, 44)

linked_list.print_list()
print("Partition list x=23")
linked_list.partition_list(23)
linked_list.print_list()
linked_list.insert(2, 44)
linked_list.insert(2, 44)
linked_list.print_list()
print("Removing duplicates..")
linked_list.remove_duplicates_without_set()
linked_list.print_list()

linked_list.insert(2, 44)
linked_list.insert(5, 44)
linked_list.print_list()
print("Removing duplicates using set ..")
linked_list.remove_duplicates_set()
linked_list.print_list()

btod = LinkedList(1)
btod.append(1)
btod.append(0)
btod.append(0)
btod.binary_to_decimal()

rev_ll = LinkedList(11)
rev_ll.append(3)
rev_ll.append(23)
rev_ll.prepend(1)
rev_ll.insert(2, 44)
rev_ll.print_list()
print("Reversing between 2 and 4 .. ")
rev_ll.reverse_between(2,4)
rev_ll.print_list()



