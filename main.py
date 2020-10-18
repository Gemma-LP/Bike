bikecost = 2000
print("If a Motorbike costs £",bikecost,"and it's value decreses by 10% each year, the value will fall as follows:\n")

while (bikecost > 1000):
  print("£",bikecost)
  deduction = bikecost / 10
  bikecost = bikecost - deduction
else:
  print("\nAfter this point, the value of the motorbike falls below £1000.")