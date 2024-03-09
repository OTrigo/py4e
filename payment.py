hours = input("Enter Hours Worked: ")
rate = input("Enter Rate: ")

MAX_HOURS = 40
ADDITIONAL_VALUE_PER_HOUR = 1.5

try:
  hours = float(hours)
  rate = float(rate)

except:
  print("Hours or Rate must be a number")
  quit()
  
if(hours > MAX_HOURS):
  bonusRatePerHour = (hours - MAX_HOURS) * (rate * ADDITIONAL_VALUE_PER_HOUR)
  finalValue = MAX_HOURS*rate + bonusRatePerHour
  print("Final Value: ", finalValue)
else:
  finalValue = hours * rate
  print("Final Value: ", finalValue)