import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def choosing_a_villain():
    list_of_villains = ["troll", "gorgon", "dragon", "pirate"]
    return random.choice(list_of_villains)


def intro(villain_intro):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain_intro} is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In you hand you hold your trusty "
                "(but not very effective) dagger.")
    print_pause("\n")


def door_or_cave_options():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("\n")


def valid_input(prompt, options):
    while True:
        user_input = input(prompt)
        if user_input in options:
            return user_input


def restart_game():
    restart = valid_input("Would you like to play again (y/n) : ", ['y', 'n'])
    if (restart == 'n'):
        print_pause("Thanks for playing! See you next time.")
        return restart
    else:
        if(restart == 'y'):
            print_pause("Excellent! Restarting the game...")
            return restart


def fight(villain_to_be_fought, fighting_items):
    if ("Sword" not in fighting_items):
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "
                    f" {villain_to_be_fought}.")
        print_pause("You have been defeated!")
        print_pause("\n")
    else:
        print_pause("As the dragon moves to attack, "
                    "you unsheath youe new sword.")
        print_pause("The Sword of Ogoroth shines brightly in"
                    " you hand as you brace your self for the attack.")
        print_pause(f" But the {villain_to_be_fought} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the dragon. "
                    "You are victorious!")
        print_pause("\n")


def runaway(villain_to_runaway_from, items_during_runaway):
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")
    print_pause("\n")
    continue_the_game(villain_to_runaway_from, items_during_runaway)


def continue_the_game(Villain_in_continuation_of_game, Weapons_obtained):
    door_or_cave_options()
    knock_or_peer(Villain_in_continuation_of_game, Weapons_obtained)


def house(final_villain, sword_obtained):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when "
                f"the door opens and out steps a {final_villain}.")
    print_pause(f"Eep! This is the {final_villain}'s house!")
    print_pause(f"The {final_villain} attacks you!")
    if "Sword" not in sword_obtained:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    print_pause("\n")
    print_pause("Would you like to (1) fight or (2) runaway?")
    fight_or_runaway = input()
    if(fight_or_runaway == '1'):
        fight(final_villain, sword_obtained)
    else:
        if(fight_or_runaway == '2'):
            runaway(final_villain, sword_obtained)


def cave(items_obtained_in_cave):
    print_pause("You peer cautiously into the cave.")
    if "Sword" in items_obtained_in_cave:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        items_obtained_in_cave.append("Sword")
    print_pause("You walk back to the field.")
    print_pause("\n")
    door_or_cave_options()
    return items_obtained_in_cave


def knock_or_peer(Villain_of_the_Game, Items):
    door_or_cave = valid_input(" (Please enter 1 or 2)\n", ['1', '2'])
    if door_or_cave == '1':
        house(Villain_of_the_Game, Items)
    else:
        if door_or_cave == '2':
            cave(Items)
            knock_or_peer(Villain_of_the_Game, Items)


def adventure_game():
    villain = choosing_a_villain()
    intro(villain)
    door_or_cave_options()
    items = []
    knock_or_peer(villain, items)


def game():
    while True:
        adventure_game()
        restarting = restart_game()

        if restarting == 'n':
            break
    exit()


if __name__ == '__main__':
    game()
