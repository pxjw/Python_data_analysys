#print ("helloworld!")
import numpy as np
import math
#import matplotlib.pyplot as plt
#t = np.arange(0., 4., 0.1)
#plt.plot(t, t, t, t+2, t, t**2)
#plt.show()    # Spyder中可不加此条语句
# PI=3.13424,32323,4343
# x1,x2,x3=PI
# print(PI)

# num=123
# num=num//10%10
# print (num)
# print(math.gcd(16,24))
# print(math.gcd(24,16))
# surname=input("Input your surname:")
# firstname=input("Input your firstname")
# print("Your surname is: ",surname)

# print("Your firstname is:",firstname)

# print("Your full name is:",surname,firstname)
# print(ord('D')-ord('A'))
# a=1/2+2.5
# print(a)
# print(math.pi)
# # dir(math)
# help(math)
from random import randint

# x=randint(0,400)
# print(x)
# while (1):
#     inputnum=int(input("input your num:"))
#     if inputnum==x:
#         print ("bingo")
#         break
#     elif inputnum>x:
#         print ("too big")
#     elif inputnum<x:
#         print ("too small")

#Range Function
#python 3 的range函数类似一个lazy list,本质上是一个生成器
# a=list(range(3,13,2))
# print(a)

# For Loop
# for iter_var in iterable_object

# question 1:
# 输入一个整数，求逆序数。
# x= int(input("please enter a num:"))
# m=x
# s=0
# while x!=0:
#     s=s*10+x%10
#     x//=10

# print("逆序数：({:d}) = {:d}".format(m,s))
# for i in range(1,10,2):
# #     print (i)
# with open('test.txt', 'r+') as fp:
#     fp.seek(15)
#     print(fp.readline())
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[0: 2])
# x = [2, 3, 0, 4, 1]
# x.sort()
# print(x)
# print(list('Life is short, you need Python.').count('is'))
# language = list('PHP'); 
# language[1:] = 'ython'; 
# print(language) 
# # print(list('Life is short, you need Python.').count('is'))
# words = ['Life', 'is', 'short', 'you', 'need', 'Python'] 
# print(words.index('you'))

# help(str)
my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]
print(my_list)
print('short' in my_list)
print(my_list[5])