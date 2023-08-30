
from .connection import MongoAccess

class Data:

    def get_all_titles(self):
        client = MongoAccess.connexion()
        collection = client["publis"]
        everything = collection.find()
        all_titles = []
        for e in everything:
            all_titles.append(e['title'])
        MongoAccess.deconnexion()
        return all_titles
    

    def get_all_titles_and_authors(self):
        client = MongoAccess.connexion()
        collection = client["publis"]
        everything = collection.find()
        titles_and_authors = []
        for e in everything:
            titles_and_authors.append([e['year'], e['title'], e['authors']])
        return titles_and_authors
    

    def get_all_titles_sorted_by_date(self):
        client = MongoAccess.connexion()
        collection = client["publis"]
        documents = collection.find()
        titles_and_authors = [[int(doc['year']), doc['title'], doc['authors']] for doc in documents]
        sorted_titles_and_authors = sorted(titles_and_authors, key=lambda x: x[0], reverse=True)
        MongoAccess.deconnexion()
        return sorted_titles_and_authors
    

    def get_all_titles_sorted_by_author(self):
        client = MongoAccess.connexion()
        collection = client["publis"]
        documents = collection.find()
        titles_and_authors = [[doc['year'], doc['title'], doc['authors']] for doc in documents if doc['authors']]
        titles_sorted_by_author = sorted(titles_and_authors, key=lambda x: x[2][0].split()[-1], reverse=False)
        MongoAccess.deconnexion()
        return titles_sorted_by_author

    
    
    def get_total_amount_articles(self):
        client = MongoAccess.connexion()
        collection = client["publis"]
        count = collection.count_documents({})
        MongoAccess.deconnexion()
        return count
    


    def get_details_via_title(self, title):
        client = MongoAccess.connexion()
        collection = client["publis"]
        document = collection.find_one({"title": title})
        MongoAccess.deconnexion()
        return document


    def get_all_articles_by_author(self, author_name):
        client = MongoAccess.connexion()
        collection = client["publis"]
        documents = collection.find({"authors": {"$in": [author_name]}})
        # MongoAccess.deconnexion()
        return documents
    


    def add_new_publication(self, title, authors, year):
        client = MongoAccess.connexion()
        collection = client["publis"]
        document = {"title": title, "authors": authors, "year": year}
        result = collection.insert_one(document)
        MongoAccess.deconnexion()
        return result.inserted_id








# data = Data()
# all_titles = data.get_all_articles_by_author("Matthew W. Crocker")
# for t in all_titles:
#     print(t)



