while True:

    option=int(input('choose:\n1)conerting hour to seconds\n2)converting seconds to hour\nplease enter your number:'))
    if option==1:

        hour=int(input('hours:'))
        minute=int(input('minutes:'))
        second=int(input('seconds:'))
        seconds=(hour*3600)+(minute*60)+second

        print(seconds,'second')
        break

    elif option==2:
        time = int(input("Input time in seconds: "))

        time = time % (24 * 3600)
        hour = time // 3600
        hour=time//3600
        time1=time-3600*hour
        minutes=time1//60
        seconds=time1-60*minutes

        print('hour:',hour,'minutes:',minutes,'seconde:',seconds)
        break
