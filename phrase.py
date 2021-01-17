class Phrase:    
    def __init__(self, phrase):
        #recives phrase parameter and holds it in an instance attribute on the phrase object
        self.phrase = phrase
    
    
    def display(self, guesses):
        #prints out phrase to console with guessed letters visble and unguessed letters = _
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
        #chec to see if letter selected by user matches a letter in the phrase               
        for letter in self.phrase:
            if guess == letter:                
                return True
        return False
              
        
    def check_complete(self, guesses):
        #check to see if the whole phrase as been guessed 
        for letter in self.phrase:
            if letter not in guesses:
                return False                
        return True
        
