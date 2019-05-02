# 定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）
# 输入格式:
# 字符串
# 输出格式：
# 列表

# 输入样例：
# Hello, World!

# 输出样例：

# [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]

def countchar(string):
    
    s=string.lower()
    l=[]
    for i in range(ord('a'),ord('z')+1):
        l.append(s.count(chr(i)))
    # l=[s.count(chr(i)) for i in range(ord('a'),ord('z')+1)]
        #将a-z的数值装到i，l[i]等于对应数值的位置出现的次数
    return l


if __name__ == "__main__":
    string = input()
    print(countchar(string))


    