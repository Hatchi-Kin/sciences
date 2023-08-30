###########################################################
sciences
├── Dockerfile
├── app.py
├── dblp.json
├── docker-compose.yaml
├── readme.txt --------------------> Vous êtes ICI
├── requirements.txt
└── website
    ├── connection.py
    ├── data.py
    ├── static
    │   ├── w3-theme.css
    │   └── w3pro.css
    └── templates
        ├── add_pub_to_auth.html
        ├── base.html
        ├── details.html
        ├── index.html
        ├── pub_by_auth.html
        ├── sorted_by_author.html
        └── sorted_by_date.html
###########################################################

dans le dossier racine du projet, dezipper dblp.zip (pas réussi à upload un json de 35mb sit github wth)

ouvrir un terminal:
docker-compose up --build -d

puis copier l'id du container de mongodb:
docker ps

puis coller l'id dans:
docker cp dblp.json < id du container de mongodb >:/

puis:
mongoimport --db=DBLP --collection=publis --file=dblp.json -u root --host=localhost --port=27017 --authenticationDatabase admin

entrer le password pass12345

et enfin aller sur http://127.0.0.1:5000/
