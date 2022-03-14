from pathlib import Path
import os

p = Path('C:\\Users2\\Kris')
print(p.glob('*'))
for n in (list(p.glob('*'))):
    print(n)
print('Printing only txt file.')
print(list(p.glob('*.txt')))
print()

print(list(p.glob('details?.csv')))
print()
print('print all csv files')

for csv in list(p.glob('*csv')):
    print(csv)