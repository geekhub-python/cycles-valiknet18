#!/usr/bin/env python3

alpha = str(input("Write letter: "))
indexAlpha = ord(alpha)
steps = 3
startAlpha = 97
endAlpha = 122

while (steps > 0):
    indexAlpha += 1
    if indexAlpha > endAlpha:
        indexAlpha = startAlpha
    print(chr(indexAlpha))
    steps -= 1
