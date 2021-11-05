# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:16:38 2021
"""
# Python Snack Water, Gun Game Coding

import random

def gamewin(comp, you):
    if comp == you:
        return None
    
    if comp == 's':
        if you == 'w':
            return False
        
        elif you == 'g':
            return True
        
    elif comp == 'w':
        if you == 'g':
             return False
         
        elif you == 's':
            return True
    
    elif comp == 'g':
        if you == 's':
             return False
         
        elif you == 'w':
            return True
        

print("Computer's Turn: Select your choice")

randomNo = random.randint(1, 3)
if randomNo ==1:
    comp = 's'
    
elif randomNo == 2:
    comp = 'w'
    
elif randomNo == 3:
    comp = 'g'
    
    


you = input("Players Turn: Select your choice Snacks(s) Water(w) Gun(g)? ")

print(f"Computer Selected: {comp}")
print(f"You have selected: {you}")

result= gamewin(comp, you)

if result == None:
    print('Game is Tie')

elif result:
    
    print('boobs ')
    
else:
    print('you Won!')
    






