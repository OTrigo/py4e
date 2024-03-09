largest = None
smallest = None

def check_if_is_larger(num_input, largest):
  if largest is None:
      return num_input
  else:
      return num_input if num_input > largest else largest
    
def check_if_is_smaller(num_input, smallest):
  if smallest is None:
    return num_input
  else:
    return num_input if num_input < smallest else smallest

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    else:
        try:
          number = int(number)
          largest = check_if_is_larger(number, largest)
          smallest = check_if_is_smaller(number, smallest)
        except:
          print("Invalid input")
    print(largest)
    print(smallest)

print("Maximum", largest)
print("Minimum", smallest)