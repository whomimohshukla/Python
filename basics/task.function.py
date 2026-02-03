
# task-1

#  take the number as input and print the even odd using fucntiosn


def even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

num = int(input("Enter a number: "))
even_odd(num)


#task-2

def maxNumber(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

max=maxNumber(num1,num2)
print("The max number is",max)

# task-3

def squareOf(num):
    return num*num
num=int(input("Enter a number: "))
result=squareOf(num)
print("The square of",num,"is",result)


# using the lambda function

square=lambda x:x*x
print(square(5))