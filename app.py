# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Create our session (link) from Python to the DB
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

#################################################
# Flask Routes
#################################################