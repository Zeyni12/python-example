import random

w=['weapon1','weapon2','weapon3','weapon4','weapon5']
t=['target1','target2','target3','target4','target5']

random.shuffle(w)
random.shuffle(t)

for i in range(5):
    print(w[i]+' '+'assigned to'+' '+t[i])
    i=i+1