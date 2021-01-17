class Phrase:    
    def __init__(self, phrase):
        self.phrase = phrase
    
    
    def display(self, guesses):
        #displays the phrase to the user as dashes for letters, appending letters as they are guessed correctly
        display = []
        for letter in self.phrase:
            if letter in guesses:
                display.append(letter)
            elif letter == ' ':
                display.append(' ')       
            else:
                display.append('_')
        print(' '.join(display))

    
    def check_letter(self, guess):
        #checks to see if the letter selected by user matches a letter in the phrase               
        for letter in self.phrase:
            if guess == letter:                
                return True
        return False
              
        
    def check_complete(self, guesses):
        #checks to see if the whole phrase as been guessed 
        for letter in self.phrase:
            if letter not in guesses:
                return False                
        return True
        
