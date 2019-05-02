import requests
import bs4
import re
import os

r=requests.get("https://book.douban.com/subject/30428815/comments/")
# print(r.status_code)
# # print(r.text)
# print(r.url)

bsoup=bs4.BeautifulSoup(r.text,"lxml")
pcontent=bsoup.find_all("span","short")
num=0
# for i in pcontent:
#     print(num,i.string,'\n')
#     num+=1
f2=[]
# os.mknod("doubancontent.txt")
with open("doubancontent.txt",'w') as f1:
    # f1.writelines(pcontent)
    for i in pcontent:
        f2.append(i)
        f2[num]=str(i)+str(f2[num])
        num+=1
        
        # f1.writelines(num)
        f1.writelines(i.string)
        
        