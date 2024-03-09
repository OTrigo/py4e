numbers = [0, 1, 2, 978, 4, 5, 1000, 7, 8, 9]
biggestNumber = None

for number in numbers:
  if biggestNumber == None:
    biggestNumber = number
  else:
    if number > biggestNumber:
      biggestNumber = number
    
print(biggestNumber)
