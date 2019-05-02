'''
2寻找第n个默尼森数。
代码格式如下：
def prime(num):
        ...
def monisen(no):
        … …
        return  xxx

print(monisen(int(input())))    # 此处输入由系统自动完成不需要自己输入，只要写这样一条语句即可（3分）
题目内容：

找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2^P-1，则称M为默尼森数。例如，P=5，M=2^P-1=31，5和31都是素数，因此31是默尼森数。

输入格式: 

按提示用input()函数输入

输出格式：

int类型

输入样例：

4

输出样例：

127

'''
from math import sqrt
import math
def primer(num):
        # m=[]
        if num==1:
                return False
        # flag=True
        # 一个数是否是素数看能否被从2到自身整除，被除数的上界为根号自身+1
        for i in range(2,int(math.sqrt(num)+1)):
                if num%i==0:
                        # flag=False
                        return False
        #如果没有可以被整除的被除数，则为素数
        return True

# def primer(n):
#         if n==1:
#                 return False
#         k=int(sqrt(n))
#         for i in range(2,k+1):
#                 if n%i==0:
#                         return False
#         return True


def monisen(no):
        P=2
        M=0
        l1=[]
        number=0
        # if no==1:
        #         return 3
        # elif no==2:
        #         return 5
        
        while  1:
                if primer(P):
                        M=2**P-1
                        if primer(M):
                                l1.append(M)
                                #计数器
                                # continue
                                number+=1
                                if number==no:
                                        break
                P+=1
        return l1[number-1]

print(monisen(int(input())))

# print(primer(int(input())))


