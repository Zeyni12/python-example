Target=[{"Type":"men with weapon","capabilites":"high","potential damage":"high","strategic importance":"medium","distance":200},
       {"Type":"men without weapon","capabilites":"medium","potential damage":"low","strategic importance":"low","distance":300},
       {"Type":["religios place","women","dams","nuclear electricity"],"capabilites":"low","potential damage":"low","strategic importance":"low","distance":"none"},
       {"Type":"missiels","capabilites":"high","potential damage":"high","strategic importance":"high","distance":500},
       {"Type":"buildings","capabilites":"low","potential damage":"low","strategic importance":"high","distance":500}] 

weapon=[{'Type':'bred_safat machine gun','range':730,'accuracy':800,'Lethality':'medium'},
        {'Type':'lewis gun','range':800,'accuracy':600,'Lethality':'medium'},
        {'Type':'spandu  machine gun','range':1200,'accuracy':890,'Lethality':'medium'},
        {'Type':'vickers machine gun','range':4000,'accuracy':600,'Lethality':'high'},
        {'Type':'blue danube (nuclear weapon) gun','range':550000,'accuracy':400,'Lethality':'high'}]


for i in range(len(Target)):
    if Target[i]['capabilites']=='high' and Target[i]['potential damage']=='high' and Target[i]['strategic importance']=='high' and Target[i]['distance']<=500:
        print(Target[i]['Type'],' priority 1')
    elif Target[i]['capabilites']=='high' and Target[i]['potential damage']=='high' and Target[i]['strategic importance']=='medium' and Target[i]['distance']<=500:
        print(Target[i]['Type'],' priority 2')
    elif Target[i]['capabilites']=='high' and Target[i]['potential damage']=='medium' and Target[i]['strategic importance']=='high' and Target[i]['distance']<=500:
        print(Target[i]['Type'],' priority 3')
    elif Target[i]['capabilites']=='low' and Target[i]['potential damage']=='low' and Target[i]['strategic importance']=='low' and Target[i]['distance']=='none':
        print(Target[i]['Type'],' Protected Assets')
    elif Target[i]['capabilites']=='low' and Target[i]['potential damage']=='low' and Target[i]['strategic importance']=='high' and Target[i]['distance']<=500:
        print(Target[i]['Type'],' priority 4')
    elif Target[i]['capabilites']=='medium' and Target[i]['potential damage']=='low' and Target[i]['strategic importance']=='low' and Target[i]['distance']<=500:
        print(Target[i]['Type'],' priority 5')               
    i=i+1    
                  


print('Based on Range')

for i in range(len(weapon)):
    if weapon[i]['range']==550000:
        print(weapon[i]['Type'],' Assigned to priority 1') 
    if weapon[i]['range']==4000:
        print(weapon[i]['Type'],' Assigned to priority 2')  
    if weapon[i]['range']==1200:
        print(weapon[i]['Type'],' Assigned to priority 3') 
    if weapon[i]['range']<=800:
        print(weapon[i]['Type'],' Assigned to priority 4')     

print('BASED ON ACCURACY')

for i in range(len(weapon)):
    if weapon[i]['accuracy']==1200:
        print(weapon[i]['Type'],' Assigned to priority 1') 
    if weapon[i]['accuracy']==890:
        print(weapon[i]['Type'],' Assigned to priority 2')  
    if weapon[i]['accuracy']==600:
        print(weapon[i]['Type'],' Assigned to priority 3') 
    if weapon[i]['accuracy']<=400:
        print(weapon[i]['Type'],' Assigned to priority 4')  

print('BASED ON LETHALITHY')  

for i in range(len(weapon)):
     if weapon[i]['accuracy']=='high':
        print(weapon[i]['Type'],' Assigned to priority 1') 
     if weapon[i]['Lethality']=='high':
        print(weapon[i]['Type'],' Assigned to priority 2')  
     if weapon[i]['Lethality']=='medium':
        print(weapon[i]['Type'],' Assigned to priority 3') 
     if weapon[i]['Lethality']=='medium':
        print(weapon[i]['Type'],' Assigned to priority 4')         