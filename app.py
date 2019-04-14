# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Create our session (link) from Python to the DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    mars_data_all = mongo.db.mars_data_all.find_one()

    # Return template and data
    return render_template("index.html", mars_data_all=mars_data_all)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data_all =scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_data_all.update({}, mars_data_all, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)