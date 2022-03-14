import re,os

def findRegex(regex,text):
    regexFind = re.compile(regex)
    foundRegex = regexFind.findall(text)
    print(foundRegex)

while True:
    dirs = input('Enter pathe to the folder you want to look for: ')
    if os.path.exists(dirs):
        print('Great!The folder exists!')
        break
    else:
        print('Enter the correct path of the folder you look for:')
userRegex = input('Enter searched expression:')
#open the searched folder, make the list with the files from this folder
files = os.listdir(dirs)
#find all txt files in the folder dirs
for file in files:
    if file.endswith('.txt'):
# print path of seearched file
        print(os.path.join(dirs,file))
#open the searched file
        fileOopen = open(os.path.join(dirs,file),'r')
        msg = fileOopen.read()
        findRegex(userRegex,msg)
        fileOopen.close()




