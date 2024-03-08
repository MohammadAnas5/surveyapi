from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase with your configuration
cred = credentials.Certificate("researchsurvey-ca10f-firebase-adminsdk-6mc87-19e91e0f62.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://researchsurvey-ca10f-default-rtdb.firebaseio.com/'
})

# Our Flask routes and application logic go here

@app.route("/")
def homepage():
    return render_template("hybrid.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    try:
        data = request.json  # Assuming you're sending JSON data in the request
        ref = db.reference('/')  # Set the path to your data
        ref.push(data)
        msg = "Data added successfully"
    except Exception as e:
        print(e)
        msg = "Error adding data"

    return render_template("result.html", msg=msg) 

@app.route("/get_data")
def get_data():
    ref = db.reference('/')
    data = ref.get()
    return str(data)

@app.route("/submit")
def thanks():
    return render_template('thanks.html')

if __name__=="__main__":
    app.run(debug=True) 
