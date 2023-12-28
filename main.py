import psycopg2

DATABASE = 'test_db'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '55555'

connection = psycopg2.connect(
    database=DATABASE,
    user=USER,
    host=HOST,
    password=PASSWORD,
    port=PORT,
)

cursor = connection.cursor()

# add data
# cursor.execute("INSERT INTO instructors(name) VALUES('Ban');")
for i in range(500):
    cursor.execute(f"INSERT INTO instructors(name) VALUES('Marta{i}');")
connection.commit()
# cursor.execute('select id, name from instructors;')
# result = cursor.fetchall()
# print(result)

cursor.close()
connection.close()

