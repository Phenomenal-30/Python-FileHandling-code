import os
f=open('hello.txt','w') #Create a new file hello if not existed
f.write('This is a new file')
f.write('\nGood morning')
f.close()

f=open('hello.txt','r')
a=f.read()
print('Content is:',a)
f.close()
