#Climate App

from datetime import timedelta , datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
#Max Date and then base the query 12 months from that date
max_date = max(session.query(Measurement.date))
print(max_date)
print(max_date[0])
#Need to format the date nicely so it can go into our query
max_date_1 = max_date[0]
max_date_1 = dt.strptime(max_date[0], "%Y-%m-%d")
print(max_date_1)
one_year_ago_date = max_date_1 - timedelta(days=365)
print(one_year_ago_date)


app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    """Return a dict for temp and dates over the last year"""

    results = session.query(Measurement.date, Measurement.prcp).all()

    # Create a dictionary from the row data and append to a list of all dates/temps
    date_temps = []
    for date in results:
        temp_dict = {}
        temp_dict["date"] = date.date
        temp_dict["prcp"] = date.prcp
        date_temps.append(temp_dict)
        
    return(jsonify(date_temps))
        
        

    


@app.route("/api/v1.0/stations")
def stations():
    """Returns unique stations"""
    
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    stations = pd.DataFrame(engine.execute("SELECT distinct station from Measurement").fetchall()).to_dict()

    return(jsonify(stations))

#Climate App


@app.route("/api/v1.0/tobs")
def tobs():
    """Return temp and dates over the last year"""
    
    session = Session(engine)
    """Return a dict for temp and dates over the last year"""
    
    results = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date > one_year_ago_date).group_by(Measurement.date).order_by(Measurement.date).all()

    # Create a dictionary from the row data and append to a list of all dates/temps
    date_temps = []
    for date in results:
        temp_dict = {}
        temp_dict["date"] = date.date
        temp_dict["prcp"] = date.prcp
        date_temps.append(temp_dict)
        
    return(jsonify(date_temps))



if __name__ == "__main__":
    app.run(debug = True)