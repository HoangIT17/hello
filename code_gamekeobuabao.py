    #rock,paper,scissors game by python
import random
while True:    
    choices=['rock','paper','scissors']
    robot=random.choice(choices)
    player=None

    while player not in choices:
        player=input("Player choice rock/paper/scissors: ").lower()
        
    if player==robot:
        print("Player_Choice:",player)
        print("Robot_Choice:",robot)
        print("Tie  (¬_¬”")
    elif player=='rock':
        if robot=='paper':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player lose (!__!)")
        if robot=='scissors':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player winers  *(^O^)*")
    elif player=='paper':
        if robot=='scissors':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player lose  (!__!)")
        if robot=='rock':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player winers  *(^O^)*")
    elif player=='scissors':
        if robot=='rock':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player lose  (!__!)")
        if robot=='paper':
            print("Player_Choice:",player)
            print("Robot_Choice:",robot)
            print("Player winers  *(^O^)*")
    play_again=input("Do you want to play again?(y/n): ").lower()
    if play_again!='y':
        break
print("Thanks for playing!")

        


            









