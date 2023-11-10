#!/usr/bin/env python
# coding: utf-8

# # Data Types in Python

# In[2]:


## Data types in Python are classifications of the data we are storing.
## This tells us what types of operations can be performed on our data


# ## Numeric Data types

# In[ ]:


## We have 3 different data types connected to integers (numbers)


# ### Integers

# In[ ]:


## A whole number, positive or negative


# In[6]:


type (12)
type (-12)
type (-12+100)


# ### Float

# In[ ]:


### Decimal numbers


# In[7]:


type (12+10.25)


# ### Complex Numbers

# In[ ]:


### Used for imaginary numbers, j is the only one that works with it


# In[8]:


type (12 + 3j)


# ## Boolean values (True & False)

# In[12]:


type(True) ## Bool is same as Boolean, either it is true or false
type (False)


# In[13]:


type (1 > 5) # this give us a boolean since it shows if 1 is greater than 5


# In[14]:


1 > 5 # this is false since 1 is not greater than 5


# In[15]:


1 == 1 # is true


# # Sequence Data types

# ### Strings

# In[47]:


## When you use strings you either put the in a single qoute, double qoute or tripple qoute. 
## This is stored as one value with multiple characters


# In[48]:


'Single Qoute'
"Double Qoute"


# In[49]:


multiline = """
The ice cream is very icy

""" ## this is basically the tripple qoute where one can write stuff


# In[50]:


print (multiline)


# In[51]:


## Strings can be indexed, meaning that you can search within it and that index starts at 0.


# In[52]:


a = 'Hello World'


# In[53]:


print (a[:5]) ##Gives us the first 5 positions of the string


# In[54]:


print (a[6]) ##Gives us the position 6 of the string


# In[55]:


print (a[-3]) ##Gives us the position 3 (counting backwards) from the string


# In[56]:


print (a[2:5]) ##Gives us the frist 5 positions counting from 2 --> (position 3,4,5)


# In[57]:


a*3 ## Give us our variables 3 times in a row or a + A


# ### Lists 

# In[23]:


## lists store multiple values, a list can store multiple separate values.


# In[35]:


[1,2,3] # the bracket means that it is going to be a list, we create a list with 3 separate values in it. 


# In[ ]:


# A list is indexed just as strings are indexed


# In[38]:


['Cookies', 'Strawberry', 'Chocolate']  # you can put strings or anything you want inside lists


# In[39]:


['Vanilla', 3, ['Scoops', 'Spoon'], True] #this is a list within a list


# In[41]:


ice_cream = ['Cookies', 'Strawberry', 'Chocolate'] #Good thing about lists are that we can change them
ice_cream.append('Salted Caramel') #here we add salted caramel at the end of the list
ice_cream


# In[42]:


ice_cream[0]='Butter Pecan' #in this case we index the first position which is cookies and replace it with the value
ice_cream


# In[ ]:


nest_list = ['Vanilla', 3, ['Scoops', 'Spoon'], True]


# In[ ]:


nest_list [0] #give us vanilla
nest_list [2] # gives us ['Scoops', 'Spoon']
nest_list [2] [1] # gives us 'Spoon' since it is our first value inside the parathatese


# # Tuples

# In[58]:


# Similar to lists, but biggest difference is that a tuples is immutable, so it CAN'T be modified or changed
#People use tuple when data is never going to change (so its not as popular as lists)


# In[59]:


tuple_scoops = (1,2,3,2,1)
type (tuple_scoops)


# In[60]:


tuple_scoops[0] # but we cant do append to add a value


# # Sets

# In[ ]:


# similar to a list and a tuple but they don't have duplicate elements
# also the values within a set cannot be accessed using an index because it doesn't have an index, because it is unordered
# Although we can loop through items in a set with a forloop but we can't use it acccessing the bracket
# Use case for this is to compare two different sets


# In[2]:


daily_pints ={1,2,3}


# In[3]:


type (daily_pints)


# In[4]:


print (daily_pints)


# In[5]:


daily_pints_log = {1,2,31,2,3,4,2,5,6,3,2,7,7,8}


# In[6]:


print (daily_pints_log) # here it only prints the unique values, so the 7 for example only whos up one time


# In[7]:


wifes_daily_pints_log = {1,3,5,7,3,24,5,7,3,2,0} #here we can compare the two values


# In[8]:


print (daily_pints_log | wifes_daily_pints_log) #This basically gives us all the combined unique values between the 2 sets


# In[9]:


print (daily_pints_log & wifes_daily_pints_log) #This shows us which values that matches, values that show up in both of the sets


# In[10]:


print (daily_pints_log - wifes_daily_pints_log) #This shows us what does not match in the two sets


# In[11]:


print (daily_pints_log ^ wifes_daily_pints_log) #Shows if a value is in one or the another, but not in both. Unique in each of the sets


# # Dictionaries

# In[ ]:


# Key/Value pair, you call a dictionary from its pair


# In[14]:


dict_cream = {'name': 'Alex Freberg','Weekly intake': 5, 'favorite ice creams': ['MCC', 'Chocolate']}


# In[15]:


type(dict_cream)


# In[16]:


print(dict_cream)


# In[17]:


dict_cream.values() #These are basically all our values within our key pairs


# In[18]:


dict_cream.keys() #This is our key value


# In[19]:


dict_cream.items() #This is our key value pairs, basically name and Alex Freberg are a key value pair, weekly intake and 5 also.


# In[ ]:


dict_cream.keys() #This is our key value


# In[20]:


dict_cream['name']


# In[23]:


dict_cream['name']= 'Christine Freberg' #updating the name
print (dict_cream)


# In[25]:


dict_cream.update({'name': 'Kimiya E', 'Weekly intake': 5, 'weight': 300}) #We can update the whole thing here, but we can't delete the old values!
print (dict_cream) #The value of the key value pair can change, but the actual whole key value pair cannot. So you can't delete anything, just modifying it.


# In[26]:


del dict_cream['weight'] # This is how you delete something
print (dict_cream)


# In[ ]:




