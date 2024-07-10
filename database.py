import pymysql

def conectarMySQL():
    host="TFG24.mysql.pythonanywhere-services.com"
    user="TFG24"
    clave="Grupo$24"
    db="TFG24$tienda_g24"
    return pymysql.connect(host=host,user=user,password=clave,database=db)

