import random
game=['rock','paper','scissors']
com=random.choice(game)
guss=input("choose between Rock,Papper or Scissors")
if com=='rock' and guss=='scissors':
    print("coputer win")
elif com=='rock' and guss=='paper':
    print("you win")
elif com=='paper' and guss=='scissors':
    print("you win")
if com=='rock' and guss=='rock':
    print("guss again")
elif com=='paper' and guss=='paper':
    print("guss again")
elif com=='scissors' and guss=='scissors':
    print("guss again")    