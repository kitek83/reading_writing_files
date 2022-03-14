from pathlib import Path
import os

print(os.path.abspath('path'))
print()
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print()
print(os.path.isabs(os.path.abspath('.')))
print()
print('---------')

p = Path('C:/Users2/Kris/account.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print('---------------------')
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
print(Path.cwd().parents[4])
print('-----------------------')
print()






























