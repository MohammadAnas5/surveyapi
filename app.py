from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase with your configuration
cred = credentials.Certificate("researchsurvey-ca10f-firebase-adminsdk-6mc87-19e91e0f62.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://researchsurvey-ca10f-default-rtdb.firebaseio.com/'
})

# Your Flask routes and application logic go here
from flask import request

# @app.route("/add_data", methods=["POST"])
# def add_data():
#     data = request.json  # Assuming you're sending JSON data in the request
#     # ref = db.reference('/path/to/your/data')  # Set the path to your data
#     ref = db.reference('/')
#     ref.push(data)
#     return "Data added successfully"

@app.route("/get_data")
def get_data():
    ref = db.reference('/')
    data = ref.get()
    return str(data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5044) 