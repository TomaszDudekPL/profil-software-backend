import sqlite3
import json
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_data(conn, arr):
    cur = conn.cursor()

    for obj in arr:

        gender = json.dumps(obj['gender'])
        title = json.dumps(obj['name']['title'])
        first = json.dumps(obj['name']['first'])
        last = json.dumps(obj['name']['last'])
        number = obj['location']['street']['number']
        name = json.dumps(obj['location']['street']['name'])
        city = json.dumps(obj['location']['city'])
        state = json.dumps(obj['location']['state'])
        country = json.dumps(obj['location']['country'])
        postcode = json.dumps(obj['location']['postcode'])
        latitude = obj['location']['coordinates']['latitude']
        longitude = obj['location']['coordinates']['longitude']
        offset = json.dumps(obj['location']['timezone']['offset'])
        description = json.dumps(obj['location']['timezone']['description'])
        email = json.dumps(obj['email'])
        uuid = json.dumps(obj['login']['uuid'])
        username = json.dumps(obj['login']['username'])
        password = json.dumps(obj['login']['password'])
        salt = json.dumps(obj['login']['salt'])
        md5 = json.dumps(obj['login']['md5'])
        sha1 = json.dumps(obj['login']['sha1'])
        sha256 = json.dumps(obj['login']['sha256'])
        date = json.dumps(obj['dob']['date'])
        age = obj['dob']['age']
        days_to_birthday = obj['dob']['days_to_birthday']
        reg_date = json.dumps(obj['registered']['date'])
        reg_age = obj['registered']['age']
        phone = obj['phone']
        cell = obj['cell']
        user_id_name = json.dumps(obj['id']['name'])
        user_id_value = json.dumps(obj['id']['value'])
        nat = json.dumps(obj['nat'])

        sql = """INSERT INTO persons VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});"""\
            .format(gender, title, first, last, number, name, city, state, country, postcode, latitude, longitude,
                    offset, description, email, uuid, username, password, salt, md5, sha1, sha256, date, age,
                    days_to_birthday, reg_date, reg_age, phone, cell, user_id_name, user_id_value, nat)

        cur.execute(sql)
    conn.commit()


def run_database(arr):
    database = r"persons.db"

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS persons (
[gender] VARCHAR NULL,
[name.title] VARCHAR NULL,
[name.first] VARCHAR NULL,
[name.last] VARCHAR NULL,
[location.street.number] INT NULL,
[location.street.name] VARCHAR NULL,
[location.city] VARCHAR NULL,
[location.state] VARCHAR NULL,
[location.country] VARCHAR NULL,
[location.postcode] INT NULL,
[location.coordinates.latitude] FLOAT NULL,
[location.coordinates.longitude] FLOAT NULL,
[location.timezone.offset] VARCHAR NULL,
[location.timezone.description] VARCHAR NULL,
[email] VARCHAR NULL,
[login.uuid] VARCHAR NULL,
[login.username] VARCHAR NULL,
[login.password] VARCHAR NULL,
[login.salt] VARCHAR NULL,
[login.md5] VARCHAR NULL,
[login.sha1] VARCHAR NULL,
[login.sha256] VARCHAR NULL,
[dob.date] VARCHAR NULL,
[dob.age] INT NULL,
[dob.days_to_birthday] INTEGER,
[registered.date] VARCHAR NULL,
[registered.age] INTEGER,
[phone] VARCHAR NULL,
[cell] VARCHAR NULL,
[id.name] VARCHAR NULL,
[id.value] VARCHAR NULL,
[nat] VARCHAR NULL
);"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        insert_data(conn, arr)

    else:
        print("Error! cannot create the database connection.")


def query_db(query):
    conn = create_connection(r'persons.db')
    c = conn.cursor()
    c.execute(query)
    all_rows = c.fetchall()
    c.close()
    conn.close()
    return all_rows
