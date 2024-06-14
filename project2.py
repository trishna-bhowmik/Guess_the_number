import random
randomNumber = random.randint(1,100)
userGauss = None
gausses = 0

while(userGauss != randomNumber):
    userGauss = int(input('Enter your gauss :'))
    gausses += 1
    if(userGauss==randomNumber):
        print('You gauss it right')
    elif userGauss > randomNumber:
        print('Gauss a small number')
    else:
        print('Gauss a large number')

print(f'The total number of turns you take is {gausses}')        
