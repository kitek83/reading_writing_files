import os
from pathlib import Path
homeFolder = r'C:/Users2/Kris'
subFolder = Path('spam')
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))
print()
print('-----------------')

print(Path.cwd())
os.chdir('C:\\windows')
print(Path.cwd())
print(Path.home())
print()
print('----------------')

#os.mkdir('C:\\Users2\\Kris\\PythonDir')
print(Path.cwd())
print(Path.cwd().is_absolute())
print()
print(Path('my/relative/patch'))
print(Path.cwd())
print(Path.home())
print()

print(Path.home() / Path('my/relative/patch'))