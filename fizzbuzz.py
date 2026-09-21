import time
import random

def createWord(num, num1, num2, num3, num4, word1, word2, word3, word4):
    word = ""
    if num % num1 == 0:
        word += word1
    if num % num2 == 0:
        word += word2
    if num % num3 == 0:
        word += word3
    if num % num4 == 0:
        word += word4
    if len(word) == 0:
        return num
    else:
        return word

def checkInput(num):
    if "y" in num:
        return True
    else:
        return False

def playGame():
    players = ["computer", "player"]
    playing = True
    turn = random.choice(players)
    currentIndex = 0
    strikes = 0
    while playing:
        if turn == "computer":
            turn = random.choice(players)
            print(main_list[currentIndex])
            currentIndex += 1
            if currentIndex > len(main_list):
                playing = False

        else:
            turn = random.choice(players)
            num = str(input(""))
            if num.lower() != main_list[currentIndex]:
                print("INCORRECT")
                strikes += 1
                if strikes > 3:
                    print("You're Out!")
                    playing = False
                elif currentIndex > len(main_list):
                    playing = False
            currentIndex += 1


start = int(input("Start with: "))
count = int(input("Count up to: "))
num1 = int(input("First Number: ") or 3)
word1 = str(input(f"Word when number is a multiple of {num1}: ") or "Fizz")
num2 = int(input("Second Number: ") or 5)
word2 = str(input(f"Word when number is a multiple of {num2}: ") or "Buzz")
threeNumbers = str(input("Do 3 numbers? ") or "y")
fourNumbers = str(input("Do 4 numbers? ") or "y")

threeNumbers = checkInput(threeNumbers)
fourNumbers = checkInput(fourNumbers)

if threeNumbers:
    num3 = int(input("Third Number: ") or 6)
    word3 = str(input(f"Word when number is a multiple of {num3}: ") or "Mazz")
else: 
    num3 = -1
    word3 = ""

if fourNumbers:
    num4 = int(input("Fourth Number: ") or 7)
    word4 = str(input(f"Word when number is a multiple of {num4}: ") or "Chizz")
else:
    num4 = -1
    word4 = ""

main_list = []

for i in range(start if start > 0 else 1, count+1):
    main_list.append(str(createWord(i, num1, num2, num3, num4, word1, word2, word3, word4)).lower())

game = str(input("Do you want to play against me?") or "y")

game = checkInput(game)

if not game:
    for i in main_list:
        print(i)
else:
    playGame()