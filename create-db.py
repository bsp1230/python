import test_mysql
import os
#import Random
import random

os.system('cls')
sql = test_mysql.mydb
cursor = sql.cursor()
teams = ['INDIA','KENYA','AUSTRALIA','SOUTH AFRICA','SRI LANKA','ENGLAND','NEW ZEALAND','BANGLADESH','IRELAND','SCOTLAND','PAKISTAN','WEST INDIES']


#print(teams[i])

query = "INSERT INTO scores (score, team) VALUES (%s, %s)"
overs = []
def predictScore():
    for x in range(0,50):
        runs = random.randrange(0,9)
        overs.append(runs)
    return sum(overs)        
for x in range(0,70):
    i = random.randrange(0,12)   
    #print(i)
    score = predictScore();
    #print(score)
    record = [(score,teams[i])]
    print(record)
    overs.clear()
    cursor.executemany(query, record)
    sql.commit()
    print(x, "record inserted.")    



