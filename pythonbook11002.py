import pythonbook11002a 
import random

answerwordlist = [ "dog" , "cat" , "bird" , "blue" , "red" , "sun" , "moon" ]
answerword = answerwordlist[random.randint(0,7)] 

pythonbook11002a.hangman( answerword )