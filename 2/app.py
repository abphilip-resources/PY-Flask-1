import json                                                                     # JSON handling
import os.path                                                                  # File handling
from werkzeug.utils import secure_filename                                      # Ensuring security of uploaded file 
from flask import Flask                                                         # Web app construction
from flask import request                                                       # Handling user I/O
from flask import redirect                                                      # URL Redirection
from flask import render_template                                               # Return a webpage
from flask import url_for                                                       # Return the URL for an object
from flask import flash                                                         # Alert messages
from flask import abort                                                         # Abort a request
from flask import session                                                       # Session handling for user
from flask import jsonify                                                       # Converting to JSON

app = Flask(__name__)                                                           # Name of the app
app.secret_key = 'Alvin333#'                                                    # Secret Key
loc = '/Users/allen/OneDrive/Desktop/Github/Learning/Python/Flask/2/'           # Directory

@app.route('/')                                                                 # Home Page
def home():
    return render_template('home.html', codes=session.keys())                   # Display home.html

@app.route('/user', methods=['GET','POST'])                                     # GET & POST methods accepted
def user():
    if(request.method=='GET'): return redirect(url_for('home'))                 # If GET, redirect to home page
    else:
        urls = {}                                                               # Dictionary to store URLs          
        if os.path.exists('urls.json'):                                         # If JSON file exists
            with open('urls.json') as urls_file:                                # Open file
                urls = json.load(urls_file)                                     # Load file into dictionary

        if request.form['code'] in urls.keys():                                 # If name already exists
            flash('''That short name has already been taken. 
                    Please select another name.''')                             # Flash Alert
            return redirect(url_for('home'))                                    # Redirect to home page

        if 'url' in request.form.keys():                                        # If URL
            urls[request.form['code']] = {'url':request.form['url']}            # Add URL to dictionary
        else:                                                                   # If file
            f = request.files['file']                                           # Get file from form
            n = request.form['code'] + secure_filename(f.filename)              # Check if secure file and name it
            f.save(loc + 'static/files/' + n)                                   # Save file to static/files
            urls[request.form['code']] = {'file':n}                             # Add file name to dictionary

        with open('urls.json','w') as url_file:                                 # Open file
            json.dump(urls, url_file)                                           # Dump dictionary into file
            session[request.form['code']] = True                                
        return render_template('user.html', code=request.form['code'])          # Display user.html for success

@app.route('/<string:code>')                                                    # The shortened URL code
def redirect_to_url(code):                              
    if os.path.exists('urls.json'):                                             # If JSON file exists   
        with open('urls.json') as urls_file:                                    # Open file
            urls = json.load(urls_file)                                         # Load file into dictionary
            if code in urls.keys():                                             # Iterate through dictionary
                if 'url' in urls[code].keys():                                  # If URL  
                    return redirect(urls[code]['url'])                          # Redirect to URL
                else:                                                           # If file
                    return redirect(url_for('static',                   
                    filename='files/' + urls[code]['file']))                     # Redirect to file
    return abort(404)                                                           # Throw 404 if not found in dictionary

@app.errorhandler(404)                                                          # 404 Error Page
def page_not_found(error):
    return render_template('404.html'), 404                                     # Render 404.html

@app.route('/api')                                                              # API Page
def session_api():
    return jsonify(list(session.keys()))                                        # Return JSON of session keys