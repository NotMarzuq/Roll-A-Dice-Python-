import random    #In Class 110, you learned to create programs using built-in module time.

#In this project, you will use another built-in module ‘random’ to create a class dice simulator.

#Story:
#Your friends have gathered at your place after a long time to spend some fun time. You all decide to play a board game. 
# But you are unable to find a dice. You quickly use your coding skills to create a dice simulator and enjoy the board game 
# with your friends.
response = 'y'
while response == 'y':
    number = random.randint(1,6)
    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  O  ]")
        print("[     ]")
        print("[-----]")
    if number == 2:
        print("[-----]")
        print("[O    ]")
        print("[     ]")
        print("[    O]")
        print("[-----]")
    if number == 3:
        print("[-----]")
        print("[O    ]")
        print("[  O  ]")
        print("[    O]")
        print("[-----]")
    if number == 4:
        print("[-----]")
        print("[O   O]")
        print("[     ]")
        print("[O   O]")
        print("[-----]")
    if number == 5:
        print("[-----]")
        print("[O   O]")
        print("[  O  ]")
        print("[O   O]")
        print("[-----]")
    if number == 6:
        print("[-----]")
        print("[O   O]")
        print("[O   O]")
        print("[O   O]")
        print("[-----]")
    response = input('press y to roll again, n to exit: ')
    #print('\n')