from pathlib import Path
import os

windDir = Path('C:\\Windows')
nonExistingPath = Path('C:\\ThisFolder\\Dir')
calcFile = Path('C:\\Windows\\System32\\calc.exe')

print(windDir.exists())
print(windDir.is_dir())
print(windDir.is_file())
print()

print(nonExistingPath.exists())
print(nonExistingPath.is_dir())
print()

print(calcFile.exists())
print(calcFile.is_dir())
print(calcFile.is_file())