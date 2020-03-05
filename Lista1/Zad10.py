from math import *

chart = []
for x in range(24):
   chart.append([])
   for y in range(80):
      chart[x].append(' ')

function = input("Podaj funkcje f(x) = ")
begin = eval(input("Podaj początek przedziału a = "))
end = eval(input("Podaj koniec przedziału b = "))

chartLen = end - begin
chartDivider = chartLen / 80

# Get all values
values = []
maximum = None
minimum = None
for idx in range(len(chart[0])):
   x = begin + idx * chartDivider
   exec('x=' + str(x))
   y = eval(function)
   if maximum == None:
      maximum = y
      minimum = y
   maximum = max(maximum, y)
   minimum = min(minimum, y)
   values.append(y)

if maximum == minimum:
   maximum = maximum + 5
   minimum = minimum - 5

# Get center
chartHeight = maximum - minimum
centerVert = -1
if maximum * minimum < 0:
   centerVert = abs(minimum) / chartHeight
   centerVert = round(centerVert * 24) - 1 
elif maximum * minimum == 0:
   centerVert = 0
   if minimum == 0:
      centerVert = 23
centerDiag = -1
if begin * end < 0:
   centerDiag = abs(begin) / chartLen
   centerDiag = round(centerDiag * 80) - 1 
elif begin * end == 0:
   centerDiag = 0
   if end == 0:
      centerDiag = 79

if centerVert != -1:
   for col in range(len(chart[centerVert])):
      chart[centerVert][col] = '-'
if centerDiag != -1:
   for row in range(len(chart)):
      chart[row][centerDiag] = '|'


# Print values
averageValue = round((maximum + minimum) / 2)
verticalDivider = chartHeight / 22

for idx, value in enumerate(values):
   pointsVert = centerVert - round(value / verticalDivider)
   chart[pointsVert][idx] = '*'

for row in chart:
   for col in row:
      print(col, end='')
   print()
