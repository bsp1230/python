import test_mysql
import os

os.system('cls')
sql = test_mysql.mydb
cursor = sql.cursor()
cursor.execute("select * from scores LIMIT 15")
myresult = cursor.fetchall()

for x in myresult:
  print(x)