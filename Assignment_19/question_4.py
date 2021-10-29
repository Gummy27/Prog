class Topping:
    def __init__(self, name, price) -> None:
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return self.__name

    def get_price(self):
        return self.__price

class Pizza:
    def __init__(self, name : str = "Unnamed", size : str = "large", toppings : list = []) -> None:
        self.name = name
        
        self.sizes_prices = {
            "small"  : 800,
            "medium" : 1200,
            "large"  : 1500
        }

        if size in self.sizes_prices:
            self.size = size
        else:
            raise ValueError("Invalid size of Pizza")

        self.toppings = toppings
    
    def __str__(self) -> str:
        if self.toppings:
            topping_string = ', '.join([str(topping) for topping in self.toppings])
        else:
            topping_string = "nothing"
        
        return f"{self.size.capitalize()} {self.name} pizza with {topping_string}"

    def add_topping(self, topping: object) -> None:
        self.toppings.append(topping)
    
    def add_toppings(self, toppings: list) -> None:
        self.toppings += toppings

    def get_price(self) -> int:
        topping_price = 0
        for topping in self.toppings:
            topping_price += topping.get_price()
        
        return topping_price + self.sizes_prices[self.size]

pizza = Pizza()

expected = "Large Unnamed pizza with nothing"

actual = str(pizza)

assert actual == expected, f"\nActual: {actual}\nExpected: {expected}\n"