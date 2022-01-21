# #fstring
# from cgi import print_environ


# name='pari'
# age=23
# print(f"Hello my name is {name} and age is {age}")

# answer = 35
# print(f"your answer is {answer}")

#ternary oprator
# a=20
# b=40
# min=a if a<b else b
# print(min ,"is minimum")

#lambda function
# minus = lambda x,y:x-y 
# print("The substraction is ",minus(10,5))

# a =[[5,2,9],[8,22,3],[55,66]]
# a.sort(key=lambda x:x[1])
# print(a)

# numbers=["3","34","56"]
# numbers = list(map(int,numbers))


# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])

#args kwargs



# def funargs(*args):
#     print(type(args))
#     print(args[0])
# har =["pari","harry","skillf","sid"]
# funargs(*har)

def funargs(normal,*args):
    for item in args:
        print(item)
    print(normal)

har =["pari","harry","skillf","sid"]
normal = "this is normal"
funargs(normal,*har)