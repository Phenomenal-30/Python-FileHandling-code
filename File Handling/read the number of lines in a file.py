import os
print(os.getcwd())
os.chdir(r'C:\Users\91884\Desktop')
f=open("test.txt",'r')
a=f.readlines()
#l=0
#for i in a:
#    l+=1
l=len(a)
print('The number of lines is',l)
