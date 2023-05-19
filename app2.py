#Import the libraries
import streamlit as st
import tensorflow as tf
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np

#Load the model
def load_model():
  model=tf.keras.models.load_model('my_model')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()
  
#Header
st.write("""
         # Pneumonia Prediction
         """
         )

#Prompt image upload
file = st.file_uploader("Please upload an brain scan file", type=["jpeg", "png"])

#Processing the image
st.set_option('deprecation.showfileUploaderEncoding', False)
def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction

#Displaying the results
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    class_names=['Normal','Pneumonia',]
    st.write('0 = Normal, 1 = Pnemonia')
    st.write(predictions)
    st.write(score)
    #print("This image most likely belongs to {} with a {:.2f} percent confidence."
    #.format(class_names[np.argmax(predictions)], 100 * np.max(score)))

    #string='Patient most likely to have: '+class_names[np.argmax(predictions)]
    #st.success(string)