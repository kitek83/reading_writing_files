from pathlib import Path
import os

calcFIlePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFIlePath))
print(os.path.dirname(calcFIlePath))
print(os.path.split(calcFIlePath))
print()
print('--------------------')
print(os.path.dirname(calcFIlePath), os.path.basename(calcFIlePath))

print(calcFIlePath.split(os.sep))
print()

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print()

print(os.listdir('C:\\Windows\\System32'))
print('================')
print('System32 size:',os.path.getsize('C:\\Windows\\System32'))
print()
print('##################')

totalSize = 0
for fileName in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', fileName))
print('Total size os folder System32: ',totalSize)