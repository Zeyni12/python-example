Target=[{"Type":"men with weapon","capabilites":"high","potential damage":"high","strategic importance":"medium","distance":200},
       {"Type":"men without weapon","capabilites":"medium","potential damage":"low","strategic importance":"low","distance":300},
       {"Type":["religios place","women","dams","nuclear electricity"],"capabilites":"low","potential damage":"low","strategic importance":"low","distance":"none"},
       {"Type":"missiels","capabilites":"high","potential damage":"high","strategic importance":"high","distance":500},
       {"Type":"buildings","capabilites":"low","potential damage":"low","strategic importance":"high","distance":500}]


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
                  
       