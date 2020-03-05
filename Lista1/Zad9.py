from math import *

while True:
   try:
      task = input('>>')
      print(round(eval(task), 10))
   except NameError:
      print("Podano niepoprawne dane")

