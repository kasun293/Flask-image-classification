from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)



# Define a mapping of class indices to class names
class_mapping = {
    0: 'Common Indian Crow',
    1: 'Common Jay',
    2: 'Common Mime Swallowtail',
    3: 'Common Rose',
    4: 'Ceylon Blue Glassy',
    5: 'Great Eggfly',
    6: 'Lemon Pansy',
    7: 'Tailed Jay'
    # Add more class mappings as needed
}




model = load_model('Identification_model_.h5')
#model._make_predict_function()

def load_and_preprocess_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(100, 100))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize the image (assuming training involved normalization)
    return x

def predict_image_class(image_path,threshold=0.7):
    # Load and preprocess the image
    preprocessed_image = load_and_preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(preprocessed_image)

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions)

    # Get the predicted class name
    predicted_class_name = class_mapping.get(predicted_class_index, 'Unknown Class')

    # Get the highest predicted probability
    max_probability = np.max(predictions)

    # Check if the highest predicted probability is below the threshold
    if max_probability < threshold:
        predicted_class_name = 'Unknown'

    return predicted_class_name

# routes
@app.route("/", methods=['GET', 'POST'])
def kuch_bhi():
	return render_template("home.html")

@app.route("/about")
def about_page():
	return "About You..!!!"






@app.route("/submit", methods = ['GET', 'POST'])
def get_hours():
	if request.method == 'POST':
		img = request.files['my_image']
		img_path = "static/" + img.filename	
		img.save(img_path)
		predicted_class = predict_image_class(img_path, threshold=0.7)



	return render_template("home.html", prediction = predicted_class, image_path = img_path)





if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)