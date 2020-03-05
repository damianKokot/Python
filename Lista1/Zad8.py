romes = {
   'I': 1,
   'V': 5,
   'X': 10,
   'L': 50,
   'C': 100,
   'D': 500,
   'M': 1000
}

romeNumber = input('Podal liczbę rzymską: ')
value = 0
last = 'I'

for number in reversed(romeNumber):
   if romes.get(last) <= romes.get(number):
      last = number
      value += romes.get(number)
   else:
      value -= romes.get(number)

print(value)
