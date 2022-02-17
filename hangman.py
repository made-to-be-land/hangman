from art import tprint
from random_words import RandomWords
from simple_term_menu import TerminalMenu
import string
import sys
import os
import time



def rules():
    os.system('clear')
    print("Rules:\nWhenever a player guesses a letter correctly, he or she receives the opportunity to try guessing "
          "the entire word puzzle. For this guess to be successful, the player must guess all the missing letters, "
          "and the guess may not include any extra letters. If the guess fails to meet any of these conditions, "
          "it counts towards the limit of 10 wrong guesses - you should only make a guess if you are reasonably sure."
          "You have one hint but its tricky one!")
    agree = ["yes", "no"]
    terminal_menu = TerminalMenu(agree, title="Are you agree?")
    menu_entry_index = terminal_menu.show()
    if agree[menu_entry_index] == "yes":
        pass
    else:
        sys.exit()

def multiplayer(alphabet_string):
    os.system("clear")
    print("Select what type of game you choice?")
    multi = ["yes", "no"]
    terminal_menu = TerminalMenu(multi, title="Do you want to play multiplayer?")
    menu_entry_index = terminal_menu.show()
    if multi[menu_entry_index] == "yes":
        random_word = players(alphabet_string)
    else:
        random_word = get_random()
    return random_word.lower()

def players(alphabet_string):
    random_word = input("Your word is?\n")
    while not random_word.isalpha():
        random_word = input("Your word is?")
    return random_word

def grafik(lifes):
    os.system('clear')
    print("\033[32m")
    tprint('H A N G M A N')
    print("\033[0m")

    print("\033[36m********************************************************************************")
    print("*------------------------------------------------------------------------------*")
    print("*|                                                                            |*")
    print("*|                                                                            |*")
    print("*|                                                                            |*")
    print("*|                                                                            |*")
    print("*|                                                                            |*")
    print("*|                       *******                                              |*")
    print("*|                    ***       ***                                           |*")
    print("*|                 ***             ***                                        |*")
    print("*|              ***                   ***                                     |*")
    print("*|           ***                         ***                                  |*")
    print("*|        ***                               ***                               |*")
    print("*|     ***                                     ***                            |*")
    print("*|  *************************************************                         |*")
    print("*|          *********************************                                 |*")
    print("*|          *                               *                                 |*")
    print("*|          *  *********                    *                                 |*")
    print("*|          *  *   |   *        ********    *                                 |*")
    print("*|          *  *-------*        *      *    *                                 |*")
    print("*|          *  *   |   *        *      *    *                                 |*")
    print("*|          *  *********        *    @ *    *                                 |*")
    print("*|          *                   *      *    *                                 |*")
    print("*|          *                   *      *    *                                 |*")
    print("*|          *********************************                                 |*")
    print("*|                                                                            |*")
    print("*------------------------------------------------------------------------------*")
    print("********************************************************************************")
    if (lifes <= 9):
        print("\033[4F\033[56C**\033[2D", end='')  # Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')  # Standing (for upper position, two left) and printing **
        print("\033[9E", end='')  # Returning to entered position
    if (lifes <= 8):  # SECOND module of gibbet(adding middle vertical module(6))
        print("\033[9F\033[56C**\033[2D", end='')  # Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')  # Standing (for upper position, two left) and printing **
        print("\033[14E", end='')  # Returning to entered position
    if (lifes <= 7):  # THIRD module of gibbet(adding last vertical module(6))
        print("\033[15F\033[56C**\033[2D", end='')  # Standing in start position + printing '**'
        for i in range(5):
            print("\033[1A**\033[2D", end='')  # Standing (for upper position, two left) and printing **
        print("\033[20E", end='')  # Returning to entered position
    if (lifes <= 6):  # FOURTH module of gibbet(adding horizontal plank)
        print("\033[20F\033[58C**************\033[2D",
              end='')  # Standing in start position + printing '**************'
        print("\033[20E", end='')  # Returning to entered position
    if (lifes <= 5):  # FIFTH module of gibbet(adding rope)
        print("\033[19F\033[71C*\033[1D", end='')  # Standing in start position + printing '*'
        for i in range(3):
            print("\033[1B*\033[1D", end='')  # Standing lower and printing *
        print("\033[16E", end='')  # Returning to entered position
    if (lifes <= 4):  # SIXTH module of gibbet(adding face)
        print("\033[15F\033[70C🙂\033[1D", end='')  # Standing in start position + printing '🥲'(face)
        print("\033[15E", end='')  # Returning to entered position
    if (lifes <= 3):  # SEVENTH module of gibbet(body + change face)
        print("\033[15F\033[70C😒\033[1D", end='')  # Standing in start position + printing '😒'(face)
        for i in range(4):
            print("\033[1B|\033[1D", end='')  # Standing (lower and left) and printing |
        print("\033[11E", end='')  # Returning to entered position
    if (lifes <= 2):  # EIGHTS module of gibbet(adding arms + change face)
        print("\033[15F\033[70C🥴\033[2D", end='')  # Standing in start position + printing ':pride:'(face)
        print("\033[1B/\033[1C\\", end='')  # Standing lower and printing \ /
        print("\033[1B\033[4D/\033[3C\\", end='')  # Standing lower and printing \ /
        print("\033[13E", end='')  # Returning to entered position
    if (lifes <= 1):  # NINTH module of gibbet(adding legs + change face)
        print("\033[15F\033[70C🥴\033[2D", end='')  # Standing in start position + printing '😱'(face)
        print("\033[5B/\033[1C\\", end='')  # Standing lower and printing / \
        print("\033[1B\033[4D/\033[3C\\", end='')  # Standing lower and printing /   \
        print("\033[9E", end='')  # Returning to entered position
    if (lifes <= 0):  # TENTH(LAST) module of gibbet(dying face)
        print("\033[15F\033[70C💀\033[1D", end='')  # Standing in start position + printing '💀'(face)
        print("\033[15E", end='')  # Returning to entered position
    print("\033[0m", end='')  # SWITCHING color to WHITE
    print(f"Available lives:{lifes}")
    print(("\033[6m" + '❤️' + " ") * lifes)


