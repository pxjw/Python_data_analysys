# 题目内容：

# 如果一个n位数刚好包含了1至n中所有数字各一次则称它们是全数字（pandigital）的，例如四位数1324就是1至4全数字的。从键盘上输入一组整数，输出其中的全数字，若找不到则输出“not found”。
#       调用函数根据结果输出

# 输入格式:
# 多个数字串，中间用一个逗号隔开

# 输出格式：
# 满足条件的数字串，分行输出

# 输入样例：
# 1243,322,321,1212,2354

# 输出样例：
# 1243
# 321


def pandigital(nums): 
    # l=sorted(nums)
    flag=False
    # pandig=[]
    # nums=str(nums)

    for n in nums:
        n=str(n)
        ladig=[str(i) for i in range(1,len(n)+1)]
        xlading=[x for x in ladig if x in n]
        if len(ladig)==len(xlading):
            print(n)
            flag=True
    if flag==0:
        print("not found")



if __name__ == "__main__":
    lst = pandigital(eval(input()))
