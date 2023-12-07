python -m venv env
source env/Scripts/activate
pip install flask
pip install --default-timeout=1000 install tensorflow
pip install pillow
python app.py