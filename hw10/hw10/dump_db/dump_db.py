import json
from pprint import pprint
from psycopg2 import Error

from db_connection import connection 
from ..mysite.app_mysite.models import Author, Quote

filenames = ["authors", "quotes"]


def create_collection():
    for filename in filenames:
        #db[filename]
        path = r"./hw10/hw10/dump_db/json_files/" + filename + ".json"

        with open(path, encoding="utf-8") as f:
            text = f.read()
            myList = json.loads(text)
            for jsonObj in myList:
                if filename == "authors":
                    authors = Author(fullname=jsonObj['fullname'], born_date=jsonObj["born_date"],
                                     born_location=jsonObj["born_location"], description=jsonObj["description"])
                    authors.save()
                elif filename == "quotes":
                    authors = Author.objects(fullname=jsonObj["author"])
                    quotes = Quote(tags=jsonObj["tags"], author=authors[0].id, quote=jsonObj["quote"])
                    quotes.save()
    return


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        try:
            create_collection()
            conn.commit()
        except Error as error:
            pprint(error)
        finally:
            c.close()