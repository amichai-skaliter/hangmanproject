# This is the code of a Hangman game created by Amichai Skaliter.
# All secret words are animals.
# Some code lines are splitted to several lines,  
# in order to not pass the "Pep 8" 79 characters limit.
# I did not use the check_valid_input function, and merged it with try_update_letter_guessed function.

def hangman_photos_maker():
    """Creates a dictionary for different Hangman statses in the game.
    :rtype: None 
    """
    HANGMAN_PHOTOS[6] = """    x-------x 
    
    
    
    
    """
    HANGMAN_PHOTOS[5] = """    x-------x
    |
    |
    |
    |
    |"""
    HANGMAN_PHOTOS[4] = """    x-------x
    |       |
    |       0
    |
    |
    |"""
    HANGMAN_PHOTOS[3] = """    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
    HANGMAN_PHOTOS[2] = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""
    HANGMAN_PHOTOS[1] = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""
    HANGMAN_PHOTOS[0] = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
     
def print_intro():
    """Prints the intro to the game, and generates the secret word.
    :param base: base value
    :return: The chosen secret word for the game from the words list.
    :rtype: str
    """
    HANGMAN_ASCII_ART ="""     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                         __/ |                      
                        |___/ """

    print (HANGMAN_ASCII_ART)
    # Getting a file path and validating it using check_file_input function.
    file_path = check_file_input()
    # Getting an index and validating it using check_file_input function.
    index = valid_index_choice()   
    secret_word = choose_word(file_path, index) 
    print("\nLet's start!")
    print("\nGuess the secret animal\n")
    return secret_word

def check_file_input():
    """Validates that the text file exists and readable.
    :return: a valid file path.
    :rtype: str
    """
    import errno # Module used to check if the file exists
    import os.path # Used to Check the file extension.
    file_path = ""
    file_ext = ""
    while(True): # Loop that will run until a valid file path will be inserted.
        file_path = input("Please Enter the words file location: ")
        file_ext = os.path.splitext(file_path)[1]
        #validating that the player chose a text file.
        if(file_ext != ".txt"):
            print("\nYou can only choose a text file.\n")
        else:    
            try: # If we can open the file, the file path will be returned.
                textfile = open(file_path, 'r')
                textfile.close()
                return file_path
            # If there's an error, the error type will be printed.
            except IOError as e: 
                if(e.errno == errno.EACCES):
                    print("\nfile exists, but isn't readable.\n")
                elif(e.errno == errno.ENOENT):
                    print("\nfile does not exist\n")

def valid_index_choice():
    """Creates the hidden word for the player.
    :param secret_word: the secret word for the game. 
    :return: a valid index.
    :rtype: str
    """
    while(True):
        index = input("Enter index: ")
        if(index.isdigit() == True):
            return index
        else:
            print("Invalid input, index must be a whole number")

def choose_word(file_path, index):
    """ retruns a word from the text file according to the index given.
    :param file_path: the text file's path that the player typed. 
    :param index: a number indicates the location of a word in the text file.
    :type file_path: str
    :type index: str
    :return: a word from the text file, to be used as the hidden word.
    :rtype: str
    """
    with open(file_path, "r") as file:
        word_file_data = file.read()
        word_file_data = word_file_data.replace('\n', ' ')
        word_file_data = word_file_data.split(" ")
        # Adding an empty item to first slot of the list
        # in order to match the indexes to the locations in the text file.          
        word_file_data[:0] = " "    
        # Using modulu to enable an index bigger than the number of words.
        chosen_word = word_file_data[int(index) % (len(word_file_data)-1)]  
       
        return chosen_word
        
def print_hangman(num_of_tries):
    """Prints the photo of the current state of the Hangman.
    :param num_of_tries: the number of tries left for the player.
    :type num_of_tries: int
    :rtype: None 
    """
    print(HANGMAN_PHOTOS[num_of_tries]) 
    
def show_hidden_word(secret_word, old_letters_guessed):
    """Creates the hidden word for the player
    :param secret_word: the secret word for the game. 
    :param old_letters_guessed: the letters that the player already guessed.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: a list of the secret word letters, with hidden letters.
    :rtype: list
    """
    hidden_word_list = []    # The list will contain the hidden word.
    for letter in secret_word:
        if(letter in old_letters_guessed): 
            hidden_word_list.append(letter)
        else:
            hidden_word_list.append("__")  
    return hidden_word_list 
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ Checks if the letter guessed is correct, 
    and adds it to the list that contains all the guessed letters.
    :param letter_guessed: The letter that the player guessed. 
    :param old_letters_guessed: the letters that the player already guessed.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: String that indicates rather the guess was correct/wrong/invalid/
    or the letter was already guessed.
    :rtype: string
    """ 
    letter_guessed = letter_guessed.lower()
    #Checking that the input is valid, and was not guessed.
    if((letter_guessed.isalpha() == False) or (len(letter_guessed) > 1)):
        return "invalid"
    elif(letter_guessed.isascii() == False): # varifying the letter is English.
        return "invalid"
    elif(letter_guessed in old_letters_guessed):   
        return "already_chosen"
    #Since the input is valid, we add it to the old_letters_guessed.    
    old_letters_guessed.append(letter_guessed) 
    # checking if the guess is correct.
    if(letter_guessed in secret_word):   
        return "correct_guess"
    else:
        return "wrong_guess"    
        
