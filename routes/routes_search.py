from flask import Blueprint, request, render_template
from sqlalchemy.orm import Session
from sqlalchemy import select
import logging

from models.offers import Offers
from utils import database_handler

search_routes = Blueprint('search_routes', __name__)

@search_routes.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        countries = request.form.getlist("country")
        stores = request.form.getlist("store")
        try:
            db_engine = database_handler.getDatabaseEngine()

            with Session(db_engine) as db:
                print(search_term, countries, stores)
                search_result = db.execute(select(Offers).where(Offers.store_id.in_(stores), Offers.title.like(f'%{search_term}%')))
                return render_template( 
                    "blocks/search_results.html.j2",
                    search_results=search_result
                )
        except Exception as e:
            logging.exception(e)
            return "500"