#!/usr/bin/env python
# coding: utf-8

# In[20]:


x=input("Enter the date : ")
dt = x.split("/")

import datetime

date = datetime.datetime.now()
a = int(dt[0])
b = int(dt[1])
c = int(dt[2])
if a>(date.day) or b>(date.month) or c>(date.year):
    print("Greater")
elif a<(date.day) or b<(date.month) or c<(date.year):
    print("Lesser")
else:
    print("Equal")
    

