# Python数据分析笔记

多重赋值

```python
PI=3.13424,32323,4343
x1,x2,x3=PI
print(PI)
```

生成随机数猜数字游戏

```python
from random import randint

x=randint(0,400)
print(x)
while (1):
    inputnum=int(input("input your num:"))
    if inputnum==x:
        print ("bingo")
    elif inputnum>x:
        print ("too big")
    elif inputnum<x:
        print ("too small")
```
###将一个正整数分解质因数。
```python

n=int(input("please input a number:"))
print(n,'=',end='')
i=2
while n!=1:
    while n%i==0:
        n//=i
        if n==1:
            print('{:d}'.format(i))
        else:
            print('{:d}*'.format(i),end='')
    i+=1    

```
### 输入一个整数，求逆序数

```python
realnum=int(input("please enter a num:"))
xnum=0

while realnum!=0:
    #取模，最后一个数作为最大数
    xnum=xnum*10+realnum%10
    #取整，去除最小的数
    realnum=realnum//10

print(xnum)

```

```
#递归
#fibonacci
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(1,10,2):
    print(fibonacci(i))
```


```
#汉诺塔
def hanoi(a,b,c,d):
    if d==1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,d-1)
        print(a,'->',c)
        hanoi(b,a,c,d-1)
hanoi('a','b','c',2)
```

### 寻找n以内的亲密数对

```python
#对于两个不同的整数A和B，如果整数A的全部因子（包括1，不包括A本身）之和等于B；且整数B的全部因子（包括1，不包括B本身）之和等于A，则将A和B称为亲密数。自定义函数fac(x)计算x包括1但不包括本身的所有因子和并返回。从键盘输入整数n，调用fac()函数寻找n以内的亲密数并输出。注意每个亲密数对只输出一次，小的在前大的在后，例如220-284。

#定义一个取因子函数
def malenum(m):
    t=0
    for j in range(1,m):
        if(m%j==0):
            t=t+j
    return t


def fac(n):
    # left=0
    right=0
    for i in range(1,n):
        #遍历1->n个数字
        right=malenum(i)
        if(i==malenum(right) and i<right and right<n):
            print("{:d}-{:d}".format(i,right))

        # for x in range(1,i//2):
        #     if(i%x==0):
        #         left=left+x
        # for x in range(1,left//2):
        #     if(left%x==0):
        #         right=right+x
        #     if(left==right and i<left):
        #         print("{:d}-{:d}".format(i,left))


fac(int(input()) )
```



