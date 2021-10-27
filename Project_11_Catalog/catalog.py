from item import Item

class Catalog:
    """
        This class will hold a catalog of different items. 
    """
    def __init__(self, name) -> None:
        self.name = name
        self.catalog = []

    def __str__(self) -> str:
        return_string = f"Catalog {self.name}:"

        for item in self.catalog:
            return_string += f"\n\t{str(item)}"
        
        return return_string
        
    def __add__(self, other):
        combined_catalog = self.catalog + other.catalog

        returned_catalog = Catalog(f"{self.name}+{other.name}")

        for item in combined_catalog:
            returned_catalog.add(item)

        return returned_catalog

    def add(self, item: Item) -> None:
        """
            This function appends a new item to the catalog.
        """
        self.catalog.append(item)

    def find_item(self, name_or_category: str) -> str:
        """
            This function gets a string as input and sees if we have
            that in our catalog. If true the item is returned, otherwise
            the function returns None.
        """
        for item in self.catalog:
            if item.name == name_or_category or item.category == name_or_category:
                return item
        return None

    def remove(self, remove_item: Item) -> None:
        """
            This function removes an item from the catalog.
        """
        remove_index = self.catalog.index(remove_item)
        self.catalog.pop(remove_index)
    
    def clear(self):
        """
            This function clears the catalog.
        """
        self.catalog = []

