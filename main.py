import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password= "egorovartur",
    host="0.0.0.0"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close communications with database
cur.close()
conn.close()