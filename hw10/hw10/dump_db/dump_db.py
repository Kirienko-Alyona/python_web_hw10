import json
from pprint import pprint
from psycopg2 import Error

from db_connection import connection 
# from ..mysite.app_mysite.models import Author, Quote

def seed_authors():
    path = r"C:\Users\Lenovo\Documents\Python-web\python_web_hw10\hw10\hw10\dump_db\json_files\authors.json" #+ filename + ".json"

    with open(path, encoding="utf-8") as f:
        text = f.read()
        myList = json.loads(text)
    for jsonObj in myList:
        
        app_mysite_author = [1, jsonObj['fullname'], jsonObj['born_date'], jsonObj['born_location'], jsonObj['description']]
        # app_mysite_author = ["1", "a", "1989-09-12", "c", "d"]
        # print(app_mysite_author)
        sql = """INSERT INTO app_mysite_author(id, fullname, born_date, born_location, description) VALUES(%s, %s, %s, %s);"""
        # k = zip(app_mysite_author)
        print(sql)
        c.executemany(sql, zip(app_mysite_author))
        

        
                





filenames = ["authors", "quotes"]


def create_collection():
    #for filename in filenames:
        #db[filename]
    path = r"C:\Users\Lenovo\Documents\Python-web\python_web_hw10\hw10\hw10\dump_db\json_files\authors.json" #+ filename + ".json"

    with open(path, encoding="utf-8") as f:
        text = f.read()
        myList = json.loads(text)
    return seed_authors(myList)
            #seed_authors(myList, filename)
            # for jsonObj in myList:
            #     if filename == "authors":
            #             app_mysite_author = [jsonObj['fullname'], jsonObj["born_date"], jsonObj["born_location"], jsonObj["description"]]
            #             sql = "INSERT INTO app_mysite_author(fullname, born_date, born_location, description) VALUES(%s, %s, %s, %s);"
            #             c.executemany(sql, zip(app_mysite_author))
                    # authors = Author(fullname=jsonObj['fullname'], born_date=jsonObj["born_date"],
                    #                  born_location=jsonObj["born_location"], description=jsonObj["description"])
                    # authors.save()
                # elif filename == "quotes":
                #     app_mysite_quote = [jsonObj['fullname']]
                #     sql = "INSERT INTO app_mysite_author(fullname) VALUES(%s);"
                #     c.executemany(sql, zip(app_mysite_author))
                    # authors = Author.objects(fullname=jsonObj["author"])
                    # quotes = Quote(tags=jsonObj["tags"], author=authors[0].id, quote=jsonObj["quote"])
                    # quotes.save()
    return


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        try:
            seed_authors()
            #create_collection()
            conn.commit()
            conn.rollback()
        except Error as error:
            pprint(error)
        finally:
            c.close()