#!/usr/bin/env python
# coding: utf-8

# # SAAD ULLAH KHAN WARSI ASSIGNMENT 3

# In[1]:


from functools import reduce
import               

my_dict = {
    
'person_1':{ 'name' : 'Abdul Rafay', 'age':22, 'Interests':['football','cricket'], 'amount_deposited':[24000,26000] },
'person_2':{ 'name' : 'Nancy James', 'age':23, 'Interests':['baseball','cricket'], 'amount_deposited':[24000,27000] },
'person_3':{ 'name' : 'Selena Gomez', 'age':26, 'Interests':['baseball','table tennis'],'amount_deposited':[24000,28000] }
    
}

def func_filter(a):
    if (str(a[key]['name']).lower().startswith('s')) or (str(a[key]['name']).lower().startswith('m')) or (str(a[key]['name']).lower().startswith('k')):  
        del a[key]
    
    return a

func_filter(my_dict)


def func_append(a):
    
    for key in a.keys():
        for i in range (97,123): 
            if i <=103: 
                if str(a[key]['name']).lower().startswith(chr(i)):
                    a[key]['name']="Mr. "+a[key]['name'] 
                    break

            if i>=104:
                if str(a[key]['name']).lower().startswith(chr(i)):
                    a[key]['name']="Ms." +a[key]['name'] 
    return a

 






# In[ ]:





# In[ ]:




