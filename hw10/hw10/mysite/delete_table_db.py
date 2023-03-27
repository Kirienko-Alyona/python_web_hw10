# ----- Example Python Program to remove a PostgreSQL database table 

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Start a PostgreSQL database session

psqlCon = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="5678")

psqlCon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

 

# Open a database cursor

psqlCursor      = psqlCon.cursor()

 

# Name of the table to be deleted

#tableName       = "app_mysite_quote"
tableName       = "app_mysite_author"

 

# Form the SQL statement - DROP TABLE

dropTableStmt   = "DROP TABLE %s;"%tableName

 

# Execute the drop table command

psqlCursor.execute(dropTableStmt)

 

# Free the resources

psqlCursor.close()

psqlCon.close()