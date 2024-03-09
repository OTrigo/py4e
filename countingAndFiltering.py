#For para contar

count = 0
sumValue = 0
array = [0,1,3,4,5,12,24,5,42,524,2,3,4,5,2,5,245,2,5,4524,52]

for item in array:
  count+=1
  
print(count)

count = 0

for item in array:
  count+=item
  
print(count)

count = 0

for item in array:
  count += 1
  sumValue += item
  
print("Average:", sumValue/count)

#For para filtrar

print('Before')
for value in [9,45,34,54,254,33,1234,54,35,4564,13]:
  if(value>20):
    print(value, " is a large number")
print('After')

#For para procurar

found = False
print('Before ', found)
for value in [1,2,3]:
  if value == 3:
    found = True
print('After ', found)