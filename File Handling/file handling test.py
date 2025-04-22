import os
print(os.getcwd())
os.chdir(r'C:\Users\91884\Desktop')
f=open("test.txt",'r')
#a1=f.read()
#a2=f.read(20) (read the test file upto 20 character NOTE:-After f.read() the curser will be at end
#a3=f.readline() #(read only one line)
#a4=f.readline() #(read second line)
#print(a1)
#print(a2)
#print(a3)
#print(a4)
a5=f.readlines() #(converts all the the lines into list
print(a5)
f.close()

