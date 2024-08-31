print("Hello World!")
# When you create a class, you are creating your own datatype.

class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie("red")
cookie_two = Cookie("blue")

print('Cookie one is ',cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

cookie_one.set_color("yellow")

print('\nCookie one is ', cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

int1 = 11
int2 = int1
print("\nint1,int2",int1,int2)
int2 = 22
print("\nAfter updating int2..")
print("\nint1, int2", int1, int2)

#repeat above code for dictionary
dict1 = {'a': 1}
dict2 = dict1
print("\ndict1, dict2", dict1, dict2)
dict2['a'] = 2
print("\nAfter updating dict2..")
print("\ndict1, dict2", dict1, dict2)