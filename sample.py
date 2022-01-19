# # print("Paritosh")

# # print("Paritosh\n" *5)

# # print('paritosh\'s "pardeshi"')

# # print(r'Pari'+'Tosh\n'*5)

# # #Variables
# # #float 
# # x= 2.2
# # y=3
# # print(type(x))
# # print(type(y))

# # #type cast
# # x=-1
# # y=1.91
# # z=1+5j

# # print(x,y,z)


# # print(int(y))

# # c= int(y)
# # print(c)

# # #input
# # print("Enter number")
# # inp =input()
# # print("you entered",int(inp))

# # print(input("Enter number"))
# # print("You entered",input)

# # #add no
# # # print("Enter first number")
# # # f1=input()

# # # print("Enter Second number")
# # # f2=input()
# # # print("addition is", int(f1)+int(f2))

#  #Strings
# from curses.ascii import isalnum


# mystr ="Pari is a good boy"
# print(mystr)
# #length
# print(len(mystr))
# #slicing
# print(mystr[1:6])

# print(mystr[0:50])

# print(mystr[5::50])

# print(mystr[-2])

# print(mystr.isalpha())
# print(mystr.count("i"))

# #Capitalize
# print(mystr.capitalize())


# print(mystr.lower())

# print(mystr.upper())
# #Find
# print(mystr.find("i"))

# print(mystr.replace("is", "are"))

# # c='32'
# # print(c.isalnum())

# #Lists 
# grocery =["harpic","deo","soap","shampoo"]
# print(type(grocery))

# print(grocery[2])

# numb =[2,5,4,6,5,4,3,18]

# print(numb[2:6])

# print(max(numb))

# apnd =numb.append(100)
# print(numb)
# # numb.sort()
# # print(numb)

# # numb.reverse()
# # print(numb)

# #Extended Slice
# # print(numb[::-1])

# numb.insert(0,69)
# print(numb)

# numb.remove(69)
# print(numb)
# numb.pop()
# print("pop" ,numb)

# #Tuples
# tp=(1,5,60)
# print(type(tp))

# #swap
# a=10
# b=20
# a,b=b,a
# print(a,b)

# #Dictionary - key value pairs
# dict ={'name':'pari',
#         'comp':'sankey',
#         'Shubham':{'B':"maggie",'L':"Burger",'D':"Pizza"}}

# print(dict["Shubham"])  
# del dict["comp"]
# print(dict)  

# print(dict.get("name"))

# print(dict.update({'Meena':'coffe'}))
# print(dict)

# print(dict.items())

# #if else elif
# var1 = 60
# var2= 6
# if var1>var2:
#     print(var1,"is greater")
# else:
#     print(var2,"is Greater")

# if var1==var2:
#     print("equal")

# from re import I


# list=[2,5,7,6,9,]
# if 5 in list:
#     print("5 is in list")
#     #not in 
# list=[2,5,7,6,9,]
# if 15 not in list:
#     print("15 is Not in list")

#  #age validation for driving   
# print("Enter your age")
# age=int(input())

# if age<7:
#     print("Invalid age")
# if age>100:
#     print("Invalid age")
# if age>18:
#     print("You can Drive")
# else:
#     print("You can not drive")

#loops
# list1=["pari","mari","carry","harri"]
# for item in list1:
#     print(item)

# list1=[["pari",10],
# ["mari",15],
# ["carry",11],
# ["harri",69]],
# for item in list1:
#     print(item,)



# items =["pArry","abc",1,2,8,7,3,6,99,44,222,5]

# for item in items:
#     if str(item).isnumeric() and item>6:
#         print(item)

##while loop
# i=0
# while(i<40):
#     print(i)
#     i=i+1 



# n=20
# print("Enter number")
# num= int(input())

# if num>n:
#     print("You entered big number")
# if num==n:
#     print("COngo you are correct")

# if num<n:
#     print("Smaller number")

# ##OPRATORS
# a=True
# b= False
# print(a or b)

# a=True
# b= False
# print(a and b)

#Exception in python



# try:
#     f=open("does.txt")
# except Exception as e:
#     print(e)

# print("important stuff")

# #finally
# try:
#     f=open("does.txt")
# except Exception as e:
#     print(e)
# finally:
#     print("run this anyway ....")
# print("important stuff")

f=open("pari.txt","w")
f.write("Welcome to python world")

print(f)
f.close()

