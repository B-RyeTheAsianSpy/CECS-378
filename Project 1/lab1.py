from pycipher import SimpleSubstitution as SS
import random
from ngram_score import ngram_score



alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# function to take every character in the list and concatenate together to form a full string
def list_to_string(message):
    string = ''
    for x in message:
        string += x
    return string

# caesar cipher decryption function
def caesar_cipher_decryption(cipher_text):
    cipher_text = cipher_text.upper()
    print('Your message:', cipher_text)
    # takes every character from the string and puts each of them in the list
    # as their own element
    cipher_text = list(cipher_text)

    # user enters the key, which is a numeric value
    key = int(input('Enter your key: '))

    # list to store characters of the decrypted message
    decrypted_text = []
    for letter in cipher_text:
        # if the current index contains a letter
        if letter.isalpha():
            # retrieves the index position of the letter in the alphabet
            # A-Z, 0-25
            index = alphabet.index(letter)

            # retrieves the shifted letter. If the value of (index - key) exceeds 26 (z),
            # then the value will go back to the beginning of the alphabet
            shift_amount = (index - key) % 26
            shifted_letter = alphabet[shift_amount]
            decrypted_text.append(shifted_letter)

        # if the current index contains whitespace
        else:
            decrypted_text.append('')
    # takes decrypted message and converts to string
    decrypted_text = list_to_string(decrypted_text)
    print('Your decrypted message:', decrypted_text)

# function for simple substitution decryption
def simple_sub_decipher(cipher_text):
    # the english_quadrams text file contains 4-count letter words with their score
    # their score is based on their frequency in the English language
    ng = ngram_score('english_quadgrams.txt')

    input("The simple substitution decipher will take a while to complete. The program will terminate at a certain point. "
              "Please be patient\n"
              "Press ENTER to begin: ")
    cipher_text.upper()
    max_key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # the default score
    max_score = -99e9

    parent_key = max_key

    # list to store keys already used
    discarded_keys = []
    i = 0
    while True:
        # get a random key
        random.shuffle(parent_key)

        # use that key to decipher the ciphertext
        deciphered_text = SS(parent_key).decipher(cipher_text)

        # get the score from the deciphered text
        parent_score = ng.score(deciphered_text)

        # generate a new key
        new_key = parent_key[:]
        random.shuffle(new_key)

        # if a generated key was used before, then another one will be generated
        if new_key in discarded_keys:
            flag = True
            while flag:
                # the loop will continue to generate a unique key that is not already used before
                random.shuffle(new_key)
                if new_key not in discarded_keys:
                    flag = False

        # new deciphered text using the new key
        deciphered_text = SS(new_key).decipher(cipher_text)

        # get the score from the new deciphered text using the new key
        child_score = ng.score(deciphered_text)

        # if the score is an improvement on the previous score
        if child_score > parent_score:
            parent_score = child_score

        # used keys will be put in the discarded keys list so they wouldn't be used anymore
        discarded_keys.append(new_key)
        discarded_keys.append(parent_key)

        # if the score is greater than the max score, then the key used is more likely to decipher the cipher text
        if parent_score > max_score:
            max_score = parent_score
            max_key = new_key
            ss = SS(max_key)
            print('---------------------------------------------'
                  '\nSCORE:', max_score)
            print('KEY:', list_to_string(max_key))
            print('DECIPHERED TEXT:', ss.decipher(cipher_text))

        i += 1

        # statement for ending the program after certain number of iterations
        if i == 50000:
            print('The program has run for long enough. Terminating...')
            break

# function for choosing a message and then decrypting it
def get_message(choice):

    message_1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"

    message_2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv " \
                "aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"

    message_3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa " \
                "twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

    message_4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq " \
                "iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs " \
                "hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt " \
                "isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun " \
                "siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq " \
                "uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    # message 1 - caesar cipher decryption
    if choice == 1:
        caesar_cipher_decryption(message_1)

    # message 2 - caesar cipher decryption
    elif choice == 2:
        caesar_cipher_decryption(message_2)

    # message 3 - simple substitution decryption
    elif choice == 3:
        simple_sub_decipher(message_3)

    # message 4 - simple substitution decryptionn
    elif choice == 4:
        simple_sub_decipher(message_4)

# function to display main menu
def menu():
    print("---------------\n"
          "1.\tMessage 1\n"
          "2.\tMessage 2\n"
          "3.\tMessage 3\n"
          "4.\tMessage 4\n"
          "5.\tExit\n---------------")

def main():
    flag = True
    while flag:
        menu()
        choice = int(input('Please enter your choice: '))

        # input validation
        while choice < 1 or choice > 5:
            choice = int(input('Please enter again: '))

        # exit the program
        if choice == 5:
            flag = False

        # other choices
        else:
            get_message(choice)


main()
