# Named tuples

A named tuple is a subclass of tuple whose values can be accessed by name or position. You may think of it as an alternative to some simple classes.

It requires the function `namedtuple()`, which is part of the package `collections` and which has two arguments:
- The name
- A string of fields separated by spaces

```python
from collections import namedtuple
Car = namedtuple('Car', 'model manufacturer topspeed')
viper = Car('Dodge', 'Viper', 230)
print(f'{viper.model=}, {viper.manufacturer=}, {viper.topspeed=}')
```

We can also make a named tuple from a dictionary; we need the keyword argument preceded by `**` to _spread_ the keys and values from the dictionary and supply them as arguments to the named tuple. Alternatively, we can just provide the keyword-value pairs.

```python
# %%
model3_ = {'model':'Model 3', 'manufacturer':'Tesla', 'topspeed': 250}
model3 = Car(**model3_)
print(f'{model3.model=}, {model3.manufacturer=}, {model3.topspeed=}')
diablo = Car(model='Diablo', manufacturer='Lamborghini', topspeed=325)
print(f'{diablo.model=}, {diablo.manufacturer=}, {diablo.topspeed=}')
```

Named tuples are immutable, but we can create a modified tuple with the `replace` method.

```python
modelX = model3._replace(model='Model X')
print(f'{modelX.model=}, {modelX.manufacturer=}, {modelX.topspeed=}')
```

Because of immutability, the next assignment will not work.

```python
model3.name = 'Model Y'
```

In summary, named tuples are concide and effective, and share some similarities with dictionaries.

# Dataclasses

Many objects are created mainly for the attributes and not for the methods, i.e. they are created as a storage. Python 3.7 introduced _data classes_, let's see how they help is simplify a traditional object.

```python
class Gadget():
    def __init__(self, name):
        self.name = name
keyboard = Gadget('bluetooth keyboard')
keyboard.name
```

```python
from dataclasses import dataclass
@dataclass
class GadgetDC:
    name: str
keyboard = GadgetDC('wired keyboard')
keyboard.name
```

Besides the `@dataclass` decorator, note that we are using _variable annotations_ of the form `name: str` or `name: type = val`.

Let's try a slightly more complicated example.

```python
@dataclass
class Computer:
    name: str
    manufacturer: str
    ram: int = 32

macbook = Computer('MacBook Pro', 'Apple', 64)
hp = Computer(name='HP Elitebook', manufacturer='HP')
macbook.name
hp.ram
```
