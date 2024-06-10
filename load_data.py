import json
from models import Author, Quote

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for author_data in authors:
            author = Author(**author_data)
            author.save()

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for quote_data in quotes:
            author = Author.objects(fullname=quote_data['author']).first()
            if author:
                quote = Quote(tags=quote_data['tags'], author=author, quote=quote_data['quote'])
                quote.save()

if __name__ == '__main__':
    load_authors('authors.json')
    load_quotes('qoutes.json')
