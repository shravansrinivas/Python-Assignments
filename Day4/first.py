fo=open('BengaluruFC.png','rb')
f1=open('fcopy.jpg','wb+')
f2=open('..\\control.jpg','wb+')
for i in fo:
   for x in i:
      f1.write(i)

fo.close()
f1.close()
