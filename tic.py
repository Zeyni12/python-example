import random

number=[1,2,3,4,5,6,7,8,9]
gameboard=[[1,2,3],[4,5,6],[7,8,9]]

def gameeboard():
    for i in range(3):
        for j in range(3):
            print("",gameboard[i][j],end=" |")
        print("\n")
gameeboard() 

def modifyarray(num,turn):
    num -= 1
    if(num==1):
        gameboard[0][0]=turn 
    if(num==2):
        gameboard[0][1]=turn  
    if(num==3):
        gameboard[0][2]=turn  
    if(num==4):
        gameboard[1][0]=turn  
    if(num==5):
        gameboard[1][1]=turn  
    if(num==6):
        gameboard[1][2]=turn  
    if(num==7):
        gameboard[2][0]=turn  
    if(num==8):
        gameboard[2][1]=turn  
    if(num==9):
        gameboard[2][2]=turn  
def gamewinner(gameeboard):
    #x axsis
    if (gameboard[0][0]=='x'and gameboard[0][1]=='x'and gameboard[0][2]=='x'):
        print("x win")
        return 'x'
    elif (gameboard[1][0]=='x'and gameboard[1][1]=='x'and gameboard[1][2]=='x'):
        print("x win")
        return 'x'
    elif (gameboard[2][0]=='x'and gameboard[2][1]=='x'and gameboard[2][2]=='x'):
        print("x win")
        return 'x'
    
    elif (gameboard[0][0]=='o'and gameboard[0][1]=='o'and gameboard[0][2]=='o'):
        print("o win")
        return 'o'
    elif (gameboard[1][0]=='o'and gameboard[1][1]=='o'and gameboard[1][2]=='o'):
        print("o win")
        return 'o'
    elif (gameboard[2][0]=='o'and gameboard[2][1]=='o'and gameboard[2][2]=='o'):
        print("o win")
        return 'o'
    #y axsis
    elif (gameboard[0][0]=='x'and gameboard[1][0]=='x'and gameboard[2][0]=='x'):
        print("x win")
        return 'x'
    elif (gameboard[0][1]=='x'and gameboard[1][1]=='x'and gameboard[2][1]=='x'):
        print("x win")
        return 'x'
    elif (gameboard[2][0]=='x'and gameboard[2][1]=='x'and gameboard[2][2]=='x'):
        print("x win")
        return 'x'
    
    elif (gameboard[0][0]=='o'and gameboard[1][0]=='o'and gameboard[2][0]=='o'):
        print("o win")
        return 'o'
    elif (gameboard[0][1]=='o'and gameboard[1][1]=='o'and gameboard[2][1]=='o'):
        print("o win")
        return 'o'
    elif (gameboard[2][0]=='o'and gameboard[2][1]=='o'and gameboard[2][2]=='o'):
        print("o win")
        return 'o'
    #cross check
    elif (gameboard[0][0]=='x'and gameboard[1][1]=='x'and gameboard[2][2]=='x'):
        print("x win")
        return 'x'
    elif (gameboard[0][2]=='x'and gameboard[1][1]=='x'and gameboard[2][0]=='x'):
        print("x win")
        return 'x' 

    elif (gameboard[0][0]=='o'and gameboard[1][1]=='o'and gameboard[2][2]=='o'):
        print("o win")
        return 'o'
    elif (gameboard[0][2]=='o'and gameboard[1][1]=='o'and gameboard[2][0]=='o'):
        print("o win")
        return 'o'
    else:
        return 'c'                                           

leave=False 
counter=0

while(leave==False):
    if(counter%2==1):
        gameeboard()
        nopic=int(input("input 1-9: "))
        if(nopic >=1 and nopic <10):
            modifyarray(nopic,'x')
            number.remove(nopic)
        else:
             print("invalid input. please try again.")
        counter += 1
  
    else:
        while(True): 
         copic=random.choice(number)
         print("\ncpu choice: ", copic)
         if(copic in number):
            modifyarray(copic,'o')
            number.remove(copic)
            counter += 1
            break    
        gameState = gamewinner(gameeboard)
        if(gameState!='c'):
            break  
