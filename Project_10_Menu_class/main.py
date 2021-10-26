from menu import Menu

main_menu = Menu()
main_menu.add("Open new account")
main_menu.add("Log into existing account")
main_menu.add("Help")
main_menu.add("Quit")
print(main_menu)

main_menu.remove("Help")
print(main_menu)

# insert the item into position 3
main_menu.insert("Withdraw money", 3) 
print(main_menu)
# if the position give is greater than the number of positions, then the item goes last.
main_menu.insert("Last option", 7) 
print(main_menu)

main_menu.insert("First option", 1)
print(main_menu)

# if the position given is less than 1, nothing is inserted
main_menu.insert("Invalid option", 0)
print(main_menu)

# get the current position of an item
pos = main_menu.position("Withdraw money")
print(pos)

# if not found, the position returned is 0
pos = main_menu.position("Not found")
print(pos)
