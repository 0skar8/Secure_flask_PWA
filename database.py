import sqlite3

conn = sqlite3.connect('LoginData.db')
cursor = conn.cursor()

cmd1 = '''CREATE TABLE IF NOT EXISTS USERS (first_name varchar(50),
                                        last_name varchar(50),
                                        email varchar(50) primary key,
                                        password varchar(50) not null)'''
cursor.execute(cmd1)

cmd2 = '''INSERT INTO USERS (first_name, last_name, email, password) values 
('tester', 'test', 'tester@gmail.com', 'testerP')'''
cursor.execute(cmd2)
conn.commit()

ans = cursor.execute("select * from USERS").fetchall()

for i in ans:
    print(i)