#老师的代码
import requests,re,time
from bs4 import BeautifulSoup

count=0  
i=0   #页数
s,count_s,count_del=0,0,0
lst_stars=[]
while count<50:
    try:
        r=requests.get('https://book.douban.com/subject/30398273/comments/hot?p='+str(i+1))
    except Exception as err:
        print(err)
        break
    soup=BeautifulSoup(r.text,'lxml')
    comments=soup.find_all('span','short')  #直接取得评论
    
    pattern=re.compile('<span class="user-stars allstar(.*?)rating"')
    p=re.findall(pattern,r.text)
    for item in comments:
        count+=1
        if(count>50):
            count_del+=1  #超出50条记录的部分
        else:
            print(count,item.string)
            
    for star in p:
        lst_stars.append(int(star))
        
    time.sleep(5)
    i+=1  #更新页数
    
for star in lst_stars[:-count_del]:
    s+=int(star)
print("average is:{:2f}".format(s//(len(lst_stars)-count_del)))