import shelve

shelfFile = shelve.open('My data')
cats = ['puszek','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()
