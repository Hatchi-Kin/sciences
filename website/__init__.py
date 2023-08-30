from flask import Flask, render_template, url_for, request
from .data import Data


def create_app():

    app = Flask(__name__)


    @app.route('/', methods=['GET', 'POST'])
    def index():
        data = Data()
        all_titles = data.get_all_titles_and_authors()
        count = data.get_total_amount_articles()
        return render_template('index.html', all_titles=all_titles, count=count)
    


    @app.route('/sorted_by_date', methods=['GET', 'POST'])
    def sorted_by_date():
        data = Data()
        all_titles_date = data.get_all_titles_sorted_by_date()
        count = data.get_total_amount_articles()
        return render_template('sorted_by_date.html', all_titles=all_titles_date, count=count)
    


    @app.route('/sorted_by_author', methods=['GET', 'POST'])
    def sorted_by_author():
        data = Data()
        all_titles_date = data.get_all_titles_sorted_by_author()
        count = data.get_total_amount_articles()
        return render_template('sorted_by_date.html', all_titles=all_titles_date, count=count)
    


    @app.route('/details', methods=['GET', 'POST'])
    def details():
        clicked_title = request.args.get('title')
        data=Data()
        document_clicked = data.get_details_via_title(clicked_title)
        return render_template('details.html', document_clicked=document_clicked)
    


    @app.route('/pub_by_auth', methods=['GET', 'POST'])
    def pub_by_auth():
        if request.method == 'POST':
            searched_auth = request.form['searched_author']
            data = Data()
            publi_by_auth = data.get_all_articles_by_author(searched_auth)
            return render_template('pub_by_auth.html', publi_by_auth=publi_by_auth)
        else:
            return render_template('pub_by_auth.html')
        


    @app.route('/add_pub_to_auth', methods=['GET', 'POST'])
    def add_pub_to_auth():
        success = False
        if request.method == 'POST':
            title = request.form['title']
            authors = []
            authors.append(request.form['author'])
            year = request.form['year']
            data = Data()
            success = data.add_new_publication(title, authors, year)
            return render_template('add_pub_to_auth.html', success=success)
        else:
            return render_template('add_pub_to_auth.html')


    

    return app



