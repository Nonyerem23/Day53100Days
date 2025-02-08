
import os, time

inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def add():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to add: > ").capitalize()
  inventory.append(item)
  print(f"{item} has been added to your inventory.")

def view():
  time.sleep(1)
  os.system("clear")
  print("Inventory")
  print("=========")
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)
  time.sleep(2)

def remove():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to remove: > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed from your inventory.")
  else:
    print(f"{item} is not in your inventory.")

while True:
  time.sleep(1)
  os.system("clear")
  print("RPG Inventory")
  print("=============")
  print()
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    remove()

  f = open("inventory.txt", "w")
  f.write(str(inventory))

  f.close()
