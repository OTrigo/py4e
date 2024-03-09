score = input("Enter score: ")

try:
  score = float(score)
except:
  print("Score must be a number")
  quit()

if score >= 0.9 and score <= 1.0:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
elif score < 0.6:
  print("F")
else:
  print("Incorrect score")