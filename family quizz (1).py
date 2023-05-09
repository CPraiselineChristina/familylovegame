#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello!, welcome family love test')
ans = input('are you ready to play (yes/no)')
score = 0
total_q = 5
if ans =='yes':
    ans = input('how much do you love your family?')
    if ans == 'very much':
        score +=1
        print('correct')
    else:
        print('incorrect')
        
    ans = input('whom you love very much?')
    if ans == 'parents':
        score +=1
        print('correct')
    else:
        print('incorrect')
        
    ans = input('what is the score you would like to give your parents?')
    if ans == 'cent%':
        score +=1
        print('correct')
    else:
        print('incorrect')
        
    ans = input('what is that you like in your family alot')
    if ans == 'generosity':
        score +=1
        print('correct')
    else:
        print('incorrect')
        
    ans = input('would you like to play further?')
    if ans == 'no':
        score +=1
        print('correct')
    else:
        print('incorrect')
        
print('thank you for takling the test', score, "questions correct")
mark =(score/total_q) * 100

print("mark: ", str(mark) + '%')

print('have a good day')
    
    
    
    
    


# In[ ]:





# In[ ]:




