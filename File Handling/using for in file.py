import os
os.chdir(r'C:\Users\91884\Desktop')
f=open('test.txt','r')
data=f.readlines()
for line in data:
    word=line.split()
    print(word)
