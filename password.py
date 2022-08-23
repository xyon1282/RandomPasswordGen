import argparse
import random

# Accept command line arguments to alter password length, and number of passwords
parser = argparse.ArgumentParser(description='Process values for password output.')
parser.add_argument("--low", type=int)
parser.add_argument("--up", type=int)
parser.add_argument("--num", type=int)
parser.add_argument("--spec", type=int)

args = parser.parse_args()

# These four vars are seperated so I can create a password that fits most modern requirments: 1 special character, 1 uppercase, and a number
# Special Characters that people most likely use
special_char = "!@#$%^&?"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = '1234567890'

# Randomize above character lists
def randomize(input_string):
    list_string = list(input_string)
    random.shuffle(list_string)
    space = ""
    new_string = space.join(list_string)
    return new_string


rand_low = randomize(lowercase)
rand_up = randomize(uppercase)
rand_num = randomize(num)
rand_spec = randomize(special_char)

default_rand = randomize(rand_spec[0:1] + rand_num[0:1] + rand_up[0:1] + rand_low[0:5])


# Checks to see if user used the --char flag. If not, then default value of 8 is used
if args.spec:
        custom_rand = randomize(rand_spec[0:args.spec] + rand_num[0:args.num] + rand_up[0:args.up] + rand_low[0:args.low])
        print(custom_rand)
else:
    print(default_rand)