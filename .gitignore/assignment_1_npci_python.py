#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##assumption lets consider the index position as role number of student.
## we will create the three list as math,chem,phy.
## score will be out of 100


# 

# In[1]:




    

    
    
math = []
phy = []
chem = []
listof_rollno_reappering_std = []
listof_rollno_failure_std = []
passlist = []
distinction = []
firstclass = []
secondclass = []
N = int(input("please provide the no of studentin the class: ")) 

for i in range(N):
    
    
        
        
        
        
        
    mathmarks = int(input(f"please provide math marks of roll no {i}  student: "))
    math.append(mathmarks)

    
    phymarks = int(input(f"please provide phy marks of roll no{i}  student: "))
    phy.append(phymarks)
    
    chemmarks = int(input(f"please provide chem marks of roll no{i}  student: "))
    chem.append(chemmarks)
    

    










    


# In[2]:


def result():
    N = int(input("please provide the no of studentin the class: ")) 
    for i in range(N):
        if (math[i] < 50 and chem[i] < 50) or (math[i]<50 and phy[i]<50) or (chem[i]<50 and phy[i]<50) or(chem[i]<50 and math[i]<50 and phy[i]<50):
            print(f"student of roll no{i} is failed!!!")
            listof_rollno_failure_std.append(i)
            
        elif (math[i] <50 and chem[i]>50 and phy[i]>50) or (phy[i] <50 and math[i]>50 and chem[i]>50) or (chem[i] <50 and phy[i]>50 and math[i]>50):
            print(f"student of roll no {i}  can reappear!!!")
            listof_rollno_reappering_std.append(i)
            
        else:
            print(f"for student of roll no {i} result is PASS")
            performance(math[i],phy[i],chem[i])
            passlist.append(i)
                
            
     


# In[3]:


def performance( math, phy, chem):
    sum = math + phy + chem
    percentage = (sum * 100)/300
    print(f" percentage of student is {percentage}")
    if percentage>80 :
        print("/n !!!! Distinction!!!!")
        distinction.append(i)
        
    elif 60 <= percentage <=79 :
        print("/n !! first class")
        firstclass.append(i)
    elif 50 <= percentage <=59:
        print("/n !! second class")
        secondclass.append(i)
        
    


# In[4]:


def classperformance():
    T_passed_student = len(passlist)
    T_failure_student = len(listof_rollno_failure_std) + len(listof_rollno_reappering_std)
    T_firstclass = len(firstclass)
    T_distinction = len(distinction)
    T_secondclass = len(secondclass)
    print(f"distinction % is { (T_distinction * 100) /T_passed_student }")
    print(f"first class % is {(T_firstclass * 100)/T_passed_student}")
    print(f"secondclass class % is {(T_secondclass * 100)/T_passed_student}")

        


# In[5]:


result()


# In[6]:


classperformance()


# In[ ]:




