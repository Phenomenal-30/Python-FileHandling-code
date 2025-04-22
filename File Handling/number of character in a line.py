import os
print(os.getcwd())
os.chdir(r'C:\Users\91884\Desktop')
f=open("test.txt",'r')
l=f.readlines()
a=l[0]
print("The number of character in first line is",len(a)-1)
