def getTrinangle(n): 
   trinangle = []

   if n > 1:
      trinangle.append([1])

   for depth in range(1, n):
      lastRow = trinangle[-1]
      trinangle.append([1])

      for i in range(1, len(lastRow)):
         trinangle[depth].append(lastRow[i] + lastRow[i - 1])
      
      trinangle[depth].append(1)   
   
   values = []
   for row in trinangle:
      values.append(list(map(str, row)))
   
   return values 

def getCenterOfRow (row):
   out = " ".join(row)
   return (len(out) - 1) // 2

def pascal_trinangle(n):
   trinangle = getTrinangle(n)
   center = getCenterOfRow(trinangle[-1])
   outputString = ''

   for row in trinangle:
      outputString += ' ' * (center - getCenterOfRow(row))
      outputString += ' '.join(row)
      outputString += '\n'
   return outputString

print(pascal_trinangle(25))