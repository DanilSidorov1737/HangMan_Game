import random

correctguess = []
lowercaseword = []

y = ['''
         ____________________
         |  /     |
         | /     (_)
         |/     / | \ 
         |        |     
         |      /   \  
         | ____________________
       ''',
     '''
         ____________________
         |  /     |
         | /     (_)
         |/     / | \ 
         |        |     
         |       
         | ____________________
       ''',

     '''
    ____________________
    |  /     |
    | /     (_)
    |/       |  
    |        |     
    |        
    | ____________________
  '''
     ]

x = ['''
         ____________________
         |  /     |
         | /     (_)
         |/     / | \ 
         |        |     
         |      /   \  
         | ____________________
       ''',
     '''
         ____________________
         |  /     |
         | /     (_)
         |/     / | \ 
         |        |     
         |       
         | ____________________
       ''',
     '''
         ____________________
         |  /     |
         | /     (_)
         |/     / |  
         |        |     
         |           
         | ____________________
       ''',
     '''
    ____________________
    |  /     |
    | /     (_)
    |/       |  
    |        |     
    |        
    | ____________________
  ''',
     '''
    ____________________
    |  /     |
    | /     (_)
    |/        
    |             
    |           
    | ____________________
  ''', ]

while True:
    print("Made By Danil Sidorov and Finished on December 9, 2021")
    category = input("What category would you like to choose from: Baby Animals, States, and General?: ")

    if category.replace(' ', '').isalpha():
        if category == 'baby animals':
            baby = open("babyanimals.txt", "r")
            wordlist = baby.read()
            wordlist = wordlist.split()
            word = random.choice(wordlist)
            length = len(word)
            print(length, "letters")
            baby.close()

            difficulty = input('Select you difficulty [normal/hard]: ')
            if difficulty == "normal":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 5
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(x[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(x[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)

            elif difficulty == "hard":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 3
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(y[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(y[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)

            break

        elif category == 'states':
            states = open("states.txt", "r")
            wordlist = states.read()
            wordlist = wordlist.split('\n')
            word = random.choice(wordlist)
            word = ''.join(word)
            word = word.replace(" ", "")
            length = len(word)
            print(length, "letters")
            states.close()

            difficulty = input('Select you difficulty [normal/hard]: ')
            if difficulty == "normal":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 5
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(x[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(x[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)

            elif difficulty == "hard":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 3
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(y[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(y[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)

            break

        elif category == 'general':
            general = open("words.txt", "r")
            wordlist = general.read()
            wordlist = wordlist.split()
            word = random.choice(wordlist)
            length = len(word)
            print(length, "letters")
            general.close()

            difficulty = input('Select you difficulty [normal/hard]: ')
            if difficulty == "normal":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 5
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(x[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(x[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)

            elif difficulty == "hard":
                for letter in word:
                    lowercaseword.append(letter.lower())
                    word = lowercaseword

                blanks = "_" * len(word)
                guessed = False
                guessed_letters = []
                guessed_words = []
                count = 3
                print(blanks)
                while not guessed and count > 0:
                    guess = input("Guess a Letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        if guess in guessed_letters:
                            print("you already tried that")
                        elif guess not in word:
                            print("That is not in the word")
                            count -= 1
                            print(y[count])
                            guessed_letters.append(guess)
                        else:
                            print("Correct Guess")
                            guessed_letters.append(guess)
                            word_as_list = list(blanks)
                            indices = [i for i, letter in enumerate(word) if letter == guess]
                            for index in indices:
                                word_as_list[index] = guess
                            blanks = "".join(word_as_list)
                            if "_" not in blanks:
                                guessed = True
                            print(blanks)
                            word = ''.join(word)
                            while True:
                                choice = input("Would you like to guess the word (no spaces and lowercase) y/n: ")
                                if choice == 'y':
                                    guess = input("Guess the word: ")
                                    if guess != word:
                                        print("That word is incorrect")
                                        count -= 1
                                        print(y[count])
                                        break
                                    else:
                                        print("Congrats you guess the word!")
                                        blanks = word
                                        exit()
                                elif choice == "n":
                                    print("Ok!")
                                    break
                                else:
                                    print("Make sure you input is correct!")

                    else:
                        print("invalid input")
                    print(blanks)
                if guessed:
                    print("Good Job, you guessed the word!")
                else:

                    print("I'm sorry, but you ran out of tries. The word was ")
                    word = ''.join(word)
                    print(word)


            break

        else:
            print("Make sure you spelled it correctly")

    else:
        print("Make sure you did not put anything but letters into the input")
