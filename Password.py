pass1 = input()
pass2 = input()
if len(pass1) < 7:
    print('Short')
elif len(pass1) >= 7 and pass1 != pass2:
    print('Difference')
else:
    print('OK')
