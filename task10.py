#!/usr/bin/env python3

import random
import string

digits = random.randint(a=10, b=10000)
randomLetters = []
randomDigits = []
password = "_"

randomDigits = [i for i in str(digits)]
randomLetters = [random.choice(string.ascii_uppercase) for i in range(len(str(digits)))]

for i in range(len(randomDigits)):
    password += randomDigits[i]
    password += randomLetters[i]

print(password)
