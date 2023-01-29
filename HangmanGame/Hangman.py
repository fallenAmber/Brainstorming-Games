
import random
import string
from hangman_visual import lives_visual_dict
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters=set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print('You have', lives, 'lives left and you have used the letters: ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet-word_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives-1
                print("Guessed letter", user_letter, "is not in the word")
        elif user_letter in used_letters:
            print("Sorry, you have already used this letter.")
        else:
            print("This is not a valid input.")

    if lives ==0:
        print(lives_visual_dict[lives])
        print(f"Sorry, you have no life left for guessing the word. The word was {word}!")
    else:
        print("Yaaaay! You have guessed the word!!!!")

if __name__=='__main__':
    hangman()
