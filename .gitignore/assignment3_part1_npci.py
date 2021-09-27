#!/usr/bin/env python
# coding: utf-8

# In[2]:


def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            
            if j == 0:
                
                print(f"{(2*i + 1)}", end=" ")
                count = 2*i + 1
                
            else:
                print(f"{count+1}",end=" ")
                count = count + 1
                

                
            
            
        

     
        # ending line after each row
        print("\r")


# In[3]:


n = 3
triangle(n)


# In[ ]:





# In[ ]:




