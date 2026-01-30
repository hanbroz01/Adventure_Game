import time
import random


def text_color(message, color, background=False):   # text color
    soc = '\33[48;5;' if background else '\33[38;5;'
    eoc = '\033[0m'
    return f"{soc}{color}m{message}{eoc}"


def print_pause(message_to_print, delay=2):
    time.sleep(delay)
    print(message_to_print)


def special_items():  # Creates random item
    color = 50
    special_items = ["a book about paint drying", "an old toothbrush",
                     "some dirty socks"]
    item = random.choice(special_items)
    item_color = text_color(f"{item}", color)
    print_pause("You find yourself at the entrance of a magical forest.")
    print_pause(f"You only have {item_color} to defend yourself.")


def random_creature(items):  # Creats random creature
    color = 220
    random_creature = ["Fairy", "Goblin", "Gremlin", "Troll", "Frog"]
    creature = random.choice(random_creature)
    creature_color = text_color(f"{creature}", color)
    print_pause(f"You encounter a wild {creature_color}!")


def random_place(items):  # Creates random place
    random_place = ["abandoned house", "large tower", "old motel"]
    place = random.choice(random_place)
    print_pause(f"You see a mysterious {place}!")


def intro1():  # Intro to start game
    color = 10
    game_name = text_color("--> A KNIGHTS MISSION <--", color)
    print_pause(f"{game_name}")
    print_pause("A game not for the light hearted...")
    print_pause("Let's begin...")
    special_items()
    print_pause("On the other side of the forest a Queen needs rescuing.")
    print_pause("You need to get through the forest and save her in "
                "order to win the game.")


def intro2(items):
    color = 20
    choice1 = text_color("Enter 1 to cross the bridge.", color, True)
    choice2 = text_color("Enter 2 to climb the tree.  ", color, True)
    print_pause("You look and see what is around you.")
    print_pause("In front of you is a giant tree you could climb.")
    print_pause("To your left is an old bridge.")
    print_pause(f"{choice1}")
    print_pause(f"{choice2}")
    forest(items)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, I do not understand "{option}".')


def forest(items):
    time.sleep(2)
    answer = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    if answer == '1':
        cross_bridge(items)  # Player crosses bridge and encounters creature
    else:
        answer == '2'
        climb_tree(items)   # Player climbs tree and finds item


def cross_bridge(items):  # Crosses bridge encounters random creature
    color = 20
    choice1 = text_color("Enter 1 to look under the rock.", color, True)
    choice2 = text_color("Enter 2 to enter the swamp.    ", color, True)
    if "sword" in items:  # Player need a sword to defeat monster
        print_pause("You choose to cross the bridge...")
        random_creature(items)  # prints a random_creature
        print_pause("You are able to defeat it because you have the "
                    "Magic Sword!")
        print_pause("You cross the bridge and continue your mission.")
        print_pause("You now find yourself by an overgrown swamp.")
        print_pause("Do you enter the swamp or turn over that "
                    "interesting rock over there...")
        print_pause(f"{choice1}")
        print_pause(f"{choice2}")
        rock_or_swamp(items)  # Player proceeds in game
    else:
        print_pause("You choose to cross the bridge...")
        random_creature(items)  # prints a random_creature
        print_pause("You do not posses the Magic Sword that you "
                    " need to kill it!")
        print_pause("You are defeated and unable to continue your mission.")


def climb_tree(items):
    color = 20
    choice1 = text_color("Enter 1 to cross the bridge.    ", color, True)
    choice2 = text_color("Enter 2 to climb the tree again.", color, True)
    print_pause("You start to climb the tree...")
    if "sword" in items:  # Already found sword
        print_pause("You find nothing but enjoy the view.")
    else:
        print_pause("You find a Magic Sword!")
        items.append("sword")  # Collect sword
        print_pause("You collect the sword and place it in your bag.")
    print_pause("You head back to the forest entrance.")
    print_pause(f"{choice1}")
    print_pause(f"{choice2}")
    forest(items)


def rock_or_swamp(items):
    time.sleep(2)
    answer = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    if answer == '1':
        turn_over_rock(items)  # Player turns over rock and finds item
    else:
        answer == '2'
        enter_swamp(items)   # Enter swamp


def turn_over_rock(items):
    color = 20
    choice1 = text_color("Enter 1 to turn over the rock again.", color, True)
    choice2 = text_color("Enter 2 to enter the swamp.         ", color, True)
    print_pause("You turn the heavy rock over...")
    if "scissors" in items:
        print_pause("There is nothing under the rock except "
                    "some insects.")  # scissors already found
    else:
        print_pause("You find a pair of very sharp scissors!")
        items.append("scissors")  # Find scissors and collect
        print_pause("You wonder if they will come in handy...")
    print_pause("You head back to the swamp.")
    print_pause(f"{choice1}")
    print_pause(f"{choice2}")
    rock_or_swamp(items)  # Back to swamp


def enter_swamp(items):
    print_pause("You enter the swamp...")
    print_pause("All of a sudden you are over come by wild vines!")
    if "scissors" in items:  # Can only pass with scissors
        print_pause("You use your scissors to cut yourself free!")
        print_pause("You manage to get out of the swamp safely.")
        print_pause("Your relief is short lived as you notice "
                    "something up ahead...")
        fight(items)
    elif "scissors" not in items:  # Player loses
        print_pause("Oh no! You have nothing to cut yourself free with!")
        print_pause("The vines take over and you are dragged into the swamp.")
        print_pause("You are defeated and are unable to complete your "
                    "mission.")


