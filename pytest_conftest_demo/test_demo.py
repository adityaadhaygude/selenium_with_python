import conftest

#import conftest file and then pass setup method as an argument in the test method.
#This will help to reduce redundancy of setup code.
def test_demo(setup):
    print("This is the demo method")

def test_demo1(setup):
    print("Another demo method")

#here we can see that for every method we have to pass setup as an argument
#This could be optimized using class and then passing texture to the class so that every method inside the class will call the textures.