from flask import Blueprint, render_template, request
from IkeaSecondHandApi import ikea_stores

ikea_api = Blueprint('ikea_api', __name__)

@ikea_api.route('/available_countries', methods=['GET'])
def available_countries():
    return render_template("blocks/dropdown.html.j2", items=ikea_stores.getAvailableCountries(), data_name="country")


@ikea_api.route('/available_stores', methods=['GET'])
def available_stores():
    if request.args.getlist("country"):
        country_list = request.args.getlist("country")
        return render_template("blocks/dropdown.html.j2", items=ikea_stores.getStoreIds(country_list), data_name="store")
    
    return render_template("blocks/dropdown.html.j2")