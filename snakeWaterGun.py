import random as rd

a = "Snake"
b = "water"
c = "Gun"
computer_Point = 0
Player_Point = 0

def Game():
    global computer_Point
    global Player_Point
    while(True):
        list1 = [1, 2, 3]
        #computer = rd.randint(1, 3)
        computer=rd.choice(list1)
        print("######################### Welcome To SNAKE WATER GUN  Game ###########################")
        print("1. Snake\n2. Water\n3. Gun")
        player = int(input("Enter Yor choice: "))
        if player == 1:
            if player == 1 and computer == 1:
                print(f"Player choose {a} & computer choose {a} \nIt's Tie")

            elif player == 1 and computer == 2:
                print(f"player choose {a} & computer choose {b} \nYou Won The Match")
                Player_Point = Player_Point + 1

            else:
                print(f"player choose {a} & computer choose {c} \nYou lose the match")
                computer_Point = computer_Point + 1


        elif player == 2:
            if player == 2 and computer == 1:
                print(f"player choose {b} & computer choose {a}  \nYou Lose the match")

                computer_Point = computer_Point + 1

            elif player==2 and computer == 2:
                print(f"player choose {b} & computer choose {b}  \nIts Tie ")

            else:
                print(f"player choose {b} & computer choose {c}  \nYou Won The Match")
                Player_Point = Player_Point + 1

        elif player == 3:
            if player == 3 and computer == 1:
                print(f"player choose {c} & computer choose {a}  \nYou Won the match")
                Player_Point = Player_Point + 1

            elif player == 3 and computer == 2:
                print(f"player choose {c} & computer choose {b}  \nYou Lose The Match")
                computer_Point = computer_Point + 1

            else:
                print(f"player choose {c}  & computer choose {c}  \nIt's Tie")

        else:
            print("Invalid number You Typed")

        play = input("Do You want to play ? ")
        check=play.lower()
        if (check == 'n'):
            print("See you again")
            if Player_Point>computer_Point:
                print("You Won the Game")
            elif Player_Point < computer_Point:
                print("--You Lose the Game--")
            else:
                print("Its Tie Bro \n")
            print(f"Player point is {Player_Point}\ncomputer Point is {computer_Point}")
            break
        elif (check=='y'):
            Game()
        else:
            print("Invalid number ")
            break
Game()
