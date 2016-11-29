# -*- coding: UTF-8 -*-
import re

f = open('data/1.txt')
f.readline()
line = f.readline().strip()

res = re.split('。|，|！|？', line)
for ele in res:
    print ele
