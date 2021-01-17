import random
import sys


from phrase import Phrase


class Game: 
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('as you wish'), 
                           Phrase('the knights who say ni'), 
                           Phrase('you are a feisty little one'), 
                           Phrase('you shall not pass'), 
                           Phrase('candygram for mongo')]            
        self.active_phrase = self.get_random_phrase()        
        self.guesses = [' ']   
                
    
    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase       

    
    def welcome(self):
        print('\n', '\n')
        print(' ','=' * 25)
        print(' ','Welcome To Phrase Hunter!')
        print(' ','=' * 25, '\n','\n')
        print('\n','Guess the presented phrase, you can only make 5 wrong guesses.','\n','Good luck!''\n')    

        
    def get_guess(self):
        # Got the isalpha() from - https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python      
        guess = input('Enter the letter you would like to guess:  ')       
        if not self.active_phrase.check_letter(guess):
            print('Try again!')
            self.missed += 1            
            if len(guess) > 1:
                print('Please enter one letter at a time')
                self.missed -= 1
            elif len(guess) == 0:
                print('Please enter one letter at a time')
                self.missed -= 1
            elif not guess.isalpha():
                print('Incorrect character, please try a letter')
                self.missed -= 1
        elif guess in self.guesses:
            print('Opps, you already tried that one!')
        self.guesses.append(guess)
        return guess

    
    def start(self):
        self.welcome()
        while self.game_over() == False:
            self.active_phrase.display(self.guesses)
            print('\n')
            self.get_guess() 
            print('\n','You have made {} out of 5 incorrect guesses.'.format(self.missed),'\n')

            
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses) == True:
            print('Congratulations! You guessed the phrase!','\n')
            self.active_phrase.display(self.guesses)
            return True
        elif self.missed == 5:
            print('Bummer, you ran out of guesses! Maybe next time!','\n')
            return True
        else:
            return False

        
    def play_again(self):
        while True:
            try:
                play_again = input('Would you like to play again?(Y/N)  ')
                self.game_reset(play_again)                                    
            except TypeError:
                print('Try either Y/N')             
                play_again = input('Would you like to play again?(Y/N)  ')
                

    def game_reset(self, answer):
        if answer.lower() == 'y':
            print('Great, Here we go!')
            self.missed = 0
            self.active_phrase = self.get_random_phrase()        
            self.guesses = [' ']
            self.start()
        elif answer.lower() == 'n':
            sys.exit('Too bad! Thanks for playing!')
        else:
            print('Try either Y/N')             

