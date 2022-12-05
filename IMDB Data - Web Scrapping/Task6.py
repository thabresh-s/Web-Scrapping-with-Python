import json
with open('task5.json','r') as f:
    j=json.load(f)
    sub={}
    i=0
    num=0
    while i<len(j):
        if j[i]['language']=='English':
            num+=1
        i+=1
        sub['English']=num
    with open('task6.json','w') as f:
        json.dump(sub,f)