weight = int(input('Enter weight: '))
unit = input('Lbs or Kgs')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} lbs")