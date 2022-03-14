import pyinputplus as pyip

print('What kind of bread would You like?:')
bread = pyip.inputMenu(['wheat','white','sourdough'])
print('What kind of protein would You like?:')
protein = pyip.inputMenu(['chicken','turkey','hum','tofu'])

cheese = pyip.inputYesNo('Would You like cheese? Answer yes or no.')
if cheese == 'yes':
    print('What kind of cheese would You like: ')
    kindCheese = pyip.inputMenu(['cheddar','swizz','mozarella'])
sandwich = pyip.inputInt('How many sandwiches would Youy like?:', min=1)

