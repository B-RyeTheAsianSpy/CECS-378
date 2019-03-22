import binascii
from textwrap import wrap

location = "C:\\OLDGAMES\\ultima\\SAVED.GAM"
f = open(location, 'rb').read()
print(f)
hex_encoded = binascii.hexlify(f).decode('utf-8')
hex_list = wrap(hex_encoded, 2)



# brian_hex = hex_list[0:31]
# shamino_hex = hex_list[32:63]
# iolo_hex = hex_list[64:95]
# mariah_hex = hex_list[96:127]
# geoffrey_hex = hex_list[128:159]
# jaana_hex = hex_list[160:191]
# julia_hex = hex_list[192:223]
# dupre_hex = hex_list[224:255]
# katrina_hex = hex_list[256:287]
# sentri_hex = hex_list[288:319]
# gwenno_hex = hex_list[320:351]
# johne_hex = hex_list[352:383]
# gorn_hex = hex_list[384:415]
# maxwell_hex = hex_list[416:447]
# toshi_hex = hex_list[448:479]
# saduj_hex = hex_list[480:511]

def change_strength(character):
    change = input("Enter your new value: ").lower()
    # 1. Brian
    if character == 1:
        hex_list[14] = change
    # 2. Shamino
    elif character == 2:
        hex_list[46] = change
    # 3. Iolo
    elif character == 3:
        hex_list[78] = change
    # 4. Mariah
    elif character == 4:
        hex_list[110] = change
    # 5. Geoffrey
    elif character == 5:
        hex_list[142] = change
    # 6. Jaana
    elif character == 6:
        hex_list[174] = change
    # 7. Julia
    elif character == 7:
        hex_list[206] = change
    # 8. Dupre
    elif character == 8:
        hex_list[238] = change
    # 9. Katrina
    elif character == 9:
        hex_list[270] = change
    # 10. Sentri
    elif character == 10:
        hex_list[302] = change
    # 11. Gwenno
    elif character == 11:
        hex_list[334] = change
    # 12. Johne
    elif character == 12:
        hex_list[366] = change
    # 13. Gorn
    elif character == 13:
        hex_list[398] = change
    # 14. Maxwell
    elif character == 14:
        hex_list[430] = change
    # 15. Toshi
    elif character == 15:
        hex_list[462] = change
    # 16. Saduj
    elif character == 16:
        hex_list[494] = change


def change_intelligence(character):
    change = input("Enter your new value: ").lower()
    # 1. Brian
    if character == 1:
        hex_list[16] = change
    # 2. Shamino
    elif character == 2:
        hex_list[48] = change
    # 3. Iolo
    elif character == 3:
        hex_list[80] = change
    # 4. Mariah
    elif character == 4:
        hex_list[112] = change
    # 5. Geoffrey
    elif character == 5:
        hex_list[144] = change
    # 6. Jaana
    elif character == 6:
        hex_list[176] = change
    # 7. Julia
    elif character == 7:
        hex_list[208] = change
    # 8. Dupre
    elif character == 8:
        hex_list[240] = change
    # 9. Katrina
    elif character == 9:
        hex_list[272] = change
    # 10. Sentri
    elif character == 10:
        hex_list[304] = change
    # 11. Gwenno
    elif character == 11:
        hex_list[336] = change
    # 12. Johne
    elif character == 12:
        hex_list[368] = change
    # 13. Gorn
    elif character == 13:
        hex_list[400] = change
    # 14. Maxwell
    elif character == 14:
        hex_list[432] = change
    # 15. Toshi
    elif character == 15:
        hex_list[464] = change
    # 16. Saduj
    elif character == 16:
        hex_list[496] = change


