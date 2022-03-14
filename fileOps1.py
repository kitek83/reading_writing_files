from pathlib import Path
myFiles = ['account.txt','details.csv','invite.docx']
for fileName in myFiles:
    print(Path(r'c:\Users2\Kris',fileName))
print('---------------')
print()
homeFolder = r'C:\Users2\Kris'
subFolder = 'spam'

print(homeFolder + '\\' + subFolder)
print('\\'.join([homeFolder,subFolder]))
