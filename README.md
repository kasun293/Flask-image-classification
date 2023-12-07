Setup virtual environment in your project directory

$python -m venv env

Activate the virtual environment

$source env/Scripts/activate

install requirements

$pip install flask
$pip install --default-timeout=1000 install tensorflow
$pip install pillow

Run the Flask app

$python app.py

Deactivate virtual environment

$deactivate
