import random;
import time;

def description(text, delay):
    print(text)
    time.sleep(delay)


#   PLAY AGAIN....

def close_game():
    description("Are you sure you want to close the game?", 3)
    close = ''
    while close not in ['Y', 'N']:
        close = input("Y to proceed, N to cancel")
        if close == 'Y':    
            description("Game closed successfuly...", 2)
            return "game_closed"
        elif close == 'N':
            return "on"

def adventure():
    print("The adventure game")

#   COIN_FLIP MAIN....
def coin_flip():
    coin = ["HEAD", "TAIL"]
    flip = random.choice(coin)
    return flip

#   DIE_ROLL MAIN
def die_roll():
    number = ['1', '2', '3', '4', '5', '6']
    randomNumber = random.choice(number)
    return randomNumber

#   COIN_FLIP   ----    HEAD WINS, TAIL LOSES....
def win_lose():
    description("Welcome to HEAD WINS TAIL LOSES", 3)
    description("You are about to enter a new game", 2)
    description("Enter Y for yes to proceed, or N for no to return to the main menu", 1)
    user_response = ''
    while user_response not in ['Y', 'N']:
        user_response = input("Proceed? Y/N:")
    if user_response == 'Y':
        res = coin_flip()
        if res == "HEAD":
            print("Yay!, you won this round")
        elif res == "TAIL":
            print("Whoops, better luck next time")
    elif user_response == 'N':
        description("Do you want to return to the main menu or close the game?", 3)
        rtm = ''
        while rtm not in ['1', '2']:
            rtm = input("Enter 1 to return to the main menu or 2 to close the game")
        if rtm == '1':
            start()
        elif rtm == '2':
            close_game()




#   COIN_FLIP   ----    PREDICT THE OUTCOME....
def predict_the_outcome():
    res = coin_flip()
    prediction = ''
    while prediction not in ['HEAD', 'TAIL']:
        prediction = input("Please type HEAD or TAIL (in caps) to predict:")
    if prediction == res:
        print("Yeah, you got it")
    else:
        print("Oops!, you got it wrong")
    print('You predicted',prediction, 'and got', res)

#   DIE_ROLL    ----    PREDICT THE OUTCOME....
def justice():
    res = die_roll()
    prediction = ''
    while prediction not in ['1', '2', '3', '4', '5', '6']:
        prediction = input("Please enter between 1 nad 6 to predict the outcome:")
    if prediction == res:
        print("Yeah, you got it")
    else:
        print("Oops!, you got it wrong")
    print('You predicted',prediction, 'and got', res)

def start():
    name = input("Please enter your name:")
    print("Welcome", name)
    description("There are various games and adventure waiting for you", 2)
    description("Enter 1 to play, THE ADVENTURE OF CONAN game", 1)
    description("Enter 2 to play, HEAD WINS TAIL LOSES", 2)
    description("Enter 3 to play, PREDICT THE COIN TOSS", 2)
    description("Enter 4 to play, PREDICT THE DIE ROLL", 2)
    user_response = ''
    while user_response not in ['1', '2', '3', '4']:
        user_response = input("Please select a game mode by entering the corresponding numbers")
    if user_response == '1':
        adventure()
    elif user_response == '2':
        win_lose()
    elif user_response == '3':
        predict_the_outcome()
    elif user_response == '4':
        justice()


game_status = 'on'

while game_status == 'on':
    start()
    game_status = close_game()