import random
from word import words

ok = False;

def color_text(text, background_code):
    color_dict = {
        "black": '\033[30m',
        "reset": '\033[0m'
    }
    background_dict = {
        "green": '\033[42m',
        "yellow": '\033[43m',
        "gray": '\033[47m',
        "reset": '\033[49m'
    }
   
    return f"{background_dict.get(background_code, background_dict['reset'])}{color_dict['black']}{text}{color_dict['reset']}"

def check_word(guess, target):
    ans = []
    for i in range(5):
        if guess[i] == target[i]:
            ans.append(color_text(guess[i], "green"))
        elif guess[i] in target:
            ans.append(color_text(guess[i], "yellow"))
        else:
            ans.append(color_text(guess[i], "gray"))
    return ''.join(ans)

def wordle():
    global ok 
    attempts = 6
    answer = random.choice(words)
    while attempts > 0:
        guess = input(f'You have {attempts} attempts left. Enter your guess: ').lower()
        if len(guess) != 5 or not guess.isalpha() or guess not in words:
            print('Enter a valid 5-letter word')
            continue
        feedback = check_word(guess, answer)
        print(feedback)
        if guess == answer:
            print("You've guessed the word!")
            break
        attempts -= 1
    if guess != answer:
        print(f"You've run out of attempts. The correct word was: {answer}")
    
    x = input("Play again Y/N: " ).upper()
    if x == "Y":
        ok = True
    else:
        ok = False

 
if __name__ == '__main__':
    wordle()
    while ok:
        wordle()
