#import pymysql
import  mysql.connector
try:
	conexion =  mysql.connector.connect(host='localhost',
                             user='root',
                             password='Elisea90',
                             db='dulceria')
	print("Conexión correcta")
except (mysql.err.OperationalError, mysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)