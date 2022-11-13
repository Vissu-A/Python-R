g = input('enter gender\n')
if g in ('m','f'):
    if g == 'm':
        age=int(input('enter your age\n'))
        if age < 18:
            print('you are a minor')
        elif 18 <= age <= 23:
            print('your are eligible to drink')
        else:
            print('your are ready to marry')

    elif g == 'f':
        age=int(input('enter your age\n'))
        if age < 18:
            print('your a minor')
        else:
            print('your are eligible to drink and marry')
else:
    print('you have enterded an invalid gender')