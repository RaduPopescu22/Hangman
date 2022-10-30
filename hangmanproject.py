
from random_word import RandomWords
r = RandomWords()
# command: .get_random_word()
print("************HANGMAN GAME****************")
# difficulty selection and selection validity
diff_selection = input("Please choose a difficulty - (easy , medium, hard): ")
valid_selection = ["easy","medium","hard"]
while diff_selection.isnumeric() or diff_selection.lower() not in valid_selection:
    diff_selection = input("Please choose a difficulty - (easy , medium, hard): ")
# word assignation based on difficulty
def word_pick(difficulty,pick=r.get_random_word()):
    if difficulty == "easy":
        while not len(pick) <= 5:
            pick = r.get_random_word()
        return pick
    elif difficulty == "medium":
        while not len(pick) <= 7:
            pick = r.get_random_word()
        return pick
    else:
        while not len(pick) > 7:
            pick = r.get_random_word()
        return pick
word = word_pick(diff_selection)
display_word = "_" * len(word)
num_lives = 6
already_guessed = []
def game_state():
    if num_lives > 0:
        return True
    else:
        return False
# Stickman completion logic
def hangman(lives_left):
    if lives_left == 5:
        return "         ( )"
    elif lives_left == 4:
        return '''        ( )
         |'''
    elif lives_left == 3:
        return '''         ( )
         /|'''
    elif lives_left == 2:
        return '''         ( )
         /|\\'''
    elif lives_left == 1:
        return '''         ( )
         /|\\
         /'''
    else:
        return '''         ( )
         /|\\
         / \\'''
print(f"WORD: {display_word}")
while game_state():
    guess = input("\nPlease type a letter: ")
 # Answer validity check   
    while len(guess) > 1 or guess.isnumeric():
        guess = input("\nPlease choose one letter only!")
    while guess in already_guessed:
        guess = input(f"\nYou've already tried {guess}, pick something else: ")
    already_guessed.append(guess)
 # Word completion logic if guess is correct
    indx_word = []
    count = 0
    for char in word:
        if char == guess:
            indx_word.append(count)
        count += 1
    display_word = list(display_word)
    for elem in indx_word:
        display_word[elem] = guess
    display_word = "".join(display_word)
  # Output word  
    print("*" * 40)
    print(f"WORD: {display_word}")
    print("*" * 40)
 # Mistake logic
    if guess not in word:
        num_lives -= 1
        if num_lives > 1:
            print(f"WRONG! You have {num_lives} lives left!")
        elif num_lives == 1:
            print(f"WRONG! You have {num_lives} life left!")
 # Hangman drawing
    if num_lives < 6:    
        print(hangman(num_lives))
 # Win path
    if "_" not in display_word:
        break

# Endings
if not game_state():
    print(f'You lost all your lives :( :(. The word was "{word}"')
else:
    print(f'Congrats!! You won!! The word was "{word}"!')




    