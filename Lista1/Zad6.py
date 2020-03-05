import random

randomNumbers = []
summary = 0

for probe in range(20):
   number = random.randint(1, 100)
   randomNumbers.append(number)
   summary += number

# Print list
print(randomNumbers)

# Print aveage value
print(summary / len(randomNumbers))

randomNumbers.sort()

# Print max and min
print("max: ", randomNumbers[-1])
print("min: ", randomNumbers[0])

# Print second max and second min
secondMax = 0
for number in reversed(randomNumbers):
   if number != randomNumbers[-1]:
      secondMax = number
      break
secondMin = 0
for number in randomNumbers:
   if number != randomNumbers[0]:
      secondMin = number
      break

print("second max: ", secondMax)
print("second min: ", secondMin)

# Prind pair numbers in list
evenCount = 0
for number in randomNumbers:
   if number % 2 == 0:
      evenCount += 1

print("Even numbers: ", evenCount)
