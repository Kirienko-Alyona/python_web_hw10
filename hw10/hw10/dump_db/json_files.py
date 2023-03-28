from models import Author, Quote
import json
from db import session


def load_authors_from_file():
    with open('../dump_db/authors.json', mode='r') as file:
        res = file.read()
        data = json.loads(res)

    

    for record in data:
        
        author = Author(fullname=record['fullname'],
                        born_date=record['born_date'],
                        born_location=record['born_location'],
                        description=record['description'],
                        user_id = 1
                        )
        session.add(author)
        session.commit()



def load_quotes_from_file():
    with open('../dump_db/quotes.json', 'r') as file:
        res = file.read()
        data = json.loads(res)


    for record in data:

        if record['author'] == 'Alexandre Dumas fils':
            #Я про цей випадок пита в слак
            record['author'] = 'Alexandre Dumas-fils'

        author = (session.query(Author.id)
                  .filter(Author.fullname.contains(record['author']))
                  .first())
        try:
            quote = Quote(tags=record['tags'],
                           author_id=author[0],
                           quote=record['quote'])
            session.add(quote)
            session.commit()

        except AttributeError:
            print(f'I cant find author "{record["author"]}"')



if __name__ == '__main__':

    load_authors_from_file()
    load_quotes_from_file()