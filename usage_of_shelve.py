import shelve

shelFile = shelve.open('myData')
myCats = ['Zophie','Pokie','Kristy']
#tricky saving the list to the dictionary 'cats'
shelFile['cats'] = myCats
shelFile.close()