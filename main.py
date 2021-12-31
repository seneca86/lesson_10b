# %%
from collections import namedtuple
Car = namedtuple('Car', 'model manufacturer topspeed')
viper = Car('Dodge', 'Viper', 230)
print(f'{viper.model=}, {viper.manufacturer=}, {viper.topspeed=}')
# %%
model3_ = {'model':'Model 3', 'manufacturer':'Tesla', 'topspeed': 250}
model3 = Car(**model3_)
print(f'{model3.model=}, {model3.manufacturer=}, {model3.topspeed=}')
diablo = Car(model='Diablo', manufacturer='Lamborghini', topspeed=325)
print(f'{diablo.model=}, {diablo.manufacturer=}, {diablo.topspeed=}')
# %%
modelX = model3._replace(model='Model X')
print(f'{modelX.model=}, {modelX.manufacturer=}, {modelX.topspeed=}')
# model3.name = 'Model Y'
# %%
class Gadget():
    def __init__(self, name):
        self.name = name
keyboard = Gadget('bluetooth keyboard')
keyboard.name
# %%
from dataclasses import dataclass
@dataclass
class GadgetDC:
    name: str
keyboard = GadgetDC('wired keyboard')
keyboard.name
# %%
@dataclass
class Computer:
    name: str
    manufacturer: str
    ram: int = 32

macbook = Computer('MacBook Pro', 'Apple', 64)
hp = Computer(name='HP Elitebook', manufacturer='HP')
macbook.name
hp.ram
# %%
