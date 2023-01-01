HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

word = 'panda'
tip = 'animal'

def hideWord(good_letters):
    hidden_word = ''
    for letter in word:
        if letter in good_letters:
            hidden_word = hidden_word + letter + " "
        else:
            hidden_word = hidden_word + "_ "
    return hidden_word

def main():
    good_letters = []
    used_letters = []
    used_letters_message = "\n\nUsed letters: "
    used_lives = 0

    hidden_word = hideWord(good_letters)
    print(HANGMAN_PICS[used_lives] + "\t" + hidden_word + "(Tip: " + tip + ")" + used_letters_message + "\n")
    
    while(used_lives < (len(HANGMAN_PICS) - 1)):
        
        letter = input("Type a letter: ")
        
        # Does not take one life for repeated letters
        if letter in used_letters:
            continue

        if letter in word:
            good_letters.append(letter)
        else:
            used_lives += 1
        
        used_letters.append(letter)
        used_letters_message = used_letters_message + letter + " "
        hidden_word = hideWord(good_letters)
        
        print(HANGMAN_PICS[used_lives] + "\t" + hidden_word + "(Tip: " + tip + ")" + used_letters_message + "\n")
        
        hidden_word_to_check = hidden_word.replace(" ", "")
        if hidden_word_to_check == word:
            break

    if used_lives == len(HANGMAN_PICS)-1:
        print("You have failed with the hangman")
    else:
        print("You have saved the man")

if __name__ == "__main__":
    main()