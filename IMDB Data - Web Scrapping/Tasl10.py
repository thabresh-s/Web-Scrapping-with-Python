import json
import numbers
with open ('task5.json','r') as f:
    j=json.load(f)
sub={"english:2"}
num={}
i=0
a=0
b=0
ch=0
while  i<len(j):
    if j[i]['director']=='madhavan':
        if j[i]['language']=='English':
           a=a+1
           sub['english']=a
    num['madhavan']=sub
             
    if j[i]['director']=='sundar':
        if j[i]['language']=='engish':
            num['sundar']=sub
            b=b+1
            sub['english']=b
    num['sundar']=sub
        
    if j[i]['director']=='mani ratnam':
        if j[i]['language']=='english':
            ch=ch+1
            sub['english']=ch
    num['mani ratnam']=sub
    i=i+1
    
        
print(num)