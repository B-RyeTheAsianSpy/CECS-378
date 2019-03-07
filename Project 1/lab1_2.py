import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# function for encrypting a message with simple substitution
#
def simple_sub_encrypt(key, message):
    print('Your key:', key)
    cipher_text = ""
    # the first for loop goes through each letter of the message
    for i in range(len(message)):
        count = 0
        # the second for loop iterates through the letters of the key.
        # when the current letter of the message is in the key, it will retrieve the index of
        # that letter in the key, retrieve the letter itself, then append it to the
        # cipher text
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                cipher_text += key[count]
            else:
                count += 1
    print("Your cipher-text:", cipher_text)

# function for generating a random key key
def key_generator():
    key = list(alphabet)
    random.shuffle(key)
    return ''.join(key)

# function for displaying the main menu
def main_menu():
    print("---------------\n"
          "1.\tEnter your own message\n"
          "2.\tSelect stock message\n"
          "3.\tExit\n---------------")

# function for displaying the menu for stock messages
def stock_message_menu():
    print("---------------\n"
          "1.\tMessage 1\n"
          "2.\tMessage 2\n"
          "3.\tMessage 3\n"
          "---------------")

# function for choosing a message and then encrypting it
def get_message(choice):

    message_1 = "He who fights with monsters should look to it that he " \
               "himself does not become a monster . And if you gaze long into an abyss , " \
               "the abyss also gazes into you."

    message_2 = "There is a theory which states that if ever anybody discovers exactly what the" \
               " Universe is for and why it is here , it will instantly disappear and be replaced " \
               "by something even more bizarre and inexplicable . There is another theory which states" \
               " that this has already happened ."

    message_3 = "Whenever I find myself growing grim about the mouth ; whenever it is a damp ," \
               " drizzly November in my soul ; whenever I find myself involuntarily pausing before" \
               " coffin warehouses , and bringing up the rear of every funeral I meet ; and especially" \
               " whenever my hypos get such an upper hand of me , that it requires a strong moral principle" \
               " to prevent me from deliberately stepping into the street , and methodically knocking people ’s" \
               " hats off - then , I account it high time to get to sea as soon as I can."
    # message 1
    if choice == 1:
        simple_sub_encrypt(key_generator(), message_1.upper())

    # message 2
    elif choice == 2:
        simple_sub_encrypt(key_generator(), message_2.upper())

    # message 3
    elif choice == 3:
        simple_sub_encrypt(key_generator(), message_3.upper())

def main():
    print("SIMPLE SUBSTITUTION ENCRYPTION")
    flag = True
    while flag:
        main_menu()
        choice = int(input('Please enter your choice: '))
        # input validation loop
        while choice < 1 or choice > 3:
            choice = int(input('Please enter again: '))

        # if the user chooses to input their own message
        if choice == 1:
            message = input("Enter your message: ")
            simple_sub_encrypt(key_generator(), message.upper())

        # if the user chooses to select a stock message
        elif choice == 2:
            stock_message_menu()
            choice = int(input('Please select your message: '))

            # input validation
            while choice < 1 or choice > 3:
                choice = int(input('Please enter again: '))

            # message 1
            if choice == 1:
                get_message(1)

            # message 2
            elif choice == 2:
                get_message(2)

            # message 3
            elif choice == 3:
                get_message(3)

        # if the user chooses to exit the program
        elif choice == 3:
            flag = False


main()
