import sqlite3
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""
cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'Charlie','Rakshith shetty',2022,'Kiran raj')")
cursor.execute("INSERT INTO movies VALUES(2,'ABCD','Varun',2015,'Prabhu dev')")
cursor.execute("INSERT INTO movies VALUES(3,'Bahubali','Prabhas',2017,'Raj mouli')")
cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
print(results)
print('Details of the movie in which Varun was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Varun'")
res = cursor.fetchall()
print(res)