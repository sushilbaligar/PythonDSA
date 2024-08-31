class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class rBST:
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


    def DFS_PreOrder(self):
        results = []
        def traverse(curr_node):
            results.append(curr_node.value)
            if curr_node.left != None:
                traverse(curr_node.left)
            if curr_node.right != None:
                traverse(curr_node.right)
        traverse(self.root)
        return results
    
    def DFS_PostOrder(self):
        results = []
        def traverse(curr_node):
            if curr_node.left != None:
                traverse(curr_node.left)
            if curr_node.right != None:
                traverse(curr_node.right)
            results.append(curr_node.value)
        traverse(self.root)
        return results
    
    def DFS_InOrder(self):
        results = []
        def traverse(curr_node):
            if curr_node.left != None:
                traverse(curr_node.left)
            results.append(curr_node.value)
            if curr_node.right != None:
                traverse(curr_node.right)
        traverse(self.root)
        return results
    
 # You are tasked with writing a method called is_valid_bst in the BinarySearchTree class that checks whether a binary search tree is a valid binary search tree.   
    def is_valid_bst(self):
        results = self.DFS_InOrder()
        for i in range(len(results)-1):
            if results[i] >= results[i+1]:
                return False
        return True

# Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.
    def kth_smallest_iterative(self, k):
        stack = []
        curr = self.root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.value
            curr = curr.right

    def kth_smallest_recursive(self, k):
        self.kth_smallest_count = 0
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            return None

        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            return left_result
 
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            return node.value
 
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            return right_result

        return None

tree = rBST()
tree.r_insert(47)
tree.r_insert(21)
tree.r_insert(76)
tree.r_insert(18)
tree.r_insert(27)
tree.r_insert(52)
tree.r_insert(82)
print(tree.DFS_InOrder())
print(tree.is_valid_bst())
print(tree.kth_smallest_iterative(4))
print(tree.kth_smallest_recursive(4))