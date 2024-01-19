#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value= 123):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        if self.value and self.value[-1] == '.':
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value and self.value[-1] == '!':
            return True
        else:
            return False
    
    def is_question(self):
        if self.value and self.value[-1] == '?':
            return True
        else:
            return False
        
    def count_sentences(self):
        if hasattr(self, 'value'):
            sentences = re.split('[.!?]', self.value.strip())
            sentences = [s for s in sentences if s]
            return len(sentences)
        else:
            return 0
        

bike = MyString("123")
simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")