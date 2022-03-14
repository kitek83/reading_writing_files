import re
fileFind = open('madLib.txt', 'r')
text = fileFind.read()
if 'ADJECTIVE' or 'NOUN' or 'VERB' in text:
    textRep1 = re.compile(r'ADJECTIVE')
    word1 = input('Enter replacement for ADJECTIVE:')
    text = textRep1.sub(word1,text)
    print(text)

    textRep2 = re.compile(r'NOUN')
    word2 = input('Enter the replacement for the NOUN:')
    text = textRep2.sub(word2,text)
    print(text)

    textRep3 = re.compile(r'VERB')
    word3 = input('Enter replacement for the VERB:')
    text = textRep3.sub(word3,text)
    print(text)

    fileNew1 = open('madLibChanged1.txt','w')
    fileNew1.write(text)
    fileNew1.close()
else:
    print('ADJECTIVE or NOUN or VEREB were not found.')
fileFind.close()
