"""Examples of a class and object instantiation."""


class Pizza:
    """Models the idea of a pizza"""

    # Attribute def
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False


    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings
        #implicit return self
    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0 
        if self.size == "large":
            total += 10
        else:
            total += 8
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1

            total += tax

        return total

a_pizza: Pizza = Pizza("large", 3)
# a_pizza.size = "large"
# a_pizza.toppings = 3
# a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
# print(f"Price: ${price(a_pizza)}")
# method call \/
print(f"Price: ${a_pizza.price()}")
another_pizza: Pizza = Pizza("small, 0")
another_pizza.extra_cheese = True
print(a_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")
