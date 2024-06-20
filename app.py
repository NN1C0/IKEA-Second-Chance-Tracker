from flask import Flask, render_template, render_template_string, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from IkeaSecondHandApi import ikea_stores, second_chance_search
from utils import database_handler
from models.base import Base
from models.offers import Offers


app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = database_handler.get_database_uri()
db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        countries = request.form.getlist("country")
        stores = request.form.getlist("store")

        print(search_term, countries, stores)
        search_result = db.session.execute(db.select(Offers).where(Offers.store_id.in_(stores), Offers.title.like(f'%{search_term}%')))
    
    #results = second_chance_search.searchSecondChance()
    return render_template( 
        "blocks/search_results.html.j2",
        search_results=search_result
    )

@app.route('/available_countries', methods=['GET'])
def available_countries():
    return render_template("blocks/dropdown.html.j2", items=ikea_stores.getAvailableCountries(), data_name="country")


@app.route('/available_stores', methods=['GET'])
def available_stores():
    if request.args.getlist("country"):
        country_list = request.args.getlist("country")
        return render_template("blocks/dropdown.html.j2", items=ikea_stores.getStoreIds(country_list), data_name="store")
    
    return render_template("blocks/dropdown.html.j2")

if __name__ == '__main__':
    app.run(debug=True)