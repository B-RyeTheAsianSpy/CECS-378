"""
Name:       Brian Nguyen
Class:      CECS 378 - Intro to Computer Security Principles
Start Date: 3/13/19
End Date:   3/24/19
"""


import binascii
from textwrap import wrap
import time

# location of save file (on my system)
location = "C:\\OLDGAMES\\ultima\\SAVED.GAM"
f = open(location, 'rb').read()
# removes all special characters and returns only the letters and numbers
hex_encoded = binascii.hexlify(f).decode('utf-8')
# combines two characters and appends them to a list
hex_list = wrap(hex_encoded, 2)
x = 32

"""

Functions for changing the character stats

"""


def change_strength(character):
    i = 14
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_change_single(character, change, i)


def change_intelligence(character):
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    # 1. Brian
    i = 16
    print('Changing...')
    time.sleep(2)
    hex_change_single(character, change, i)

def change_dexterity(character):
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    i = 15
    print('Changing...')
    time.sleep(2)
    hex_change_single(character, change, i)

def change_hp(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    while len(change) != 4:
        change = input("Please enter again: ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    i = 18
    print('Changing...')
    time.sleep(2)
    hex_change_double(character, a, b, i)

def change_max_hp(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    while len(change) != 4:
        change = input("Please enter again: ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    i = 20
    print('Changing...')
    time.sleep(2)
    hex_change_double(character, a, b, i)

def change_experience(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    while len(change) != 4:
        change = input("Please enter again: ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    i = 22
    print('Changing...')
    time.sleep(2)
    hex_change_double(character, a, b, i)


def hex_change_single(character, change, i):
    # 1. Brian
    if character == 1:
        hex_list[i] = change
    # 2. Shamino
    elif character == 2:
        hex_list[i + x] = change
    # 3. Iolo
    elif character == 3:
        hex_list[i + (x * 2)] = change
    # 4. Mariah
    elif character == 4:
        hex_list[i + (x * 3)] = change
    # 5. Geoffrey
    elif character == 5:
        hex_list[i + (x * 4)] = change
    # 6. Jaana
    elif character == 6:
        hex_list[i + (x * 5)] = change
    # 7. Julia
    elif character == 7:
        hex_list[i + (x * 6)] = change
    # 8. Dupre
    elif character == 8:
        hex_list[i + (x * 7)] = change
    # 9. Katrina
    elif character == 9:
        hex_list[i + (x * 8)] = change
    # 10. Sentri
    elif character == 10:
        hex_list[i + (x * 9)] = change
    # 11. Gwenno
    elif character == 11:
        hex_list[i + (x * 10)] = change
    # 12. Johne
    elif character == 12:
        hex_list[i + (x * 11)] = change
    # 13. Gorn
    elif character == 13:
        hex_list[i + (x * 12)] = change
    # 14. Maxwell
    elif character == 14:
        hex_list[i + (x * 13)] = change
    # 15. Toshi
    elif character == 15:
        hex_list[i + (x * 14)] = change
    # 16. Saduj
    elif character == 16:
        hex_list[i + (x * 15)] = change
    print('Success!')


def hex_change_double(character, a, b, i):
    # 1. Brian
    if character == 1:
        hex_list[i], hex_list[i + 1] = b, a
    # 2. Shamino
    elif character == 2:
        hex_list[i + x], hex_list[(i + x) + 1] = b, a
    # 3. Iolo
    elif character == 3:
        hex_list[i + (x * 2)], hex_list[(i + (x * 2)) + 1] = b, a
    # 4. Mariah
    elif character == 4:
        hex_list[i + (x * 3)], hex_list[(i + (x * 3)) + 1] = b, a
    # 5. Geoffrey
    elif character == 5:
        hex_list[i + (x * 4)], hex_list[(i + (x * 4)) + 1] = b, a
    # 6. Jaana
    elif character == 6:
        hex_list[i + (x * 5)], hex_list[(i + (x * 5)) + 1] = b, a
    # 7. Julia
    elif character == 7:
        hex_list[i + (x * 6)], hex_list[(i + (x * 6)) + 1] = b, a
    # 8. Dupre
    elif character == 8:
        hex_list[i + (x * 7)], hex_list[(i + (x * 7)) + 1] = b, a
    # 9. Katrina
    elif character == 9:
        hex_list[i + (x * 8)], hex_list[(i + (x * 8)) + 1] = b, a
    # 10. Sentri
    elif character == 10:
        hex_list[i + (x * 9)], hex_list[(i + (x * 9)) + 1] = b, a
    # 11. Gwenno
    elif character == 11:
        hex_list[i + (x * 10)], hex_list[(i + (x * 10)) + 1] = b, a
    # 12. Johne
    elif character == 12:
        hex_list[i + (x * 11)], hex_list[(i + (x * 11)) + 1] = b, a
    # 13. Gorn
    elif character == 13:
        hex_list[i + (x * 12)], hex_list[(i + (x * 12)) + 1] = b, a
    # 14. Maxwell
    elif character == 14:
        hex_list[i + (x * 13)], hex_list[(i + (x * 13)) + 1] = b, a
    # 15. Toshi
    elif character == 15:
        hex_list[i + (x * 14)], hex_list[(i + (x * 14)) + 1] = b, a
    # 16. Saduj
    elif character == 16:
        hex_list[i + (x * 15)], hex_list[(i + (x * 15)) + 1] = b, a
    print('Success!')

def change_gold():
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    while len(change) != 4:
        change = input("Please enter again: ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    print('Changing...')
    time.sleep(2)
    hex_list[516], hex_list[517] = b, a
    print('Success!\n')


"""
Functions for changing items
"""


def change_keys():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[518] = change
    print('Success!')


def change_gems():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[519] = change
    print('Success!')


def change_skull_keys():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[523] = change
    print('Success!')


def change_black_badges():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[536] = change
    print('Success!')


def change_magic_carpets():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[522] = change
    print('Success!')


def change_magic_axes():
    change = input("Enter your new value: ").lower()
    while len(change) != 2:
        change = input("Please enter again: ").lower()
    print('Changing...')
    time.sleep(2)
    hex_list[576] = change
    print('Success!\n')


"""
Menu functions
"""


def main_menu():
    print("----------------\n"
          "1.\tChange Character Stats\n"
          "2.\tChange Character Items\n"
          "3.\tExit\n")
    choice = int(input('Enter your selection: '))
    while choice < 1 or choice > 3:
        choice = int(input("Please try again: "))
    return choice


def character_menu():
    print("----------------\n"
          "1.\tBrian (main character)\n"
          "2.\tShamino\n"
          "3.\tIolo\n"
          "4.\tMariah\n"
          "5.\tGeoffrey\n"
          "6.\tJaana\n"
          "7.\tJulia\n"
          "8.\tDupre\n"
          "9.\tKatrina\n"
          "10.\tSentri\n"
          "11.\tGwenno\n"
          "12.\tJohne\n"
          "13.\tGorn\n"
          "14.\tMaxwell\n"
          "15.\tToshi\n"
          "16.\tSaduj\n"
          )
    choice = int(input("What character are you choosing? "))
    while choice < 1 or choice > 16:
        choice = int(input("Please try again: "))
    return choice


def stats_menu():
    print("----------------\n"
          "1.\tStrength\n"
          "2.\tIntelligence\n"
          "3.\tDexterity\n"
          "4.\tHP\n"
          "5.\tMax HP\n"
          "6.\tExperience\n"
          )
    choice = int(input("What stat you like to change? "))
    while choice < 1 or choice > 6:
        choice = int(input("Please try again: "))
    return choice


def item_menu():
    print("----------------\n"
          "1.\tKeys\n"
          "2.\tSkull Keys\n"
          "3.\tGems\n"
          "4.\tBlack Badges\n"
          "5.\tMagic Carpets\n"
          "6.\tMagic Axes\n"
          "7.\tGold\n")
    choice = int(input("What item you like to change? "))
    while choice < 1 or choice > 7:
        choice = int(input("Please try again: "))
    return choice


def return_main_menu():
    print("Returning to main menu...\n")
    time.sleep(3)
    return user_interface()


def user_interface():
    while True:
        s = main_menu()
        # change character stats
        if s == 1:
            # select character
            character = character_menu()
            stat = stats_menu()
            # 1. strength
            if stat == 1:
                change_strength(character)
            # 2. intelligence
            if stat == 2:
                change_intelligence(character)
            # 3. dexterity
            if stat == 3:
                change_dexterity(character)
            # 4. hp
            if stat == 4:
                change_hp(character)
            # 5. max hp
            if stat == 5:
                change_max_hp(character)
            # 6. experience
            if stat == 6:
                change_experience(character)
        # change character items
        if s == 2:
            item = item_menu()
            # 1. keys
            if item == 1:
                change_keys()
            # 2. skull keys
            if item == 2:
                change_skull_keys()
            # 3. gems
            if item == 3:
                change_gems()
            # 4. black badges
            if item == 4:
                change_black_badges()
            # 5. magic carpets
            if item == 5:
                change_magic_carpets()
            # 6. magic axes
            if item == 6:
                change_magic_axes()
            # 7. gold
            if item == 7:
                change_gold()
        if s == 3:
            break


def main():
    print("Welcome to B-Rye's Ultima V Hacking Tool!\n"
          "Please note that all values entered are in hexadecimal\n"
          "and have a length of 2 unless stated otherwise.\n"
          "Enjoy!\n")
    user_interface()


main()
f = open(location, 'wb')
new = "".join(hex_list)
hex_encoded = binascii.unhexlify(new)
f.write(hex_encoded)
