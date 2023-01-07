#Code to generate a random password using random module

import random
import string
def random_pass(length):
    password = ''
    char = string.ascii_letters
    for i in range(length):
        password += random.choice(char + string.digits)
    return password


print(random_pass(10))
print(random_pass(7))
random_pass(5)
