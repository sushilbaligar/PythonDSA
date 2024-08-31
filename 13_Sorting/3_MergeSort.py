def merge(list1,list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

original_list = [3, 1, 4, 2, 5]
sorted_list = merge_sort(original_list)
print("Original list:",original_list)
print("Sorted list:", sorted_list)

############################################################
############################################################
############################################################
# MERGE SORT LINKEDLIST
class Node:
    def __init__(self, value):
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

    def merge(self, other_list):
        dummy = Node(0)
        current = dummy
        temp = self.head
        other_list = other_list.head
        while temp and other_list:
            if temp.value <= other_list.value:
                current.next = temp
                temp = temp.next
            else:
                current.next = other_list
                other_list = other_list.next
            current = current.next
        while temp:
            current.next = temp
            temp = temp.next
            current = current.next
        while other_list:
            current.next = other_list
            other_list = other_list.next
            current = current.next
        self.head = dummy.next
        self.tail = current
        return self.head


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""