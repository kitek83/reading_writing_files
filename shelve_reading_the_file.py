import shelve

myFile = shelve.open('myData')
print(type(myFile))
print(myFile['cats'])
myFile.close()

