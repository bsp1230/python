"""p1 = input('Sachin')
p2 = input('Dravid')
p3 = input('Laxman')
p4 = input('Sehwag')
p5 = input('Kohli')
p6 = input('Rohit')
p7 = input('Dhoni')"""
import datetime


players= [];
def match():
    for x in range(1,12):
       p = input('player: ')
       players.append(int(p))
    ip = input('Enter extras') 
    extras = int(ip) 
    score = sum(players)+extras 
    venue(); 
    print('Total Score : ',score)   
    avg = score / 50
    print('Run Rate : ',avg)
    print('Man of match : player',players.index(max(players)),'-',max(players))

def venue():
   date = datetime.datetime.now()
   print('------INDIA vs KENYA------')
   print('Date : ',date)
     
match();        
        