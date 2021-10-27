class Item:
    """
        This class will store name and category of a specific item.
    """
    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.category}"