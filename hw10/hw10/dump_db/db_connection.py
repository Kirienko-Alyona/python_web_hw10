from contextlib import contextmanager

from psycopg2 import connect, Error


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host="localhost", user="postgres", database="postgres",
                       password="5678")
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()