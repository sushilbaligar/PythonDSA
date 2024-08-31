# Create a class Cookie
class Cookie:
    # self keyword differentiates method and a function, 
    # If it has self, it is a Method, that is part of a class.
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

# Cookie_one is variable name. Instead of setting it to be integer or string, We are setting it to type 'Cookie' passing color green.
# This gets passed to constructor and that creates a green Cookie.  
cookie_one = Cookie("green") # Cookie(green) triggers the __new__ method, which allocates memory for the object. The __init__ method is then called to initialize the object.
cookie_two = Cookie("blue")

print('Cookie one is ',cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

cookie_one.set_color("Yellow")
print('\nCookie one is now ', cookie_one.get_color())
print('Cookie two is still ', cookie_two.get_color())