#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

# L = ['bob', 'about', 'Zoo', 'Credit']

# print(sorted(L))
# print(sorted(L, key=str.lower))

students = {'Bob': 75, 'Adam':92, 'Bart':66, 'Lisa':88}

# print(sorted(students, key=itemgetter(0)))
# print(sorted(students, key=lambda temp: temp[1]))
# print(sorted(students, key=itemgetter(1), reverse=True))

temp = sorted(students.items(),key=lambda temp: temp[1], reverse = True)
print(temp)
print(len(temp))
i=0
while i<6 & i < len(temp):
	print(temp[i])
	i=i+1
#Contact GitHub API Training Shop Blog About
