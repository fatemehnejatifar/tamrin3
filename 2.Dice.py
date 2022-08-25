import random
total=0
while True:
    chance=random.randint(1,6)

    if chance==6:
        print('6\nlucky')
        total=total+chance
        continue
    else:
        total=total+chance
        print('total of numbres:',total)
        break
