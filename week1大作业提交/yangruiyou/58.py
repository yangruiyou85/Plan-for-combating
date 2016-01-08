#-*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time


url='http://bj.58.com/pbdn/?PGTID=0d100000-0000-1121-f41b-137aeef068b7&ClickID=6'
wb_data=requests.get(url)

soup=BeautifulSoup(wb_data.text,'lxml')
#print (soup)
#pro_title=soup.select('.tbody.tr:nth-child > td.t')
#pro_title=soup.select('.t')
pro_title=soup.select('.t > a[target="_blank"]')[0].text
print (pro_title)

#print (pro_title)
#print (pro_title)
view_count=soup.select('ul.mtit_con_left.fl > li.count')
note_time=soup.select('ul.mtit_con_left.fl > li.time')
#pro_price=soup.select('div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-child')
pro_price=soup.select('div.su_con>span.price')
bug_type=soup.select('#divContacter > ul > ul')
area=soup.select('tbody > tr:nth-child > td.t')
pro_type=soup.select('#infolist > div.filterbar > table > tbody > tr > td:nth-child > div > h1')
print (pro_title,view_count,note_time,pro_price,bug_type,area,pro_type)

print ('杨瑞友')

for pro_title,view_count,note_time,pro_price,bug_type,area,pro_type in zip(pro_title,view_count,note_time,pro_price,bug_type,area,pro_type):
  data={
  'pro_title':pro_title.get_text(),
  'view_count':view_count.get_text(),
  'note_time':note_time.get_text(),
  'pro_price':pro_price.get_text(),
  'bug_type':bug_type.get_text(),
  'area':area.get_text(),
  'pro_type':pro_type.get_text()

  }
  print (data)


'''
老师先提交下，作业是没完成。周末我只能好好研究下。
'''
