import re,os
files=os.listdir("C:\\Users\\ssrinivas35\\Desktop\\New folder")

for file in files:
    if file.endswith(".log"):
        fo=open("C:\\Users\\ssrinivas35\\Desktop\\New folder\\"+file,'rb')
        for f in fo:
            
            matches=re.findall('^[a-zA-Z0-9]*[@][a-zA-Z0-9]*[.][a-zA-Z0-9]*',f.decode())
            if len(matches)!=0:
                for match in matches:
                    print(match)