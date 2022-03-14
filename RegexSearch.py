import re
import os
def regexSearch(regex,text):
    forRegex = re.compile(regex)
    result = forRegex.findall(text)
    print(result)

while True:
    dirs = input('Enter path of the folder you want to search:')
    if os.path.exists(dirs) == True:
        print('Folder exists!')
        break;
userSearch = input('Enter the regular expression you look for: ')
#creating the list of all files in the folder
files = os.listdir(dirs)

for file in files:
    if file.endswith('.txt'):
        print(os.path.join(dirs,file))
        fileOpen = open(os.path.join(dirs,file), 'r+')
        msg = fileOpen.read()
        regexSearch(userSearch,msg)

