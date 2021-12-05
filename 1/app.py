from flask import Flask, render_template, flash
from flask import request, jsonify, redirect

app = Flask(__name__)                                                       # App created

@app.route('/')                                                             # Decorator for showing the home page path
def home():
    return '<h1>Allen</h1>'                                                 # Return the html code

@app.route('/a')                                                            # Decorator for showing the 'a' page path
def a():
    return '''<h1>Allen</h1><br/>
    <h2>Contact me</h2>
    <b>9449277201, allenbphilip@gmail.com</b>'''                            # Return the html code

@app.route('/b')                                                            # Decorator for showing the 'b' page path
def b():
    return '''<h1>Allen</h1><br/>
    <h2>Occupation</h2>
    <i>Data Analyst at ZS</i>'''                                            # Return the html code

@app.route('/c')                                                            # Decorator for showing the 'c' page path
def c():
    return '''<h1>Allen</h1><br/>
    <h2>Website</h2>
    <a href="https://abphilip.me">Click Here</b>'''                         # Return the html code

@app.route('/alerts/create')                                                # Create page path
def create():
    return jsonify({'message':'Alert created successfully'})                # Return the json code      

@app.route('/alerts/delete')                                                # Delete page path
def delete():
    return jsonify({'message':'Alert deleted successfully'})                # Return the json code

countries = [                                                               # List of countries as data
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "India", "capital": "Delhi", "area": 3287259},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}    
]

def find_next_id():
    return max(country["id"] for country in countries) + 1                  # Return the next ID

@app.get("/countries")                                                      # To GET the countries data
def get_countries():
    return jsonify(countries)                                               # Return the data as JSON

@app.post("/countries")                                                     # To POST to countries data
def add_country():
    if request.is_json:                                                     # Check if the request data is JSON
        country = request.get_json()                                        # Parse JSON data
        country["id"] = find_next_id()                                      # Assign ID to new data
        countries.append(country)                                           # Append the data to the list   
        return country, 201                                                 # Return success code
    return {"error": "Request must be JSON"}, 415                           # Return the error message if not JSON

'''-----------------------------------------------------------------
    
    To add new data, send a POST request to the endpoint

    curl -i http://127.0.0.1:5000/countries \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"name":"Germany", "capital": "Berlin", "area": 357022}'

-----------------------------------------------------------------'''

if __name__ == "__main__":  
    app.run(debug=True)                                                     # Run the app in debug mode