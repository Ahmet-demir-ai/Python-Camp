import random
hangman_stages = [
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    =========
    YOU LOST!
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / 
      |
    =========
    Only 1 life left!
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   
      |
    =========
    2 lives left!
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |   
      |
    =========
    3 lives left!
    """,
    """
      ------
      |    |
      |    O
      |    |
      |   
      |
    =========
    4 lives left!
    """,
    """
      ------
      |    |
      |    O
      |    
      |   
      |
    =========
    5 lives left!
    """,
    """
      ------
      |    |
      |    
      |    
      |   
      |
    =========
    6 lives left!
    """
]

# Word list
word_list = [
    "elephant", "giraffe", "kangaroo", "dolphin", "crocodile", 
    "penguin", "octopus", "butterfly", "chameleon", "rhinoceros",
    "brazil", "canada", "germany", "japan", "norway",
    "strawberry", "pineapple", "blueberry", "watermelon",
    "galaxy", "meteor", "nebula", "asteroid", "telescope",
    "computer", "keyboard", "internet", "software"
]
chosen_word=random.choice(word_list)
print(chosen_word)
display=["-"]*len(chosen_word)
print(" ".join(display))
end_of_game=True
lives=6
print("Welcome to Hangman!")
while  end_of_game:
    guess=input("Guess a letter: ").lower()
    for index in range(len(chosen_word)):
        if chosen_word[index]==guess:
            display[index]=guess
        
    print(" ".join(display))
    if guess not in chosen_word:
        lives-=1
        print(f"{guess} is not in the word. You lose a life.")
        if lives==0:
            end_of_game=False
            print("You lose.")

    if "-" not in display:
        end_of_game=False
        print("You win.")   
    print(hangman_stages[lives])


    

