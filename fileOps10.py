import pprint

myCats = [{'name': 'Zophie','description':'chubby'},{'name':'Pookie','description':'fluffy'}]
print(pprint.pformat(myCats))
fileObject = open('myCats.py','w')
fileObject.write('catsv='+pprint.pformat(myCats) + '\n')
fileObject.close()