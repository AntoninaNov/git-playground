import words_fetcher
import random
from itertools import permutations


def congratulate_user():
    print(f"Your words: {guesses}")
    print("=============================")
    print("= Congratulations! You won! =")
    print("=============================")


def user_lost():
    print("====================")
    print("= Hehe:) You lost! =")
    print("====================")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

word_letters = set(word)
appropriate_words = set()
guesses = set()

for n in range(3, len(word)):
    for y in list(permutations(word_letters, n)):
        permuted_word = "".join(y)
        if permuted_word in full_list:
            appropriate_words.add(permuted_word)

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")
    if guess in appropriate_words - guesses:
        guessed += 1
        guesses.add(guess)
        if guessed == WORDS_TO_WIN:
            congratulate_user()
            exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    elif guess in guesses:
        print("You have already used that word. Choose another.")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
    if errors == ERRORS_TO_LOSE:
        user_lost()
        exit()