# word hide all letter by '_'
def hidden_word(list_letter_guess, random_word):
    guess = True
    print("Word that you need to guess:")
    print("\033[32m", end='')
    for i in random_word:
        if i in list_letter_guess:
            print(i, end=' ')
        elif i == '-' or i == ' ':
            print(i, end=' ')
        else:
            print('_', end=' ')
            guess = False
    print("\033[0m", end='')
    print("\n")
    return guess


# alphabet hiding letter
def available_letters(list_letter_guess, alphabet_string):
    print("Available letters:")
    for letter in alphabet_string:
        if letter in list_letter_guess:
            print('\_', end='')
        else:
            print(f'\{letter}', end='')
    print("\033[31m or quit\n")


# get random word and difficult of a word
def get_random():
    os.system("clear")
    print("\033[32m")
    tprint('=========')
    tprint('H A N G M A N')
    tprint('=========')
    print("\033[0m")
    r = RandomWords()
    time.sleep(0.5)
    level = ["[a] easy", "[b] medium", "[o] HARD AS HEELLL"]
    terminal_menu = TerminalMenu(level, title="Level of difficult:")
    menu_entry_index = terminal_menu.show()
    random_word = r.random_word()
    if level[menu_entry_index] == "[a] easy":
        while len(random_word) > 5:
            random_word = r.random_word()
    elif level[menu_entry_index] == "[b] medium":
        while 5 < len(random_word) < 10:
            random_word = r.random_word()
    elif level[menu_entry_index] == "[o] HARD AS HEELLL":
        while 10 < len(random_word):
            random_word = r.random_word()
    return random_word.lower()


def game():
    rules()
    lifes = 10
    alphabet_string = list(string.ascii_lowercase)
    list_letter_guess = []

    random_word = multiplayer(alphabet_string)

    isnot_alpha = True
    is_allready_input = False


    while lifes > 0:
        grafik(lifes)

        if lifes == 5:
            i = input("Do you want a hint?\n")
            if i == 'yes':
                print(f"\033[31mYou are PUSSY!\nBe a men, you left only {lifes} lifes!\n \033[0m")
            else:
                continue

        if isnot_alpha == False:
            print("\033[31mTry to print a Letter! Don't be a stupid!\033[0m")
        isnot_alpha = True

        if is_allready_input:
            print("\n\033[31mYou already try this letter, Dumbass!\033[0m")
        is_allready_input = False

        available_letters(list_letter_guess, alphabet_string)
        guess = hidden_word(list_letter_guess, random_word)

        if guess:
            print("\033[32m")
            tprint("YOU  WON !")
            print(f"YOUR SCORE IS {lifes}")
            print("\033[0m")
            break

        in_letter = input("choose a letter: ")
        if in_letter.lower() == 'quit':
            break
        if len(in_letter) > 1 or len(in_letter) == 0:
            print(str(len(in_letter)))
            continue

        # check for an letten no a random char, and
        if in_letter.lower() not in alphabet_string:
            isnot_alpha = False
            continue
        if in_letter in list_letter_guess:
            is_allready_input = True
            continue
        # add input to the list of word that allready been used
        list_letter_guess.append(in_letter)
        if in_letter not in random_word:
            lifes -= 1
            continue

    if lifes == 0:
        grafik(lifes)
        print("\033[31m")
        print(f"The word was \033[0m \033[32m{random_word}")
        print("\033[31m")
        tprint("YOU  Lose !")
        print("\033[0m")

    next_game = ["[y] Yes", "[n] NO"]
    terminal_menu = TerminalMenu(next_game, title="Next game?")
    menu_entry_index = terminal_menu.show()
    if next_game[menu_entry_index] == "[y] Yes":
        game()
    elif next_game[menu_entry_index] == "[n] NO":
        sys.exit()


game()
