import random


def choose_word():
    words = ["python", "developer", "hangman", "challenge", "programming"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman(simulated_inputs=None):
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    input_index = 0

    print("Welcome to Hangman!")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")

        if simulated_inputs:
            if input_index >= len(simulated_inputs):
                print("No more simulated inputs. Exiting...")
                return
            guess = simulated_inputs[input_index].lower()
            print(f"Guessing: {guess}")
            input_index += 1
        else:
            return  # Prevent input() call in sandboxed environments

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")

        if set(word) <= guessed_letters:
            print(f"Congratulations! You guessed the word: {word}")
            return

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    test_inputs = ["p", "y", "t", "h", "o", "n"]  # Example inputs for testing
    hangman(test_inputs)
