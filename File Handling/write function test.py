import os
os.chdir(r'C:\Users\91884\Desktop')
f=open("test.txt",'w') #Remove the old data and overwrites it
f.write("New lines are now adding")
f.close()

f=open("test.txt",'r')
a=f.read()
print("Content is:",a)
f.close()
