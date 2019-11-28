#-*-coding:UTF-8-*-
#-*-encoding=UTF-8-*-

from bs4 import BeautifulSoup
import requests
import traceback

defaultSeperator = ','
resultHeaders = ['问题ID','标签','价格','描述']
sourceFilePath = './id_list.csv'
resultFilePath = './patient_questions.csv'

print('Starting crawling questions ...')

id_list=[]

with open(sourceFilePath) as sf:
	next(sf)
	lines = sf.readlines()
	with open(resultFilePath, 'w' , encoding='utf-8') as rf:
		
		rf.write(defaultSeperator.join(resultHeaders))
		
		for line in lines:
			q_id = line.strip()
			print(q_id)
			url = "https://bbs.guahao.com/question/" + q_id
			res = requests.get(url)
			soup = BeautifulSoup(res.text,'html.parser')
			
			detail = soup.select('[class=g-detail]')[0]
			
			labels = detail.select("ul > li")
			label = ""
			for l in labels:
				label += l.text.strip()+" "
			
			price = detail.select('[class=g-price]')[0].text.strip()
			
			describtion = soup.find(attrs={"name":"description"})['content'].split("，，")[0].replace("\n"," ").replace("\t"," ").replace(",","，")
			#describtion = detail.select('[class=g-question]')[0].text.strip()
			#print(describtion)
			rf.write('\n'+defaultSeperator.join([q_id,label,price,describtion]))

