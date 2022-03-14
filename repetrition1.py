import pprint

cats = [{'name':'Zophie','descr':'chubby'},{'name':'Pookie','descr':'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py','w')
fileObj.write('cats=' + pprint.pformat(cats) +'\n')
fileObj.close()
