import random
import time


def description_delay(message, wait_time):
    print(message)
    time.sleep(wait_time)


# def action(weapon):



def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            description_delay("Thanks for playing! See you next time.", 2)
            return 'off'
        elif choice == 'y':
            description_delay("Nice! Restart in progress ...", 2)
            return 'on'

def chase_down():
    description_delay(f"You chase the {badPerson} for over 70 metres", 2)
    description_delay(f"Catching up to the {badPerson}, he attacks you trying to hit you with his fist", 2)
    description_delay(f"You dodge the incoming fist, leaving the {badPerson} open", 2)
    description_delay("You seeing the opening, give him a hard blow to the chest, then knocked him down with a Mike Tyson level kind of uppercut, afterward pinning him down", 2)
    description_delay(f"You then grab the purse from the {badPerson}", 2)
    description_delay("And returned it to the young woman", 2)
    description_delay(f"The young woman being glad you saved her from the {badPerson}, and from potential loss of very crucial company documents", 2)
    description_delay("And as a token of appreciation, she invites you to dinner, which you accepted after she insisted and won't let go", 2)
    description_delay("Following your heroics, you have mad a new friend, and your reputation in the neigbourhood has improved, and now popularly called HERO in the neighbourhood", 2)
    description_delay("YAY!!!", 3)

def walk_away():
    description_delay("You walked away from the whole situation", 2)
    description_delay("Causing the young woman to lose her purse and vital items", 2)
    description_delay("GAME OVER", 3)

def start():
    description_delay("On your way from work around 5:00pm", 2)
    description_delay(f"You see a young woman being harassed by a {badPerson}", 2)
    description_delay(f"You see the {badPerson} getting away with the young woman's purse", 2)
    description_delay("You have the choice to either prevent the woman from getting mugged", 2)



def what_to_do():
    description_delay("", 1)
    description_delay(f"Enter 1 chase down the {badPerson}", 2)
    description_delay("Enter 2 to walk away from the situation", 2)
    description_delay("What will you do?", 2)
    option = ''
    while option not in ['1', '2']:
        option = input("(Please enter 1 or 2.)\n")
    if option == '1':
        chase_down()
    elif option == '2':
        walk_away()




game_status = 'on'
while game_status == 'on':

    badPersons = ['thief', 'thug']
    badPerson = random.choice(badPersons)

    start()
    what_to_do()

    game_status = play_again()