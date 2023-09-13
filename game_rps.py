import random
option=[1,2,3]
randomoption=random.choice(option)
counter=0
#getting input

for i in range(1,11):
    #getting input
    userinput=(input("enter the option r for 'Rock', p for 'Paper' and s for 'Sicssor'"))
    if userinput == 'r' or userinput =='R':
        userinput=1
    elif userinput == 'p' or userinput =='P':
        userinput=2
    else:
        userinput=3

    print(userinput)
    print(randomoption)
    if userinput==1:
        if userinput == randomoption:
            print("it's a DRAW you choose 'Rock' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput<randomoption:
            print("you LOST you choose 'Rock' and Computer Choose 'Paper', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput>randomoption:
            print("you WON you choose 'Rock' and Computer Choose 'Sicssor', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        
    elif userinput == 2:
        if userinput == randomoption:
            print("it's a DRAW you choose 'Paper' and Computer Choose 'Paper', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput<randomoption:
            print("you LOST you choose 'Paper' and Computer Choose 'Sicssor', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput>randomoption:
            print("you WON you choose 'Paper' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        
    else:
        if userinput == randomoption:
            print("it's a DRAW you choose 'Sicssor' and Computer Choose 'Sicssor', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput==3 and randomoption==2:
            print("you WON you choose 'Sicssor' and Computer Choose 'Sicssor', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        elif userinput>randomoption:
            print("you LOST you choose 'Sicssor' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
            counter=counter+1
            
        
    
print("You Won = ",counter)
computerwins=counter-10
print("Computer Won = ",computerwins)

if counter > computerwins:
    print("THEN.....\n You're the Overall  Winner")
else:
    print("THEN.....\n Computer is the Overall Winner")





