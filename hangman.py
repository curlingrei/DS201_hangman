import random
words_list = ["python", "pandas", "numpy", "spreadsheet", "tableau", "function", "variable", "matplotlib"]
guessed_letters = []
last_index = len(words_list)
index_of_target_word = random.randint(0, last_index - 1)
incorrect_count = 0
match_count = 0
target_word = words_list[index_of_target_word]
length_of_target_word = len(target_word)
limit = 6 + length_of_target_word // 3

print("Welcome to Hangman!")
print("Let's guess the word by inputting one letter one after another.")
print(f"You can make wrong guesses up to {limit} times.")
print()

while True:
    print("Current word: ", end="")
    for letter in target_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    print("guessed_letter: ", end="")
    for index in range(len(guessed_letters)):
        if not index == 0:
            print(", ", end="")
        print(guessed_letters[index], end="")

    print()
    print(f"Incorrect guesses remaining: {limit - incorrect_count}")
    print()

    while True:
        input_letter = input("Guess a letter: ")
        if input_letter not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            print("Invalid Value! Input only one alphabet in lower case")
            continue
        elif len(input_letter) != 1:
            print("Invalid Value! Input only one alphabet in lower case")
            continue
        elif input_letter in guessed_letters:
            print("You already used the letter. Try again.")
            continue
        else:
            guessed_letters.append(input_letter)
            break

    if input_letter in target_word:
        match_count += target_word.count(input_letter)


    if input_letter in target_word:
        print(f"Good job!, {input_letter} is in the word.")
        match_count += target_word.count(input_letter)
    else:
        print(f"Sorry, {input_letter} is not in the word.")
        incorrect_count += 1

    if match_count == length_of_target_word:
        print(f"Congratulations! You got the right word: {target_word}")
        break

    if incorrect_count == limit:
        print(f"Game over! The word was: {target_word}")
        break
