#!/usr/bin/env python
# coding: utf-8

# #### <font color=red> Read / Write text file </font>
# ##### The following code reads each line of cheat sheet and remove the unnecessary lines 
# ##### http://www.newthinktank.com/2014/08/mysql-video-tutorial/

# In[16]:


sql =open('C:/Users/fshok/Documents/SQL/CommandLineTutorials.txt', 'r')
nsql=open('C:/Users/fshok/Documents/SQL/CommandLineTutorialsNew.txt', 'w')

i=1
for line in sql:
    if line==str(i).zfill(3)+'\n': 
        i+=1
        continue
    elif line=='\n':
        continue
    nsql.write(line)

sql.close()
nsql.close()


# In[ ]:




