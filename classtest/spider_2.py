# “迷你爬虫编程小练习”进阶:抽取某本书的前 50 条短评内容并计算评分(star)的平 均值。提示:有的评论中并不包含评分。
import requests
import bs4
import re

#定义页数
i=0
pcount=0
star=[]
starnum=0

while len(star)<50:
    # 获取资源
    r=requests.get('https://book.douban.com/subject/30398273/comments/hot?p='+str(i+1))
    bsoup=bs4.BeautifulSoup(r.text,"lxml")
    pcontent=bsoup.find_all("span","short")
    # 正则，获取分数
    pattern=re.compile('<span class="user-stars allstar(.*?) rating"')
    star.extend(re.findall(pattern,r.text))
    i=i+1
    print(star)
for rate in star:
    starnum+=int(rate)
        # pcount+=1

    # print(starnum)
        

print("average star is:{:d}".format(starnum//len(star)))

    
