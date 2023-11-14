from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase with your configuration
cred = credentials.Certificate("researchsurvey-ca10f-firebase-adminsdk-6mc87-19e91e0f62.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://researchsurvey-ca10f-default-rtdb.firebaseio.com/'
})

# Your Flask routes and application logic go here

@app.route("/")
def homepage():
    return render_template("hybrid.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    try:
        data = request.json  # Assuming you're sending JSON data in the request
        print(data)
        ref = db.reference('/')  # Set the path to your data
        ref.push(data)
        msg = "Data added successfully"
    except Exception as e:
        print(e)
        msg = "Error adding data"

    return render_template("result.html", msg=msg) 

@app.route("/submit", methods=["POST"])
def submit_form():
    try:
        # Retrieve data from the JSON payload
        data = request.get_json()

        # Extract individual values from the data
        gender = data.get("gender")
        course = data.get("course")
        q3 = data.get("q3")
        q4 = data.get("q4")
        q5 = data.get("q5")
        q6 = data.get("q6")
        q7 = data.get("q7")
        q8 = data.get("q8")
        q9 = data.get("q9")
        q10 = data.get("q10")
        q11 = data.get("q11")
        q12 = data.get("q12")
        q13 = data.get("q13")
        q14 = data.get("q14")
        q15 = data.get("q15")
        q16 = data.get("q16")
        q17 = data.get("q17")

        # Perform any additional processing or validation as needed

        # Example: Save the data to a database (replace with your logic)
        # db.save_form_data(gender=gender, course=course, ...)

        # Return a success message
        msg = "Form data successfully submitted"
        return jsonify({"msg": msg})

    except Exception as e:
        # Handle exceptions and return an error message
        error_msg = f"Error processing form data: {str(e)}"
        return jsonify({"error": error_msg}), 500

@app.route("/get_data")
def get_data():
    ref = db.reference('/')
    data = ref.get()
    return str(data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5044) 
