
# coding: utf-8

# In[27]:


name= input('Enter First and Last Name ')
l = name.split(' ')

l=l[::-1]

str1 = ' '.join(l)

print(str1)




# In[15]:


list1 = ['1', '2', '3']
str1 = ''.join(list1)
print(str1)


# In[10]:


mylist = ['spam', 'ham', 'eggs']
print ', '.join(mylist)

