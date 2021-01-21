a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Sellist kolmnurka ei eksisterri!')
elif a == b and b == c:
    print('Võrdhaarne kolmnurk')
elif a == b and b != c or a == c and a != b or b == c != a:
    print('Võrdhaarne kolmnurk')
else: 
    print('Erikülgne kolmnurk')