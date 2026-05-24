import random

def pick_random_ball():

    balls=['Red','Green','Blue']

    result=random.choice(balls)

    pro=balls.count(result)/len(balls)
    print('Probability of picking red ball is:',pro)

    if result=='Red':
        return 'Red ball was picked'
    else:
        return 'Better luck next time!'
    
res=pick_random_ball()
print(res)