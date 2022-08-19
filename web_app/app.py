from flask import Flask, render_template, redirect, request, jsonify
from gbrModelHelper import GBRModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/about_thm")
def about_thm():
    # Return template and data
    return render_template("about_thm.html")

@app.route("/dashboard_one")
def dashboard_one():
    # Return template and data
    return render_template("dashboard_one.html")

@app.route("/dashboard_two")
def dashboard_two():
    # Return template and data
    return render_template("dashboard_two.html")

@app.route("/database")
def database():
    # Return template and data
    return render_template("database.html")

@app.route("/machine_learning")
def machine_learning():
    # Return template and data
    return render_template("machine_learning.html")


@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    # Return template and data
    content = request.json["data"]
    print(content)
    
    # parse
    metric = str(content["metric"])
    state_code = str(content["state_code"])
    year = int(content["year"])
    month = int(content["month"])
    day = int(content["day"])

    preds = GBRModelHelper.makePredictions(metric, state_code, year, month, day)
    return(jsonify({"ok": True, "prediction": str(preds)}))

# @app.route("/tableau")
# def tableau():
#     # Return template and data
#     return render_template("tableau2.html")

# @app.route("/makePredictions", methods=["POST"])
# def make_predictions():
#     content = request.json["data"]
#     print(content)
    
#     # parse
#     sex_flag = int(content["sex_flag"])
#     age = float(content["age"])
#     fare = float(content["fare"])
#     familySize = int(content["familySize"])
#     p_class = int(content["p_class"])
#     embarked = content["embarked"]

#     preds = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked)
#     return(jsonify({"ok": True, "prediction": str(preds)}))


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)