# Python: Flask

### Variables
    $env:FLASK_APP = "x.py"                     --> set the flask app to run
    $env:FLASK_RUN_PORT = xxxx                  --> set the port to run on
    $env:FLASK_ENV = "development"              --> set the environment to run in

### Virtual environment
    python -m venv venv                         --> create a virtual environment I
    pipenv install                              --> create a virtual environment II
    pipenv shell                                --> enter the virtual environment
    pipenv install x                            --> install x in the virtual environment

### `flask run`