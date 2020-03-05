import random

alphabet = ['a', 'b', 'c']
wordLength = 4
wordsCount = 10

words = []
for word in range(wordsCount):
   string = ''
   for letter in range(wordLength):
      string += random.choice(alphabet)
   
   words.append(string)

print(words)
pattern = str(input('Wpisz wzorzec: '))
dictionary = { k: v for k, v in enumerate(pattern) if v != '*'}

print(dictionary)
output = []
for word in words:
   add = True
   for idx, value in dictionary.items():
      if word[idx] != value:
         add = False
         break
   if add == True: 
      output.append(word)

print(output)

