#-*-coding:UTF-8-*-
#-*-encoding=UTF-8-*-
#coding=gbk

from bs4 import BeautifulSoup
import requests

#设置爬取页数n
n=2

defaultSeperator = ','
resultHeader = "data-id"
resultFilePath = './id_list.csv'

print('Starting crawling ...')
sourceUrl = 'https://bbs.guahao.com/help'

q_list = []

for i in range(1,n+1):
	res = requests.get(sourceUrl+"?page="+str(i))
	soup = BeautifulSoup(res.text,'html.parser')
	q_list += soup.find_all(class_="post-view-item J_GoPage")


with open(resultFilePath, "w") as rf:

	rf.write(resultHeader)
	for item in q_list:
		rf.write('\n'+item["data-id"])

