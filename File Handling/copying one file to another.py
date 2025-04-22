import os
os.chdir(r'C:\Users\91884\Desktop')
f1=open("test.txt",'r')
f2=open("cslab",'w')
line=f1.read()
print(line)
f2.write(line)
f1.close()
f2.close()
