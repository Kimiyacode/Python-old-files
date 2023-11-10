#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("hello world")


# # First Notebook

# In[7]:


x = 22
print (x)


# In[9]:


type(x)


# In[10]:


y = 'Mint Chocolate chip'
print(y)


# In[11]:


type(y)


# In[12]:


print (y)


# In[2]:


x, y, z = 'Chocolate', 'Vanilla', 'Rocky Road'

print (x)
print (y)
print (z)


# In[ ]:


## Creating multiple variables for the same value


# In[5]:


x = y = z = 'Root Beer Float '
print (x)
print (y)
print (z)


# In[ ]:


## Creating one variable with multiple values


# In[6]:


ice_cream = ['Chocolate', 'Vanilla', 'Rocky Road']

x,y,z = ice_cream
print (x)
print (y)
print (z)


# In[8]:


#Camelcase
testVariableCase  = 'Vanilla Swirl'


# In[10]:


# Pascal Case
TestVariableCase = 'Vanialla Swirl'


# In[ ]:


# Snake Case (this is the easiest way to read, use this always
test_variable_case = 'Vanilla Swirl'


# In[15]:


## ways you can write variables
test_var = 'Vanilla Swirl'
testvar = 'Vanilla Swirl'
_test_var ='Vanilla Swirl'
testVar = 'Vanilla Swirl'
TestVar = 'Vanilla Swirl'
testVar2 ='Vanilla Swirl'


# In[ ]:


## ways you can't write variables
test var = 'Vanilla Swirl'
2testvar = 'Vanilla Swirl'
test!var ='Vanilla Swirl'
test,Var = 'Vanilla Swirl'

# In[13]:


x = 'Ice cream is my favourite' + '.'
print (x)


# In[ ]:


## you can't combine a string together with an integer! but yoiu can have a integer + an integer (3 + 2)
x = 'Ice cream is my favourite' + '2'
print (x)


# In[17]:


x = 'Ice Cream'
y = ' is'
z = ' my favourite.'

print (x+y+z)


# In[ ]:





# In[20]:


## You can combine a integer and a string by combining them with a comma ,
x = 'Ice Cream'
y = 2

print (x,y)

