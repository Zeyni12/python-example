weapon=[{'Type':'bred_safat machine gun','range':730,'accuracy':800,'Lethality':'medium'},
        {'Type':'lewis gun','range':800,'accuracy':600,'Lethality':'medium'},
        {'Type':'spandu  machine gun','range':1200,'accuracy':890,'Lethality':'medium'},
        {'Type':'vickers machine gun','range':4000,'accuracy':600,'Lethality':'high'},
        {'Type':'blue danube (nuclear weapon) gun','range':550000,'accuracy':400,'Lethality':'high'}]

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