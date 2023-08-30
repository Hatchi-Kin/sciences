# sciences
```
sciences
├── Dockerfile
├── app.py
├── dblp.json
├── docker-compose.yaml
├── readme.md --------------------> Vous êtes ICI
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
```

## Set-up:

Assurez vous d'avoir un projet avec cette structure.
(dézippez dblp.zip, j'ai pas réussi à uploader le json de 35mb dans github? wth)

pour construire et deployer le container, ouvrez un terminal et entrez:
```
docker-compose up --build -d
```
puis rendez-vous sur http://127.0.0.1:5000/

