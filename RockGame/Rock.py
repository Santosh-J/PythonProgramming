from random import randint
player=input('rock(r),paper(p) or scissors(s)?')
print(player, 'vs')
choose=randint(1,3)
#print(choose)
if choose==1:
    computer='r'
elif choose==2:
    computer='p'
else:
    computer='s'

print(computer)

if player==computer:
    print('Draw!')
elif player=='r' and computer=='s':
    print('Player wins!')
elif player=='r' and computer =='p':
    print('Computer wins!')
elif player=='p' and computer=='r':
    print('Player wins!')
elif player == 'p' and computer == 's':
    print('Player wins!')
elif player == 's' and computer == 'r':
    print('Computer wins!')
elif player == 's' and computer == 'p':
    print('Player wins!')


