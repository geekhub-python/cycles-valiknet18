#!/usr/bin/env python3

current_index = 11

while True:
    flag = True

    for i in range(2, 11):
        if (current_index % i) != 1:
            flag = False
            break

    if flag:
        print(current_index)
        break

    current_index += 11

