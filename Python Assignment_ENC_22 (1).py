#!/usr/bin/env python
# coding: utf-8

# # Python Assignment By Mitali Kashaveni_Roll no-22_ENC 

# ###### Q.1. Write a Python program to calculate the length of a string. 

# In[2]:


# This will give length of the string.
# In lenght space is also calculated with the number of letters in that string. 
length = len(input('enter a string or any sentence :  '))
print(length)  


# In[ ]:





# ###### Q.2. Python Program to calculate the square root.

# In[3]:


# This will calculate the square root of the given number. 
# Input means user gives the number. 
import math
number = float(input("Enter a number: "))
sqrt = math.sqrt(number)
print(f"The square root of {number} is {sqrt}")


# In[ ]:





# ###### Q.3. Write a Python program to convert temprature in Celcius to temprature in Fahrenheit.

# In[1]:


# This will convert temperature in celcius to temprature in fahrenheit. 
# Here we will use f = c * 9/5 + 32 this formula to convert the temperature. 
def celsius_to_fahrenheit(c):
  f = c * 9/5 + 32
c = float(input('temperature in celsius: '))
f = (celsius_to_fahrenheit(c))
print(f'{c}°C is {f}°F.')


# In[ ]:





# ###### Q.4. Write a data type needed for given data.(10,4.5,2+6j). 

# In[2]:


# In this we have to print the type of the given data. 
data = (10, 4.5, 2+6j)
# this is interger type .
a = 10 
print(type(a)) 
# this is float type .
b = 4.5 
print(type(b))
# this is complex type. 
c = 2+6j
print(type(c))


# In[ ]:




