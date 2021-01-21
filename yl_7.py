year = int(input('aasta: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, 'on liigaasta')
else:
    print(year, 'pole liigaasta')