def check_win(secret_word, old_letters_guessed):
    """Checks if the player guessed all letters and won.
   :param secret_word: the secret word for the game. 
   :param old_letters_guessed: the letters that the player already guessed.
   :type secret_word: str
   :type old_letters_guessed: list
   :return: True if the player, False if not.
   :rtype: bool
   """ 
    current_guess_status = show_hidden_word(secret_word, old_letters_guessed)
    for letter in current_guess_status:
        if(letter == "__"):
            return False 
    return True

def game_play():
    """ Starts a new game, and new rounds until the player wants to stop playing.
    :rtype: None
    """ 
    global secret_word
    want_to_continue = "1"
    MAX_TRIES = 6
    while want_to_continue == "1":
        num_of_tries = MAX_TRIES
        old_letters_guessed = []  # Resets the list before a new game.  
        secret_word = print_intro() # Prints a intro,and generates secret_word
        round_play(num_of_tries, secret_word, old_letters_guessed)
        want_to_continue = \
        input("Enter 1 to play again, "
        "enter any other key to exit: ")

def round_play(num_of_tries, secret_word, old_letters_guessed):
    """Plays a round of the game.
    :param num_of_tries: number of tries the player has.
    :param secret_word: the secret word for the game.
    :param old_letters_guessed: the letters that the player already guessed.
    :type num_of_tries: int
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if the player, False if not.
    :rtype: None
    """ 
    # The next 3 code lines used for clearing the screen.
    import os  
    want_screen_clear = '' 
    cls = lambda: os.system('cls')
    while num_of_tries >= 1:
        print_hangman(num_of_tries) 
        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        print(*hidden_word, sep = "    ") 
        print("\nYou have %s mistakes left\n" % num_of_tries)
        if(len(old_letters_guessed) >= 1):
        # Allows the player to clear the screen only after the first guess.
            want_screen_clear = \
            input("Enter c to clear screen, "
            "enter any other key to continue:\n ")
        if(want_screen_clear.lower() == 'c'):
            cls() 
            want_screen_clear = ""
            #Printing the current state of the game after screen clear:
            print_hangman(num_of_tries)    
            print(*hidden_word, sep = "    ")    
            print("\nYou have %s mistakes left\n" % num_of_tries)
        letter_guessed = input("Guess a letter: ")
        num_of_tries = \
        guess_result(num_of_tries, letter_guessed, old_letters_guessed)
        if(check_win(secret_word, old_letters_guessed) == True):
            hidden_word = \
            show_hidden_word(secret_word, old_letters_guessed)
            print(*hidden_word, sep = "    ") 
            print("\nYOU WIN!, GOOD JOB\n")
            return # Breaking the loop in order to start a new game.        
    print_hangman(num_of_tries)
    print("\nYOU LOST\n")   
    
def guess_result(num_of_tries, letter_guessed, old_letters_guessed):
    """verifys that the guess is valid, and returns its result.
    :param num_of_tries: number of tries the player has.
    :param letter_guessed: The letter that the player guessed. 
    :param old_letters_guessed: the letters that the player already guessed.
    :type num_of_tries: int
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: num_of_tries
    :rtype: int
    """ 
    guess_status = \
    try_update_letter_guessed(letter_guessed, old_letters_guessed) 
    while(guess_status == "invalid" or guess_status == "already_chosen"):
        if(guess_status == "invalid"):     
            print("X ")
            print("\nInvalid input\n")
        if(guess_status == "already_chosen"):
            print("X ")
            print("\nYou already chose this letter\n")
            print(*sorted(old_letters_guessed), sep="--->")
        print("\n")
        letter_guessed = input("Guess a letter: ")
        guess_status = \
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
    if(guess_status == "correct_guess"):
        print("\nGood guess!\n")
    elif(guess_status == "wrong_guess"):
        num_of_tries -= 1
        print("\n:(\n") 
    return num_of_tries


def main(): 
    global HANGMAN_PHOTOS
    HANGMAN_PHOTOS = {0:"",1:"",2:"", 3:"", 4:"", 5:"", 6:""}
    hangman_photos_maker()  #Generates the hangman photos dict.
    game_play()
    print("\nThank you for playing, goodbye!\n")
 
if __name__ == "__main__":
    main()






