##import os
##os.chdir(r'C:\Users\91884\Desktop')
##f=open("test.txt",'a') #Don't overwrites it start just after the curser has left
##f.write('\nNow the new game begins')
##f.close()
##f=open('test.txt','r')
##a=f.read()
##print(a)
##f.close()

import os
os.chdir(r'C:\Users\91884\Desktop')
f=open("test.txt",'a')
lst=['34','23r','wda','efe']
f.writelines(lst)
f.close()

import os
os.chdir(r'C:\Users\91884\Desktop')
f=open('test.txt','r')
a=f.read()
print(a)
f.close()
         
