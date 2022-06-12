import sqlite3
import pandas as pd

url = 'https://raw.githubusercontent.com/Pectus-Finance/hiring-exercises/master/python-backend/expanses.csv'
sql_query = '''CREATE TABLE expanses (
            departments TEXT NOT NULL,
            project_name TEXT NOT NULL,
            amount TEXT NOT NULL,
            expanse_date TIMESTAMP NOT NULL,
            member_name TEXT NOT NULL
            );'''

# Db creation in sqlite
def create_db_creation():
    conn = None
    print('Creating db connection!!')
    try:
        conn = sqlite3.connect('database.db')
    except:
        print('Error creating DB')

    return conn

# Update table with expanses.csv
def update_table_with_csv_data():

    #create DB
    conn = create_db_creation()

    # create table
    create_table(conn)

    # Fetch data from csv
    dataset = fetch_csv_data()

    # insert values into DB
    try:

        for val in dataset:
            print(val)
            sql = ''' INSERT INTO expanses(departments,project_name,amount,expanse_date,member_name)
                VALUES(?,?,?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, val)
            conn.commit()
    except:
        print('Error inserting into DB')


# def create_db_creation():
#     conn = None
#     print('creating db!!')
#     try:
#         conn = sqlite3.connect('database.db')
#     except:
#         print('Error creating DB')

#     return conn

# expanses table creation
def create_table(conn):
    print('creating table!!')
    cur = conn.cursor()
    try:
        cur.execute(sql_query)
    except:
        print('Error creating table')
    
    conn.commit()

# get data from github expanses.csv
def fetch_csv_data():

    dataset = pd.read_csv(url)
    excel_data = dataset.values.tolist()

    return excel_data

# execute sql statements
def execute_cur(sql_query):

    conn = create_db_creation()
    cur = conn.cursor()
    data = cur.execute(sql_query)
    try:
        cur.execute(sql_query)
        data = cur.fetchall()
    except:
        print('Error creating table')
    
    conn.commit()
    return data

