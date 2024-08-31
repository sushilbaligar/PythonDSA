# BST: Convert Sorted List to Balanced BST
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, curr_node, value):
        if curr_node == None:
            return Node(value)
        if value < curr_node.value:
            curr_node.left = self.__r_insert(curr_node.left, value)
        if value > curr_node.value:
            curr_node.right = self.__r_insert(curr_node.right, value)
        return curr_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, curr_node, value):
        if curr_node == None:
            return False
        if value == curr_node.value:
            return True
        if value < curr_node.value:
            return self.__r_contains(curr_node.left, value)
        if value > curr_node.value:
            return self.__r_contains(curr_node.right, value)
    
    def _r_contains(self,value):
        return self.__r_contains(self.root, value)

    def min_value(self, curr_node):
        while curr_node.left != None:
            curr_node = curr_node.left
        return curr_node.value    

    def __r_delete(self, curr_node, value):
        if curr_node == None:
            return None
        if value < curr_node.value:
            curr_node.left = self.__r_delete(curr_node.left, value)
            return curr_node
        elif value > curr_node.value:
            curr_node.right = self.__r_delete(curr_node.right, value)
            return curr_node
        else:
            if curr_node.left == None and curr_node.right == None:
                return None
            elif curr_node.left == None:
                curr_node = curr_node.right
            elif curr_node.right == None:
                curr_node = curr_node.left
            else:
                sub_tree_min = self.min_value(curr_node.right)
                curr_node.value = sub_tree_min
                curr_node.right = self.__r_delete(curr_node.right, sub_tree_min)
        return curr_node
    
    def r_delete(self, value):
        self.__delete(self.root, value)

    def sorted_list_to_bst(self, list):
        self.root = self.sorted_list_to_balanced_bst(list, 0, len(list) - 1)

    def sorted_list_to_balanced_bst(self, list,left,right):
        if left > right:
            return None
        mid = (left + right) // 2
        current = Node(list[mid])
        current.left = self.sorted_list_to_balanced_bst(list, left, mid - 1)
        current.right = self.sorted_list_to_balanced_bst(list, mid + 1, right)
        return current

    def invert_tree(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, curr_node):
        if curr_node != None:
            curr_node.left, curr_node.right = self.__invert_tree(curr_node.right), self.__invert_tree(curr_node.left)
        return curr_node

print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])




