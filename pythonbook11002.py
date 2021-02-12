import pythonbook11002a 
import random

answerwordlist = [ "dog" , "cat" , "bird" , "blue" , "red" ]
answerword = answerwordlist[random.randint(0,5)] 

pythonbook11002a.hangman( answerword )