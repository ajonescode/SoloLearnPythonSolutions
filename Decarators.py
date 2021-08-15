#Decorators provide a way to modify functions using other functions. 
#This is ideal when you need to extend the functionality of functions that you don't want to modify.
#Example:



def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()