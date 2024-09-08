def start_game():
    print("You find yourself walking alone at night, and it begins to rain lightly.")
    print("You continue walking anyways, until you spot a strange lone figure standing still beside the lamppost ahead.")
    print("Will you 'walk' ahead or 'run' away?")

    choice = input("> ").lower()

    if choice == "walk":
        walk_ahead()
    elif choice == "run":
        print("You decide to run away, only to get run over by a truck. Unfortunately, this isn't an isekai genre.")
        play_again()
    else:
        print("Invalid choice! Try again.")
        start_game()

def walk_ahead():
    print("You decide to walk ahead. As you are about to walk past the stranger, they whisper your name.")
    print("Maomao, do you want to know your fortune?")
    print("Goosebumps rise on your skin. How come this stranger guessed your name correctly?")
    print("You stop and turn to the stranger.")
    print("Will you 'listen' or 'run'?")
    
    choice = input("> ").lower()
     
    if choice == "listen":
        listen()
    elif choice == "run":
        print("You ran away safely, but you lost sleep overthinking about your choices. Your performance at work dropped drastically, making your boss humiliate you for all to witness.")
        play_again()
    else:
        print("Invalid choice! Try again.")
        start_game()

def listen():
    print("You decided to listen.")
    print("The stranger utters, 'A wise choice. If you lend me your right palm, you will know your joys, if you lend me your left, you will know your sorrows. You can only pick one, which one would you want to know?'")
    print("What will you pick? Your 'right'  or your 'left'?")
    
    choice = input("> ").lower()
    
    if choice == "right":
        right()
    elif choice == "left":
        left()
    else:
        print("Invalid choice! Try again.")
        listen()

def right():
    print("You lend your right palm, and then the stranger reveals herself as a witch. Her eyes glows in wicked gold as she speaks, 'As promised, you will know your joys. You will ascend from the clutches of poverty, and you will be blessed. But there will come a time where you will be forced to make a decision.")
    print("Your heart glimmers with promises of riches. You decide to give your Mcdo happy meal to the witch.")
    print("The witch smiles in amusement and takes your Mcdo meal, 'You are free to go, child.'")
    print("You get home safe and sound. Hungry, but at least you're alive.")
    play_again()

def left():
    print("You lend your left palm, and the stranger reveals herself as a witch.")
    print("Her eyes glows in blood red, shadowy trails emanates from the corner of her eyes.")
    print("Fear overtakes you.")
    print("The wicked witch grips your left palm tight, and looks at you straight in the eyes.")
    print("'As promised, you will know your sorrows,' The witch sneers, 'And now I shall deliver the very cause of your sorrow!'")
    print("The trails from her eyes stretches like a shadowy whip, and cuts off your left hand.")
    print("You scream with pain and terror, watching your hand fall to the ground, as the cruel laughter of the witch fills your ears.")
    print("'What a foolish child. You are given the obvious choice, and this is how you choose your cards? Say goodbye to your hand, and to your MCDO meal!'")
    print("The witch forcibly takes your mcdo meal from your remaining hand, and walks away gleefully.")
    print("Due to bleeding and hunger, you are dead.")
    print("GAME OVER.")
    play_again()
    
def play_again():
    print("Do you want to play again? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice! Try again.")
        play_again()
        
if __name__ == "__main__":
    start_game()
    
    