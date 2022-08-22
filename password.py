import random

# Special Characters that people most likely use
special_char = "!@#$%^&?"

#These four vars are seperated so I can create a password that fits most modern requirments: 1 special character, 1 uppercase, and a number
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = '1234567890'

def randomize(input_string):
    list_string = list(input_string)
    random.shuffle(list_string)
    space = ""
    new_string = space.join(list_string)
    print(new_string)


randomize(lowercase[0:8])