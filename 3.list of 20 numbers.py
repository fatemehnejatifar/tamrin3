import math
number_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number_2=[]

for number in range(len(number_1)):
    number_2.append(math.pow(number_1[number],2))

print('1 to 20',number_1)
print('1 to 20 power of two',number_2)