def fight(items):  # Player fights random enemy
    color = random.choice([10, 20, 30])
    weapons = ["rock", "baseball bat", "rusty hammer", "camping chair"]
    enemies = ["Mermaid", "rabbit", "giant black bear", "giant pigeon"]
    rand_weapon = random.choice(weapons)
    rand_enemy = random.choice(enemies)
    rand_weapon_color = text_color(f"{rand_weapon}", color)
    rand_enemy_color = text_color(f"{rand_enemy}", color)
    print_pause(f"It's a {rand_enemy_color}!")
    print_pause("It battles you to a duel!")
    print_pause("You look around to see what you can use...")
    print_pause(f"You notice a {rand_weapon_color} and pick it up!")
    print_pause("You raise your weapon and...")
    if weapons.index(rand_weapon) > enemies.index(rand_enemy):
        color = 20
        choice1 = text_color("Enter 1 to talk to the Wizard.", color, True)
        choice2 = text_color("Enter 2 continue walking.     ", color, True)
        print_pause(f"You succesfully use your {rand_weapon_color} to defeat")
        print_pause(f"the {rand_enemy_color}!", 0)
        print_pause("You brush yourself off and look up ahead...")
        random_place(items)
        print_pause("You walk towards it not knowing what will happen...")
        print_pause("Before you reach the mysterious place up ahead, "
                    "you notice something...")
        print_pause("A Wizard!")
        print_pause(f"{choice1}")
        print_pause(f"{choice2}")
        last_item_search(items)  # Player moves to next step
    else:
        print_pause(f"Your {rand_weapon_color} was not strong enough to")
        print_pause(f"defeat the {rand_enemy_color}!", 0)


def last_item_search(items):
    time.sleep(2)
    answer = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    if answer == '1':
        wizard(items)  # Player talks to wizard and recieves final item
    else:
        answer == '2'
        final_chapter(items)   # last creature - need dagger to win


def wizard(items):
    color = 20
    choice1 = text_color("Enter 1 to talk to the Wizzard again.", color, True)
    choice2 = text_color("Enter 2 to continue walking.         ", color, True)
    print_pause("The Wizzard points to the table beside them...")
    if "dagger" in items:  # If dagger already collected
        print_pause("The table is empty. You already took the dagger.")
    else:
        print_pause("You see a dagger and think to yourself why "
                    "you would need that...")
        print_pause("You take the dagger anyway.")
        items.append("dagger")  # Collect dagger
    print_pause("You head back to the mysterious place you saw before.")
    print_pause(f"{choice1}")
    print_pause(f"{choice2}")
    last_item_search(items)  # talk to Wizzard again or enter swamp


def final_chapter(items):
    print_pause("You approach the mysterious place...")
    random_creature(items)
    if "dagger" in items:  # Need dagger to win
        print_pause("You use your dagger to defeat the wild creature!")
        print_pause("After killing the creature you proceed to enter "
                    "the mysterious building.")
        almost_there(items)
    elif "dagger" not in items:
        print_pause("Oh no! You do not posses the magic dagger!")
        print_pause("You are defeated by the wild creature and can not "
                    "complete your mission.")


def almost_there(items):
    print_pause("Before you is a stairwell and you hear the Queen "
                "at the top!", 1)
    print_pause("Before you can run up the stairs...", 1)
    random_creature(items)
    print_pause("The creature is blocking your path!", 1)
    print_pause("It says you need to play a game in order to pass.", 1)
    print_pause("Guess what number I am thinking of and I shall let you pass "
                "says the creature...")
    chance(items)


def chance(items):
    creature = random.randint(1, 10)  # creature picks number
    print_pause("Choose wisely, you only have 6 guesses...")
    guess = 0
    while guess < 6:
        try:
            time.sleep(2)
            user = int(input("Pick a whole number between 1 and 10.\n"))
            if creature == user:  # user wins
                guess = 6
                print("The number was %d!" % creature)
                print_pause("The creature steps aside and you run up the "
                            "stairs.")
                print_pause("Congratulations! You save the Queen and "
                            "complete your mission!")

            elif creature > user:  # User has to guess again
                guess += 1
                print_pause("Your guess is too small")
                if guess == 6:  # Player looses if trys are up
                    print_pause("The number was %d!" % creature)
                    print_pause("You failed to guess correctly meaning "
                                "you have failed your mission!")
            elif creature < user:  # User has to guess again
                guess += 1
                print_pause("Your guess is too big")
                if guess == 6:  # Player looses if trys are up
                    print_pause("The number was %d!" % creature)
                    print_pause("You failed to guess correctly meaning "
                                "you have failed your mission!")
        except ValueError:  # stops user putting in letters as answer
            print_pause("I dont understand. Try again.")


def end():
    print_pause("Better luck next time...if you're "
                "brave enough to try again that is...")


def play():
    items = []
    intro1()
    intro2(items)


def play_again():
    color = 160
    text_red = text_color("-->GAME OVER--<", color)
    print_pause(f"{text_red}")
    time.sleep(2)
    return valid_input("Play again? Yes or No\n", ["yes", "no"])


def game():
    while True:
        play()
        if play_again() == 'no':
            break
    end()


if __name__ == '__main__':
    game()
