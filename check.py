dict1 = {'cake':'chocolate','cat':'pookie','car':'ferrari'}
print(dict1['cat'])
print(dict1['car'])
print()
print('======================')
list1 = ['Alabama','Oklahoma','New Jersy','New York']
print(list1.index('Oklahoma'))
print()

print(f"{'ABCD'}"[2])
text = 'EFGH'
print(text[0])
print()

for i in range(4):
    print(f"{'ABCD'}"[i])

cities = ['Szczecin', 'Wroclaw', 'Gdynia', 'Krakow']
print('--------------')
for i in range(4):
    print(f"{'ABCD'[i]}.{cities[i]}")