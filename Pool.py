import pymysql as Mysql

def ConnectionPooliing():
   DB=Mysql.connect(host="localhost",port=3306,user='root',passwd='somil',database='medassist_com',cursorclass=Mysql.cursors.DictCursor)
   CMD=DB.cursor()
   return DB,CMD