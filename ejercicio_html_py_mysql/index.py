import mysql.connector
import cgi

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios1"
)

import cgi
form = cgi.FieldStorage()

name = form.getvalue("name")
mail = form.getvalue("mail")
passwd = form.getvalue("passwd")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM usuarios WHERE name = %s AND mail = %s", (name, mail))
tabla = mycursor.fetchone()
# ahora en el if le decimos (if tabla) es como decirle que me valide que existe esa fila en la tabla, seria equivalente a esto: tabla[1] == usuario y que el id exista
if tabla and tabla[2] == passwd:
 
        print("Usuario ", tabla[0], "ingresado")

mydb.commit()
