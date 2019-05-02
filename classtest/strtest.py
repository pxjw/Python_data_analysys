# 1、使用以下语句存储一个字符串：
#   string = 'My moral standing  is: 0.98765'
# 将其中的数字字符串转换成浮点数并输出。  
# （提示：可以使用find()方法和字符串切片或split()方法，提取出字符串中冒号后面的部分，然后使用float函数，将提取出来的字符串转换为浮点数）


# string = 'My moral standing  is: 0.98765'
# print(string)
# strfloat = string.split(':',1)
# print(float(strfloat[1]))

# 2\自定义函数move_substr(s, flag, n)，将传入的字符串s按照flag（1代表循环左移，2代表循环右移）的要求左移或右移n位（例如对于字符串abcde12345，循环左移两位后的结果为cde12345ab，循环右移两位后的结果为45abcde123），结果返回移动后的字符串，若n超过字符串长度则结果返回-1。__main__模块中从键盘输入字符串、左移和右移标记以及移动的位数，调用move_substr()函数若移动位数合理则将移动后的字符串输出，否则输出“the n is too large”。

# def move_substr(s, flag, n):
#     srt=[]
#     if flag==1:
#         srt=s[n:]+s[:n]
#         return srt
#     if flag==2:
#         srt=s[len(s)-n:]+s[:len(s)-n]
#         return srt
#     else:
#         return -1

# if __name__ == "__main__":
#     a=input("enter a string:")
#     b=int(input("enter a flag,1 or 2:"))
#     c=int(input("enter a number,no more len(str):"))
#     if(move_substr(a,b,c)==-1):
#         print('the n is too large')
#     else:
#         print(move_substr(a,b,c))
#     # print(b)