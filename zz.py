import random

def guss(x):
    random_no=random.randint(1,x)
    guss_no=0
    while random_no!=guss_no:
        guss_no=int(input("guss number:"))
        if guss_no<random_no:
            print("low guss again")
        elif guss_no>random_no:
            print("to high guss again")
    print(f"cogra you guss correct {random_no}")    

guss(10)
                    
    