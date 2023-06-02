'''Basic script for Postgres database manipulation'''

import json, psycopg2

#retrieving basic data for login
data_file = open("config.json").read()
data = json.loads(data_file)

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host = data['host'],
        port = data['port'],
        user = data['user'],
        dbname = data['dbname'],
        password = data['password']
    )

    cursor = conn.cursor()


    create_script = '''
        CREATE TABLE IF NOT EXISTS student(
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR(30) NOT NULL,
            student_major VARCHAR(30) DEFAULT 'undecided',
            student_age INTEGER NOT NULL
        );
    '''

    read_script = '''SELECT * FROM student;'''

    insert_script = '''
        INSERT INTO student(student_name, student_major, student_age) VALUES(%s, %s, %s)
    '''
    script_values = ('Mike', 'Biology', 19)

    update_script = '''
        UPDATE student
            SET student_id = 1
            WHERE student_name = 'Mike';
    '''

    delete_script = '''
        DROP TABLE IF EXISTS student;
    '''

    #my_data = cursor.execute(insert_script, script_values)
    #my_data = cursor.execute(read_script)
    #my_data = cursor.execute(update_script)
    my_data = cursor.execute(delete_script)

    #print(cursor.fetchall())
    conn.commit()

except (Exception, psycopg2.Error) as err:
    print(err)

finally:

    #closing cursor
    if cursor is not None:
        cursor.close()
        print('cursor closed')

    #closing connection
    if conn is not None:
        conn.close()
        print('connection closed')
