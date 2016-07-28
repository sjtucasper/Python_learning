#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

# L = ['bob', 'about', 'Zoo', 'Credit']

# print(sorted(L))
# print(sorted(L, key=str.lower))
class student:
	def __init__(self, name, score):
		self.name = name
		self.score = score

anna = student('anna', 96)
bob = student('bob', 76)
Adam = student('Adam',65)
Bart = student('bart',33)

a={'1':bob,'2':bob,'3':anna,'4':Bart}
print(a)
print(sorted(a.items(),key=lambda temp: temp[1].score))

# students = {'Bob': 75, 'Adam':92, 'Bart':66, 'Lisa':88}

# # print(sorted(students, key=itemgetter(0)))
# # print(sorted(students, key=lambda temp: temp[1]))
# # print(sorted(students, key=itemgetter(1), reverse=True))

# temp = sorted(students.items(),key=lambda temp: temp[1], reverse = True)
# print(temp)
# print(len(temp))
# i=0
# while i<6 & i < len(temp):
# 	print(temp[i])
# 	i=i+1
# #Contact GitHub API Training Shop Blog About
