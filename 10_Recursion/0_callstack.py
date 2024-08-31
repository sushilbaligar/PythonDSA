def funcThree():
    print("This is function three")

def funcTwo():
    funcThree()
    print("This is function two")

def funcOne():
    funcTwo()
    print("This is function one")

funcOne()