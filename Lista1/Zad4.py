def prime_factors(n):
   factors = []

   for divider in range(2, n):
      power = 0
      while n % divider == 0:
         power += 1
         n /= divider
      
      if power != 0:
         factors.append((divider, power))

   return factors

#n = (3 ** 8) * (2 ** 5) * (5 ** 2)
n = 5248800
print(prime_factors(n))
