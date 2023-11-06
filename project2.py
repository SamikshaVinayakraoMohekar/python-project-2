import random
l=['Rock','Scissor','Paper']

while True:
    u_Choice=int(input("Enter you choice: "))
    print('''
1:YES
2:NO- End Game.
        ''')
    if u_Choice==1:
        u_input=input("Enter your input: ")
        print('''
1: Rock
2: Scissor
3: Paper
''')
    else:
        break