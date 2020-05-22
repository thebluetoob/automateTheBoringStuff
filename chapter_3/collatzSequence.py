#!/usr/bin/env python3

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

userInput = input('Please enter a number: ')
while userInput != 1:
    userInput = collatz(int(userInput))