import random
import os

#print(random.randint(1,12))
os.system('cls')
overs = []
def predictScore():
    for x in range(0,50):
        runs = random.randrange(0,12)
        overs.append(runs)
        #print('Over ',x,'-',runs)        

predictScore();
score = sum(overs)
print('Total Score : ',score)
