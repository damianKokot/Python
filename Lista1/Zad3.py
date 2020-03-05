def filterRepeat(table):
   output = []
   for item in table:
      if item not in output:
         output.append(item)
   return output

table = [1,1,2,2,2,3,3,5,5,5,4,4,4,0]
print(filterRepeat(table))