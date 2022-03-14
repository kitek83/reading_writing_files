from pathlib import Path
import os

p = Path('spam1.txt') #creating the file
p.write_text('Hello my King Kris')
print(p.read_text())

k = Path('hello.txt')
k.write_text('Hello my King Kris again.')
print()

helloFile = open('C:\\Users2\\Kris\\hello.txt','r')
print(helloFile.read())
print()

sonnetFile = open('C:\\Users2\\Kris\\sonnet29.txt','r')
for line in sonnetFile.readlines():
    print(line)
print('----------------------')

baconFile = open('bacon.txt','w')
baconFile.write('Hello my superior King Kris\n')
baconFile.write('Bacon is not a vegetable!')
content = baconFile.read()

baconFile.close()
print(content)

