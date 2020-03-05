def fraczero(n):
   result = 1
   for number in range(2, n + 1):
      result *= number
   
   result = str(result)
   
   zeros = 0
   for number in reversed(result):
      if number != '0':
         break
      zeros += 1

   return zeros

print(fraczero(100))
