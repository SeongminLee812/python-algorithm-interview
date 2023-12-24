original = {'roomL': 52000,
            'earth_star': 56000,
            'izakaya': 44000}

a = {key:val for key, val in original.items()}
print(a)

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

print(get_natural_number())
g = get_natural_number()
for _ in range(3):
    print(next(g))

a = range(100)
print(a[12])

b = list(range(100))
import sys

print((sys.getsizeof(a)))
print((sys.getsizeof(b)))


print('A1', 'B1')
print('A1', 'B1', sep='/')
a = ['A1', 'B1']
print(a)
print(' '.join(a))

import pprint
pprint.pprint(locals())

from dataclasses import dataclass

@dataclass
class Product:
    weight: int=None
    price: float=None

p = Product(22, 3.5)
print(p)
print(p.weight)

def string_option(S: float) -> None:
    print(S)

string_option(12.1213)