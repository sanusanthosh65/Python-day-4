#!/usr/bin/env python
# coding: utf-8

# # Question 1 - find all the occurance of substring in the given string.

# In[7]:


test_str = "what we think we become ; we are python programmer"
test_sub = "we"
print("The orginal string is :"  + test_str)
print("The substring to find :" + test_sub)
res = [i for i in range (len(test_str)) if test_str.startswith(test_sub,i)]
print("The index values are :" + str(res))


# # Question 2 - islower() ,isupper()

# In[8]:


str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())

str = "THIS is string example....wow!!!"
print (str.isupper())


# In[9]:


str_name = "welcome python user"
print(str_name.islower())   
  
str_name = "welcome 2019"
print(str_name.islower())   
  
str_name = "welcome @ 2020"
print(str_name.islower()) 

