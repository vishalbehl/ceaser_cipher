logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# shift=shift%26          #If the shift amount is greater than alphabets

##############################################
#Method: 1

# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text} ")

# def decrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text} ")

# if direction=="encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(plain_text=text,shift_amount=shift)

###############################################
#Method: 2

# def ceaser(cipher_direction,plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         if cipher_direction=="encode":
#             new_position=position+shift_amount
#             new_letter=alphabet[new_position]
#             cipher_text+=new_letter
#         elif cipher_direction=="decode":
#             new_position=position-shift_amount
#             new_letter=alphabet[new_position]
#             cipher_text+=new_letter
#     print(f"The {direction}d text is {cipher_text}")

# ceaser(cipher_direction=direction,plain_text=text,shift_amount=shift)

###############################################
#Method: 3

def ceaser(cipher_direction,plain_text,shift_amount):
    cipher_text=""
    if cipher_direction=="decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=letter
    print(f"The {direction}d text is {cipher_text}")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26          #If the shift amount is greater than alphabets
    ceaser(cipher_direction=direction,plain_text=text,shift_amount=shift)

    result=input("Type 'Yes' if you want to go again,Otherwise type 'no'.\n")
    if result=="no":
        should_continue=False
        print("Good Bye!")
