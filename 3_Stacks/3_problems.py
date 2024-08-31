# Implement stack using list
class Stack:
    def __init__(self):
        self.items = []

    def print_stack(self):
        for items in self.items:
            print(items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            temp = self.items[-1]
            self.items.remove(self.items[-1])
            return temp
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stackobj = Stack()
stackobj.push(5)
stackobj.print_stack()


# IS BALANCED PARANTHESIS USING STACK
def is_balanced_parentheses(parentheses):
    stack = Stack()
    for char in parentheses:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
print(is_balanced_parentheses('((()))'))
print(is_balanced_parentheses('(()))'))


def isbalancedparanthesis(s):
    stack = []
    openbrackets = ['(','{','[']
    closebrackets = [')','}',']']
    bracketpairs = {')':'(','}':'{',']':'['}
    for char in s:
        if char in openbrackets:
            stack.append(char)
        elif char in closebrackets:
            if not stack:
                return False
            elif stack[-1] == bracketpairs[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(isbalancedparanthesis('({[]})'))

# REVERSE STRING USING STACK
def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string('hello'))
print(reverse_string('kanak'))

# SORT STACK USING TEMPORARY STACK
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

stackobj = Stack()
stackobj.push(5)
stackobj.push(3)
stackobj.push(8)
stackobj.push(1)
print("before sort:")
stackobj.print_stack()
sort_stack(stackobj)
print("after sort: ")
stackobj.print_stack()

def sortstack_list(stack):
    temp_stack = []
    while not stack.is_empty():
        temp = stack.pop()
        while len(temp_stack) > 0 and temp_stack[-1] > temp:
            stack.push(temp_stack.pop())
        temp_stack.append(temp)

    while len(temp_stack) > 0:
        stack.push(temp_stack.pop())

# IMPLEMENT ENQUEUE METHOD USING STACK
def enqueue(stack, item):
    temp_stack = Stack()
    while not stack.is_empty():
        temp_stack.push(stack.pop())
    stack.push(item)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

stackobj = Stack()
stackobj.push(5)
stackobj.push(3)
stackobj.push(8)
stackobj.push(1)
print("before enqueue:")
stackobj.print_stack()
enqueue(stackobj, 10)
print("after enqueue: ")
stackobj.print_stack()

