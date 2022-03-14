import shelve

shelfFile = shelve.open('My data')
type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('My data')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))