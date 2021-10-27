from item import Item
from catalog import Catalog

item1 = Item("12 Angry Men", "Drama")

item2 = Item("The Godfather", "Crime")

item3 = Item("Schindler's List", "Biography")

item4 = Item("Pulp Fiction", "Crime")

catalog = Catalog('Films')

catalog.add(item1)

catalog.add(item2)

catalog.add(item3)

catalog.add(item4)

item4 = Item("Macbook Pro", "Mac")

item5 = Item("Macbook Air", "Mac")

item6 = Item("Lenovo ThinkPad", "Lenovo")

catalog2 = Catalog("Computers")

catalog2.add(item4)

catalog2.add(item5)

catalog2.add(item6)

combined_catalog = catalog + catalog2

actual = combined_catalog.__str__()

expected = "Catalog Films+Computers:\n\tName: 12 Angry Men, Category: Drama\n\tName: The Godfather, Category: Crime\n\tName: Schindler's List, Category: Biography\n\tName: Pulp Fiction, Category: Crime\n\tName: Macbook Pro, Category: Mac\n\tName: Macbook Air, Category: Mac\n\tName: Lenovo ThinkPad, Category: Lenovo"

assert actual == expected, f"\nExpected: {expected}\nActual: {actual}"