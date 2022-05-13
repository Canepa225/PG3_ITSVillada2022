import pymysql

miConexion = pymysql.connect(
    host="localhost", user="canepa", passwd=".igna1221", db="Practico0_Ej1"
)
cur = miConexion.cursor()
try:
    cur.execute("SELECT * FROM Control")
    print(cur.fetchall())
except pymysql.err.ProgrammingError as e:
    print("Error en el comando!!!!!")
    print(e)

miConexion.close()