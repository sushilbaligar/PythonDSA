# Insertion Sort
def insertion_sort(arr):
    # Insertion Sort
    # 1. Iterate through the array starting from the second element
    # 2. For each element, compare it with the elements before it
    # 3. If the element is smaller than the elements before it, swap them
    # 4. Continue until the end of the array
    # 5. Return the sorted array
    # for i in range(1, len(arr)):
    #     temp = arr[i]
    #     j = i - 1
    #     while temp < arr[j] and j > -1:
    #         arr[j + 1] = arr[j]
    #         arr[j] = temp
    #         j -= 1
    # return arr
    for i in range(1, len(arr)):
        #temp = arr[i]
        j = i - 1
        while arr[i] < arr[j] and j > -1:
            arr[i],arr[j] = arr[j],arr[i]
            i -= 1
            j -= 1
    return arr

print(insertion_sort([4,2,6,5,1,3]))

# INSERTION SORT LINKEDLIST

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

#     def sorted_insert(self, sorted_list, new_node):
#         if sorted_list is None or sorted_list.value >= new_node.value:
#             new_node.next = sorted_list
#             sorted_list = new_node
#         else:
#             curr = sorted_list
#             while curr.next is not None and curr.next.value < new_node.value:
#                 curr = curr.next
#             new_node.next = curr.next
#             curr.next = new_node
#         return sorted_list

#     def insertion_sort(self):
#         if self.length < 2:
#             return
#         sorted_list = None
#         curr = self.head
#         while curr is not None:
#             next_node = curr.next
#             sorted_list = self.sorted_insert(sorted_list, curr)
#             curr = next_node
#         self.head = sorted_list

# my_linked_list = LinkedList(4)
# my_linked_list.append(2)
# my_linked_list.append(6)
# my_linked_list.append(5)
# my_linked_list.append(1)
# my_linked_list.append(3)

# print("Linked List Before Sort:")
# my_linked_list.print_list()

# my_linked_list.insertion_sort()

# print("\nSorted Linked List:")
# my_linked_list.print_list()



# """
#     EXPECTED OUTPUT:
#     ----------------
#     Linked List Before Sort:
#     4
#     2
#     6
#     5
#     1
#     3

#     Sorted Linked List:
#     1
#     2
#     3
#     4
#     5
#     6

# """

