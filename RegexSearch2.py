import re
import os

def regexSearch(regex,text):
    regexFile = re.compile(regex)
    findRegex = regexFile.findall(text)
    print(findRegex)

while True:
    dirs = input('Enter patch of the folder you want to look for: ')
    if os.path.exists(dirs) == True:
        print('Folder exists!')
        break;

inputSearch = input('Enter regular expression you look for: ')
fileList = os.listdir(dirs)

for file in fileList:
    if file.endswith('.txt'):
        print(os.path.join(dirs,file))
        openFile = open(os.path.join(dirs,file), 'r+')
        msg = openFile.read()
        regexSearch(inputSearch,msg)

