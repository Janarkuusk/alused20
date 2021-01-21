name = input('Nimi: ')
print('Tere', name.capitalize() + '!')

residence = input('Elukoht: ')
if 'saaremaa' in residence.lower():
    print('Sa oled pizdec', name.capitalize() + '!')

    age = int(input('Vanus: '))

    if age < 18:
        print('Ei tohi alkoholi pruukida!')
    elif age == 18:
        print('Palju õnne, joo edasi!')
    else:
        print('Tõmba nahuj!')




