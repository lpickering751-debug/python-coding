import random


def letterScore(letter):

    score = scores[letter.upper()]

    return score


def wordscore(word):

    score = 0

    for letter in word:

        score += letterScore(letter)

    return score


dictionary_file = open("dictionary.txt", "r")

valid_words = {line.strip().upper() for line in dictionary_file}


scores = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


bag = (
    ["A"] * 9
    + ["B"] * 2
    + ["C"] * 2
    + ["D"] * 4
    + ["E"] * 12
    + ["F"] * 2
    + ["G"] * 3
    + ["H"] * 2
    + ["I"] * 9
    + ["J"] * 1
    + ["K"] * 1
    + ["L"] * 4
    + ["M"] * 2
    + ["N"] * 6
    + ["O"] * 8
    + ["P"] * 2
    + ["Q"] * 1
    + ["R"] * 6
    + ["S"] * 4
    + ["T"] * 6
    + ["U"] * 4
    + ["V"] * 2
    + ["W"] * 2
    + ["X"] * 1
    + ["Y"] * 2
    + ["Z"] * 1
)


letters_needed = 7

player_letters = []

total_games = 0

old_scores = ""

invalid = False


try:

    with open("scores.txt", "r") as score_file:

        lines = score_file.readlines()

    if lines:

        total_games = int(lines[0].split(":")[1])

    old_scores = "".join(lines[1:])


except FileNotFoundError:

    total_games = 0


total_games += 1


with open("scores.txt", "w") as score_file:

    score_file.write(f"total games: {total_games}\n")

    score_file.write(old_scores)

    score_file.write(f"\ngame {total_games}\n")


score_file = open("scores.txt", "a")


while len(bag) > 0 or len(player_letters) > 0:
    invalid = False

    for i in range(letters_needed):

        letter = random.choice(bag)

        player_letters.append(letter)

        bag.remove(letter)

    print(f"Your letters are \n {', '.join(player_letters)}")

    player_input = input("Word: ")

    if player_input.upper() in valid_words:

        for letter in list(player_input):

            if letter.upper() not in player_letters:

                print("you cannot use: " + letter)

                invalid = True


        else:
            if not invalid:
                for letter in list(player_input):

                    player_letters.remove(letter.upper())

    else:
        print("Not a valid word")

        break
    if not invalid:
        print(f"Score: {wordscore(player_input)}")

        score_file.writelines(str(wordscore(player_input)))

        score_file.writelines("\n")

    letters_needed = min(7 - len(player_letters), len(bag))


score_file.close()

dictionary_file.close()