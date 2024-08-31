class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class rBST:
    def __init__(self):
        self.root = None

    def __insert(self, curr_node, value):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = Node(value)
                return True
            else:
                return self.__insert(curr_node.left, value)
        elif value > curr_node.value:
            if curr_node.right == None:
                curr_node.right = Node(value)
                return True
            else:
                return self.__insert(curr_node.right, value)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return True
        return self.__insert(self.root, value)

    def __r_contains(self, curr_node, value):
        if curr_node == None:
            return False
        if value == curr_node.value:
            return True
        if value < curr_node.value:
            return self.__r_contains(curr_node.left, value)
        if value > curr_node.value:
            return self.__r_contains(curr_node.right, value)
    
    def r_contains(self,value):
        return self.__r_contains(self.root, value)
    
my_tree = rBST()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.r_contains(27))
print(my_tree.r_contains(17))
