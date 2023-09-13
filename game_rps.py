import random
option=[1,2,3]
randomoption=random.choice(option)


for i in range(1,11):
    #getting input
    userinput=(input("enter the option r for 'Rock', p for 'Paper' and s for 'Scissor'"))
    if userinput == 'r' or userinput =='R':
        userinput=1
    elif userinput == 'p' or userinput =='P':
        userinput=2
    else:
        userinput=3

    if userinput==1:
        if userinput == randomoption:
            print("it's a DRAW \nyou choose 'Rock' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
           
            
        elif userinput<randomoption:
            print("you LOST \nyou choose 'Rock' and Computer Choose 'Paper', The remaining Chances are = ",i if i == 0 else 10 - i)
         
            
        elif userinput>randomoption:
            print("you WON \nyou choose 'Rock' and Computer Choose 'Scissor', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            
        
    elif userinput == 2:
        if userinput == randomoption:
            print("it's a DRAW \nyou choose 'Paper' and Computer Choose 'Paper', The remaining Chances are = ",i if i == 0 else 10 - i)
           
            
        elif userinput<randomoption:
            print("you LOST \nyou choose 'Paper' and Computer Choose 'Scissor', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            
        elif userinput>randomoption:
            print("you WON \nyou choose 'Paper' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            
        
    else:
        if userinput == randomoption:
            print("it's a DRAW \nyou choose 'Scissor' and Computer Choose 'Scissor', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            
        elif userinput==3 and randomoption==2:
            print("you WON \nyou choose 'Scissor' and Computer Choose 'Paper', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            
        elif userinput>randomoption:
            print("you LOST \nyou choose 'Sicssor' and Computer Choose 'Rock', The remaining Chances are = ",i if i == 0 else 10 - i)
            
            






