#dependencies
from flask import Flask, render_template, redirect,  jsonify
import pymongo
import scrape


app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection

@app.route('/')
def index ():
    mars_df = list(db.collection.find())
    print(mars_df)
    return render_template('index.html', mars_df = mars_df)


@app.route('/scrape')
def scrape ():
    mars_df = scrape.scrape()
    db.collecition.insert_one(mars_df)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)






