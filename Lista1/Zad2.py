def primes(n):
   if n <2:
      return

   numbers = []
   
   for number in range(n + 1):
      numbers.append(number)
   numbers[1] = 0

   for number in numbers:
      if number == 0:
         continue
      
      divider = number * number
      while divider <= n:
         numbers[divider] = 0
         divider += number

   return list(filter(lambda x: x != 0, numbers))

print(primes(6))
