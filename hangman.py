import random

choice = random.choice(['python', 'java', 'kotlin', 'javascript'])
hint = list("-" * len(choice))
lives = 0
guesses = []

print("H A N G M A N")

selection = input('Type "play" to play the game, "exit" to quit:')
if selection == "play":
    lives = 8
elif selection == "quit":
    lives = 0
    
while lives > 0:
    print()
    print(''.join(hint))
    letter = input("Input a letter:")
    if len(letter) != 1:
        print("You should input a single letter")
        continue    
    if not letter.islower():
        print("Please enter a lowercase English letter")
        continue
    if letter in guesses:
        print("You've already guessed this letter")
        continue
    guesses.append(letter)
    for index in range(len(choice)):
        if letter == choice[index]:
            hint[index] = letter
    if letter not in choice:
        print("That letter doesn't appear in the word")
        lives -= 1
    if "-" not in hint:
        print("You guessed the word!")
        if lives >= 0:
            print("You survived!")
        break
else:
    print("You lost!")
