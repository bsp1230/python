import psycopg2
import random

pgadmin = psycopg2.connect(database = "testdb", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "root",
                        port = 5432)
print('connecting postgres...')
overs = []
teams = ['INDIA','KENYA','AUSTRALIA','SOUTH AFRICA','SRI LANKA','ENGLAND','NEW ZEALAND','BANGLADESH','IRELAND','SCOTLAND','PAKISTAN','WEST INDIES']
def predictScore():
    for x in range(0,50):
        runs = random.randrange(0,15)
        overs.append(runs)
    return sum(overs)     

cursor = pgadmin.cursor()
query = 'INSERT INTO scores(score, team) VALUES (%s,%s)'

for x in range(0,70):
    i = random.randrange(0,12)   
    #print(i)
    score = predictScore();
    #print(score)
    record = [(score,teams[i])]
    print(record)
    overs.clear()
    cursor.executemany(query, record)
    pgadmin.commit()
    print(x, "record inserted.")  
cursor.close()
pgadmin.close()