# Selection Sort
def selection_sort(arr):
    # Finds minimum value in array and swaps it with the first element
    # Then finds the next minimum value and swaps it with the second element
    # This process continues until the array is sorted
    # Time Complexity: O(n^2) as there are two nested loops
    # Space Complexity: O(1) as it sorts in place
    # Stable: No as the relative order of equal elements is not preserved
    # In-Place: Yes as it sorts the array in place without using any additional data structures
    # Online: No as it requires the entire array to be sorted before it can process new data
    # Adaptive: Yes as it is efficient for already sorted data sets

    for i in range(len(arr)-1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([4,2,6,5,1,3]))

# SELECTION SORT LINKEDLIST

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

    def selection_sort(self):
        if self.length < 2:
            return
        curr = self.head
        while curr.next is not None:
            smallest = curr
            inner_curr = curr.next
            while inner_curr is not None:
                if inner_curr.value < smallest.value:
                    smallest = inner_curr
                inner_curr = inner_curr.next
            if smallest != curr:
                curr.value,smallest.value = smallest.value, curr.value
            curr = curr.next
        

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

