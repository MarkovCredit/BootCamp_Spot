#dependencies
from flask import Flask, render_template, redirect,  jsonify
from flask_pymongo import PyMongo
import pymongo as pm
import scrape





client = pm.MongoClient('mongodb://localhost:27017/')


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def index ():
    
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)


@app.route('/scrape')
def scrape_df ():
    mars = mongo.db.mars
    mars_data = scrape.scrape()
    mars.update(
        {},
        mars_data,
        upsert = True
    )
    
    return redirect("/", code = 302)


if __name__ == "__main__":
    app.run(debug=True)






