import re
fileOpen = open('madLib.txt','r')
text = fileOpen.read()
if 'ADJECTIVE' or 'NOUN' or 'VERB' in text:
    textRegex1 = re.compile(r'ADJECTIVE')
    word1 = input('Enter replacement for the adjective:')
    text = textRegex1.sub(word1,text)
    print(text)

    textRegex2 = re.compile((r'NOUN'))
    word2 = input('Enter replacement for the NOUN')
    text = textRegex2.sub(word2,text)
    print(text)

    textRegex3 = re.compile((r'VERB'))
    word3 = input('Enter replacement for the VERB:')
    text = textRegex3.sub(word3,text)
    print(text)
    print()

    newFile = open('madLibChanged2.txt', 'w')
    newFile.write(text)
    newFile.close()
else:
    print('ADJECTIVE or NOUB or VERB was not dound.')
fileOpen.close()