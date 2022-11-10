"""Example of optimal parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    else:
        greeting += "Comp" + str(name)
    return greeting

# a single argument 
print (hello("Sally"))

# No argument
print(hello())

# int argument works
print(hello(110))