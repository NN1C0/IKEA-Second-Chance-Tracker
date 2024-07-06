from flask import Flask, render_template

from routes.routes_search import search_routes
from routes.routes_ikea_api import ikea_api

from Config.config import DEBUG

app = Flask(__name__)

app.register_blueprint(ikea_api)
app.register_blueprint(search_routes)

@app.route('/')
def index():
    return render_template('index.html.j2')

if __name__ == '__main__':
    app.run(debug=DEBUG)