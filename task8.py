#!/usr/bin/env python3

for i in range(1000, 10000):
    first_number = i % 10
    second_number = i % 100 // 10
    third_number = i % 1000 // 100
    fourth_number = i // 1000

    check_first_number = (first_number != 6 and first_number != 5)
    check_second_number = (second_number != 6 and second_number != 5)
    check_third_number = (third_number != 6 and third_number != 5)
    check_fourth_number = (fourth_number != 6 and fourth_number != 5)

    if check_first_number and check_second_number and check_third_number and check_fourth_number:
        print(i)
