from flask import Blueprint, request, render_template
from sqlalchemy.orm import Session
from sqlalchemy import select
import logging

from IkeaSecondHandApi import second_chance_search
from models.offers import Offers
from utils import database_handler

search_routes = Blueprint('search_routes', __name__)

@search_routes.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        countries = request.form.getlist("country")
        stores = request.form.getlist("store")
        print(search_term, countries, stores)
        try:
            search_results = second_chance_search.searchLocalDatabase(search_term, stores)
            return render_template("blocks/search_results.html.j2", search_results=search_results)
        except Exception as e:
            logging.exception(e)
            return "Error retreiving search results"