def change_dexterity(character):
    change = input("Enter your new value: ").lower()
    # 1. Brian
    if character == 1:
        hex_list[15] = change
    # 2. Shamino
    elif character == 2:
        hex_list[47] = change
    # 3. Iolo
    elif character == 3:
        hex_list[79] = change
    # 4. Mariah
    elif character == 4:
        hex_list[111] = change
    # 5. Geoffrey
    elif character == 5:
        hex_list[143] = change
    # 6. Jaana
    elif character == 6:
        hex_list[175] = change
    # 7. Julia
    elif character == 7:
        hex_list[207] = change
    # 8. Dupre
    elif character == 8:
        hex_list[239] = change
    # 9. Katrina
    elif character == 9:
        hex_list[271] = change
    # 10. Sentri
    elif character == 10:
        hex_list[303] = change
    # 11. Gwenno
    elif character == 11:
        hex_list[335] = change
    # 12. Johne
    elif character == 12:
        hex_list[367] = change
    # 13. Gorn
    elif character == 13:
        hex_list[399] = change
    # 14. Maxwell
    elif character == 14:
        hex_list[431] = change
    # 15. Toshi
    elif character == 15:
        hex_list[463] = change
    # 16. Saduj
    elif character == 16:
        hex_list[495] = change


def change_hp(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    # 1. Brian
    if character == 1:
        print(hex_list[0:31])
        hex_list[18], hex_list[19] = b, a
        print(hex_list[0:31])
    # 2. Shamino
    elif character == 2:
        hex_list[50], hex_list[51] = b, a
    # 3. Iolo
    elif character == 3:
        print(hex_list[64:95])
        hex_list[82], hex_list[83] = b, a
        print(hex_list[64:95])
    # 4. Mariah
    elif character == 4:
        print(hex_list[64:95])
        hex_list[114], hex_list[115] = b, a
        print(hex_list[64:95])
    # 5. Geoffrey
    elif character == 5:
        hex_list[146], hex_list[147] = b, a
    # 6. Jaana
    elif character == 6:
        hex_list[178], hex_list[179] = b, a
    # 7. Julia
    elif character == 7:
        hex_list[210], hex_list[211] = b, a
    # 8. Dupre
    elif character == 8:
        hex_list[242], hex_list[243] = b, a
    # 9. Katrina
    elif character == 9:
        hex_list[274], hex_list[271] = b, a
    # 10. Sentri
    elif character == 10:
        hex_list[306], hex_list[307] = b, a
    # 11. Gwenno
    elif character == 11:
        hex_list[338], hex_list[339] = b, a
    # 12. Johne
    elif character == 12:
        hex_list[370], hex_list[371] = b, a
    # 13. Gorn
    elif character == 13:
        hex_list[402], hex_list[403] = b, a
    # 14. Maxwell
    elif character == 14:
        hex_list[434], hex_list[435] = b, a
    # 15. Toshi
    elif character == 15:
        hex_list[466], hex_list[467] = b, a
    # 16. Saduj
    elif character == 16:
        hex_list[498], hex_list[499] = b, a


def change_max_hp(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    # 1. Brian
    if character == 1:
        print(hex_list[0:31])
        hex_list[20], hex_list[21] = b, a
        print(hex_list[0:31])
    # 2. Shamino
    elif character == 2:
        hex_list[52], hex_list[53] = b, a
    # 3. Iolo
    elif character == 3:
        print(hex_list[64:95])
        hex_list[84], hex_list[85] = b, a
        print(hex_list[64:95])
    # 4. Mariah
    elif character == 4:
        print(hex_list[64:95])
        hex_list[116], hex_list[118] = b, a
        print(hex_list[64:95])
    # 5. Geoffrey
    elif character == 5:
        hex_list[148], hex_list[149] = b, a
    # 6. Jaana
    elif character == 6:
        hex_list[180], hex_list[181] = b, a
    # 7. Julia
    elif character == 7:
        hex_list[212], hex_list[213] = b, a
    # 8. Dupre
    elif character == 8:
        hex_list[244], hex_list[245] = b, a
    # 9. Katrina
    elif character == 9:
        hex_list[276], hex_list[277] = b, a
    # 10. Sentri
    elif character == 10:
        hex_list[308], hex_list[309] = b, a
    # 11. Gwenno
    elif character == 11:
        hex_list[340], hex_list[341] = b, a
    # 12. Johne
    elif character == 12:
        hex_list[372], hex_list[373] = b, a
    # 13. Gorn
    elif character == 13:
        hex_list[404], hex_list[405] = b, a
    # 14. Maxwell
    elif character == 14:
        hex_list[436], hex_list[437] = b, a
    # 15. Toshi
    elif character == 15:
        hex_list[468], hex_list[469] = b, a
    # 16. Saduj
    elif character == 16:
        hex_list[500], hex_list[501] = b, a

def change_experience(character):
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    # 1. Brian
    if character == 1:
        print(hex_list[0:31])
        hex_list[22], hex_list[23] = b, a
        print(hex_list[0:31])
    # 2. Shamino
    elif character == 2:
        hex_list[54], hex_list[55] = b, a
    # 3. Iolo
    elif character == 3:
        print(hex_list[64:95])
        hex_list[86], hex_list[87] = b, a
        print(hex_list[64:95])
    # 4. Mariah
    elif character == 4:
        print(hex_list[64:95])
        hex_list[118], hex_list[120] = b, a
        print(hex_list[64:95])
    # 5. Geoffrey
    elif character == 5:
        hex_list[150], hex_list[151] = b, a
    # 6. Jaana
    elif character == 6:
        hex_list[182], hex_list[183] = b, a
    # 7. Julia
    elif character == 7:
        hex_list[214], hex_list[215] = b, a
    # 8. Dupre
    elif character == 8:
        hex_list[246], hex_list[247] = b, a
    # 9. Katrina
    elif character == 9:
        hex_list[278], hex_list[279] = b, a
    # 10. Sentri
    elif character == 10:
        hex_list[310], hex_list[311] = b, a
    # 11. Gwenno
    elif character == 11:
        hex_list[342], hex_list[343] = b, a
    # 12. Johne
    elif character == 12:
        hex_list[374], hex_list[375] = b, a
    # 13. Gorn
    elif character == 13:
        hex_list[406], hex_list[407] = b, a
    # 14. Maxwell
    elif character == 14:
        hex_list[438], hex_list[439] = b, a
    # 15. Toshi
    elif character == 15:
        hex_list[470], hex_list[471] = b, a
    # 16. Saduj
    elif character == 16:
        hex_list[502], hex_list[503] = b, a

def change_gold():
    change = input("Enter your new value (PLEASE PUT 4 DIGITS): ").lower()
    # first half
    a = change[0:len(change) // 2]
    # second half
    b = change[len(change) // 2 if len(change) % 2 == 0 else ((len(change) // 2) + 1):]
    hex_list[516], hex_list[517] = b, a
    print(hex_list)


def main_menu():
    print("1.\tChange Character Stats\n"
          "2.\tChange Character Items\n"
          "3.\tExit\n")


def character_menu():
    print("1.\tBrian (main character)\n"
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
          "16.\tSaduj\n")
    choice = int(input("What character are you choosing? "))
    return choice

def stats_menu():
    print("1.\tStrength\n"
          "2.\tIntelligence\n"
          "3.\tDexterity\n"
          "4.\tHP\n"
          "5.\tMax HP\n"
          "6.\tExperience\n"
          "7.\tGold\n")
    choice = int(input("What would you like to change? "))
    return choice


def menu_selection():
    s = int(input('Enter your selection: '))
    return s


def user_interface():
    while True:
        main_menu()
        s = menu_selection()
        # change character stats
        if s == 1:
            # select character
            character = character_menu()
            stat = stats_menu()
            if stat == 1:
                change_strength(character)
            if stat == 2:
                change_intelligence(character)
            if stat == 3:
                change_dexterity(character)
            if stat == 4:
                change_hp(character)
            if stat == 5:
                change_max_hp(character)
            if stat == 7 and character == 1:
                change_gold()
        if s == 2:
            print('\n*****UNDER CONSTRUCTION*****\n')
        if s == 3:
            break
        if s == 4:
            print(hex_list)


def main():

    user_interface()


main()

print(hex_list)
d = open(location, 'wb')
new = "".join(hex_list)
print(new)
hex_encoded = binascii.unhexlify(new)
d.write(hex_encoded)
