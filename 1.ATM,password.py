password=1449
incorrect_password=9441
counter=0

while True:
    new_password=int(input('please enter your password:'))
    counter+=1
    
    if new_password==incorrect_password:
        print('you were verifyed by the police')
        break

    elif new_password<1000 or new_password>9999:
        print('your Password must be 4 digits')

    elif new_password==password:
        print('welcome\nyou are loged in')

    elif  counter==3 :
        print('your account is locked')
        break

    else:
        print('please try again')
