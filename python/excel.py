#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

flag=0
class colleague:	#define class colleague
	
	def __init__(self, name, department):
		self.name = name	#员工姓名
		self.department = department	#部门名称	
		self.total_data = 0	#总流量
		self.data={}	#站点流量
		self.serial_number=1	#流量排名
		
	def add_data(self, site_url, total_bytes): #add data 
		if site_url in self.data:
			self.data[site_url]=self.data[site_url]+int(total_bytes)
		else:
			self.data[site_url]=int(total_bytes)
	
	def add_total_data(self, total_data): #add total data
		self.total_data =self.total_data+int(total_data)
			
def add_totaldata_from_csv(a,filename): #input data from csv file 
	with open(filename,'r') as f: 
		reader = csv.reader(f)
		for row in reader:
			if row[0] in a:
				a[row[0]].add_total_data(row[1])
			else:
				a[row[0]] = colleague('Not found', 'Not found')
				a[row[0]].add_total_data(row[1])
				noneinfocolleague.add(row[0])

def add_data_from_csv(a,filename): #input data from csv file 
	with open(filename,'r') as f: 
		reader = csv.reader(f)
		for row in reader:
			if row[0] in a:
				a[row[0]].add_data(row[1],row[6])
			else:
				noneinfocolleague.add(row[0])
				
a={} 
noneinfocolleague=set()

#input from csv file
with open('info.csv','r') as f: #input name and department
	reader = csv.reader(f)
	for row in reader:
		a[row[0]] = colleague(row[1],row[2])

add_totaldata_from_csv(a, 'total.csv')		
add_data_from_csv(a, 'morning.csv')
add_data_from_csv(a, 'afternoon.csv')

#sort
for userid in a:
	for compare in a:
		if a[compare].total_data > a[userid].total_data:
			a[userid].serial_number=a[userid].serial_number+1

#output
with open('miss_info_list.csv','w') as f:
	f.write(str(noneinfocolleague))
flag=0
serial_number=1
with open('output.csv','w') as f:
	while flag == 0:
		flag = 1
		for userid in a:
			if userid != '':
				if a[userid].serial_number == serial_number:
					flag = 0
					if a[userid].data != {}:
						count = 0
						temp_data = sorted(a[userid].data.items(),key=lambda temp: temp[1], reverse = True)
						while count < 10 :
							if count < len(temp_data):
								f.write('"%s","%s","%s","%s","%s","%s"\n'%(a[userid].serial_number, userid, temp_data[count][0], a[userid].data[temp_data[count][0]], a[userid].name, a[userid].department))
							count = count + 1
		serial_number = serial_number+1

