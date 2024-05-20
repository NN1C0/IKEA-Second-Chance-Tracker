from flask import Flask, render_template, render_template_string, jsonify, request
from IkeaSecondHandApi import ikea_stores, second_chance_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/update', methods=['POST'])
def update():
    count = request.form.get('count', 0)
    new_count = int(count) + 1
    return render_template_string('<input name="count" id="count" value="{{value}}" />', value=new_count)

@app.route('/search', methods=['GET', 'POST'])
def search():
    print(request.form.to_dict())
    print(request.form.getlist("country"))
    print(request.form.getlist("store"))
    results = second_chance_search.searchSecondChance()
    return render_template()

@app.route('/available_countries', methods=['GET'])
def available_countries():
    return render_template("blocks/dropdown.html.j2", items=ikea_stores.getAvailableCountries(), data_name="country")


@app.route('/available_stores', methods=['GET'])
def available_stores():
    if request.args.getlist("country"):
        country_list = request.args.getlist("country")
        return render_template("blocks/dropdown.html.j2", items=ikea_stores.getStoreIds(country_list), data_name="store")

if __name__ == '__main__':
    app.run(debug=True)