#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=input("Enter a number in comma::")
s=num.split(",")
minimum=999
maximum=0
for c in s:
    if int(c)>maximum:
        maximum=int(c)
    if int(c)<minimum:
        minimum= int(c)
print("The maximum value is : ", maximum)
print("The minimum value is : ", minimum)

