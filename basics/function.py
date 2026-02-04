# # A function is a block of code that:

# # Does one specific task

# # Can be reused multiple times

# # Real life:

# # Making tea → same steps every time → function ☕

# # def function_name(parameters):
# #     code
# #     return value


# def add(x,y):
#     return x+y
# print(add(10,20))

# def multiply(x,y):
#     return x*y
# print(multiply(10,20))

# def subtract(x,y):
#     return x-y
# print(subtract(10,20))

# def divide(x,y):
#     return x/y
# print(divide(10,20))    


# def greet(name):
#     print("Hello",name)

# greet("Mimoh")


# # // functions with parameters

# def greet(name):
#     print("Hello",name)

# greet("Mimoh")
# greet("Shukla")


# # return statement
# def square(num):
#     return num * num

# result = square(5)
# print(result)


# # // default parameter

# def greet(name="World"):
#     print("Hello",name)

# greet()


# # lambda functions 
# # Used for small, quick logic.

# # lambda arguments: expression

# add=lambda x,y:x+y
# print(add(10,20))


def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')