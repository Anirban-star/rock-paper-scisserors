import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='R':
     if you=='p': 
         return True
    elif you=='S':
     return False
    elif comp=='P':
     if you=='R':
         return False
    elif  you =='S':
     return True
    elif comp=='S':
     if you=='P':
            return False
    elif you =='R':
            return True
    return False
    print("compturn:Rock(R) PAPER(P) SCISSORS(S)?")
randNo = random.randint(1, 3) 
if randNo == 1:
 comp='R' 
elif randNo==2:
 comp='P'
elif randNo==3:
 comp ='S'
you = input("Rock(R) PAPER(P) SCISSORS(S)?")
a = gamewin(comp,you)
print(f"Copmputer chose {comp}")
print(f"you chose {you}")
if a==None:
      print("The game is tie")
elif a:
     print("you win")
else:
     print ("you lose")   

