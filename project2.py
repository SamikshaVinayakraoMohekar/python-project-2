import random
li=['Rock','Scissor','Paper']

while True:
    usr_Count=0
    Com_Count=0
    print("Choices: ")
    print("1:YES\n2:NO")

    u_Choice=int(input("Enter you choice: "))
    if u_Choice==1:
        for a in range(1,6):
            
            print("1:Rock\n2:Scissor\n3:Paper")

            u_Input=int(input("Enter your choice from above: "))
            if u_Input==1:
                u_Choice='Rock'
            elif u_Input==2:
                u_Choice='Scissor'
            elif u_Input==3:
                u_Choice='Paper'
            C_Choice=random.choice(li)


            if u_Choice==C_Choice:
                print("Game is Draw..")
                print("User Choice: ",u_Choice)
                print("Computer Choice: ",C_Choice)
                usr_Count+=1
                Com_Count+=1
            elif (u_Choice=='Rock'and C_Choice=='Scissor') or (u_Choice=='Scissor'and               C_Choice=='Paper') or (u_Choice=='Paper'and C_Choice=='Rock'):
                print("User Choice: ",u_Choice)
                print("Computer Choice: ",C_Choice)
                usr_Count+=1
                print("You Win")
            else:
                print("User Choice: ",u_Choice)
                print("Computer Choice: ",C_Choice)
                Com_Count+=1
                print("Computer Win")
            print( )
        
        
        print( )
        if Com_Count==usr_Count:
            print("User Score: ",usr_Count)
            print("Computer Score: ",Com_Count)
            print("Finally Game is Draw")
        elif Com_Count>usr_Count:
            print("User Score: ",usr_Count)
            print("Computer Score: ",Com_Count)
            print("Finally Computer is Win")
        else:
            print("User Score: ",usr_Count)
            print("Computer Score: ",Com_Count)
            print("Finally User is Win")

    else:
        break