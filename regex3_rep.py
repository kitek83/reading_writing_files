import re,os

def findRegex(regex,text):
    regex = re.compile(regex)
    findRegex = regex.findall(text)
    print(findRegex)

while True:
    dirs = input('Enter the patch of folder for searching the expression:')
    if os.path.exists:
        print('Great, folder exists!')
        break

userExpression = input('Enter searched expression: ')
#creat list of the existinf file in the folder
listFiles = os.listdir(dirs)
#finding all txt files
for file in listFiles:
    if file.endswith('.txt'):
        #printing the patch of the file containing searched regex
        print(os.path.join(dirs,file))
        fileOpen = open(os.path.join(dirs,file),'r+')
        fileRead = fileOpen.read()
        findRegex(userExpression,fileRead)