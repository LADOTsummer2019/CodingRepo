drink_dict = {'coke': 4,'sprite': 3,'water': 2}
snack_dict = {'chips':2, 'candy': 2, 'cookie': 3}

print('Vending Machine')
print('Choose a drink')
x = input()

if x == 'coke':
  print("Insert 4 coins")
  y = int(input())
  while y < drink_dict[x]:
    print("not enough money")
    y = y + int(input())
  print("Your {} is dispensed below".format(x))
  if y > drink_dict[x]:
    change = y - drink_dict[x]
    print("You received {} coins in change".format(change))
elif x == 'sprite':
  print("Insert 3 coins")
  y = int(input())
  while y < drink_dict[x]:
    print("not enough money")
    y = y + int(input())
  print("Your {} is dispensed below".format(x))
  if y > drink_dict[x]:
    change = y - drink_dict[x]
    print("You received {} coins in change".format(change))
else:
  print("Insert 2 coins for water")
  y = int(input())
  while y < drink_dict[x]:
    print("not enough money")
    y = y + int(input())
  print("Your {} is dispensed below".format(x))
  if y > drink_dict[x]:
    change = y - drink_dict[x]
    print("You received {} coins in change".format(change))