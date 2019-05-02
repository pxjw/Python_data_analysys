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