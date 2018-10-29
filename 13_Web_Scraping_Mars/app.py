#dependencies
from flask import Flask, render_template, redirect,  jsonify
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import scrape



app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection

@app.route('/')
def index ():
    mars_dict = list(db.collection.find())
    print(mars_dict)
    return render_template('index.html', mars_dict = mars_dict)


@app.route('/scrape')
def scrape_df ():
    mars_dict = scrape.scrape()
    db.collection.insert_one(mars_dict)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)






