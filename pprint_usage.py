import pprint

myCats = [{'name':'Zophie','descrioption':'chubby'},{'name':'Pookie','description':'fluffy'}]
print(pprint.pformat(myCats))
myCatsFIle = open('myCapts.py','w')
myCatsFIle.write('cats=' + pprint.pformat(myCats) + '\n')
myCatsFIle.close()