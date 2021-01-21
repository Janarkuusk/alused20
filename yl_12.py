fruits = ['omena', 'banaani', 'kahvel']
print(fruits[0])
fruits.append('naine')
print(fruits[-1])
print(fruits[len(fruits)-1])
fruits[-2] = 'ogalik'
print(fruits)
if 'banaani' in fruits:
    print('Pirn on listis')

    print(len(fruits))
    fruits.remove('banaani')
    print(fruits)
