#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

#load model
model =load_model("finalmalariya.h5")
modeltb =load_model("Tuberculosis.h5")
modelbr =load_model("finalmri.h5")
modelco =load_model("Covid19model.h5")
print('@@ Model loaded')


def pred_human_horse(horse_or_human):
  test_image = load_img(horse_or_human, target_size = (224,224)) # load image 50,50 for model111.h5 , 224,224 for el.h5
  #if there is any error come during loding of ek.h5 then use different input shape and finally put 224 input shape
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image).round(3) # predict class horse or human
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value
  acc=round(result[0][pred]*100,2)
  if pred == 0:
    return "infected",acc # if index 0 
  else:
    return "normal",acc # if index 1


#------------>>pred_human_horse<<--end
    
def tuber(horse_or_human):
  test_image = load_img(horse_or_human, target_size = (224,224)) # load image 50,50 for model111.h5 , 224,224 for el.h5
  #if there is any error come during loding of ek.h5 then use different input shape and finally put 224 input shape
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = modeltb.predict(test_image).round(3) # predict class horse or human
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value
  acc=round(result[0][pred]*100,2)
  if pred == 0:
    return "normal",acc # if index 0 
  else:
    return "Infected",acc # if index 1


def braintumor(horse_or_human):
  test_image = load_img(horse_or_human, target_size = (224,224)) # load image 50,50 for model111.h5 , 224,224 for el.h5
  #if there is any error come during loding of ek.h5 then use different input shape and finally put 224 input shape
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = modelbr.predict(test_image).round(3) # predict class horse or human
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value
  acc=round(result[0][pred]*100,2)
  if pred == 0:
    return "normal",acc # if index 0 
  else:
    return "infected",acc # if index 1



def covidfu(horse_or_human):
  test_image = load_img(horse_or_human, target_size = (224,224)) # load image 50,50 for model111.h5 , 224,224 for el.h5
  #if there is any error come during loding of ek.h5 then use different input shape and finally put 224 input shape
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = modelco.predict(test_image).round(3) # predict class horse or human
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value
  acc=round(result[0][pred]*100,2)
  if pred == 0:
    return "covid",acc # if index 0 
  else:
    return "normal",acc # if index 1







# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
#malaria template
@app.route("/malaria", methods=['GET', 'POST'])
def malaria():
        return render_template('malaria.html')
    
#tuberculosis template
@app.route("/tb", methods=['GET', 'POST'])
def tb():
        return render_template('tb.html')


#braintumor template
@app.route("/brain", methods=['GET', 'POST'])
def brain():
        return render_template('brain.html')



#covid template
@app.route("/covid", methods=['GET', 'POST'])
def covid():
        return render_template('covid.html')


@app.route("/predic", methods = ['GET','POST'])
def predic():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred = pred_human_horse(horse_or_human=file_path)
        pre ,e = pred_human_horse(horse_or_human=file_path)
        print(pre)
        print(e)
        if(pre=="normal"):
                return render_template('malu.html', pred_output = pred, user_image = file_path)
        else:
                return render_template('mali.html', pred_output = pred, user_image = file_path)
        
           
    
# tuberculosis call function:

@app.route("/tbi", methods = ['GET','POST'])
def tbi():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred = tuber(horse_or_human=file_path)
        pre ,e = tuber(horse_or_human=file_path)
        print(pre)
        print(e)
        if(pre=="normal"):
                return render_template('tbu.html', pred_output = pred, user_image = file_path)
        else:
                return render_template('tbi.html', pred_output = pred, user_image = file_path)
        

@app.route("/braini", methods = ['GET','POST'])
def braini():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred = braintumor(horse_or_human=file_path)
        pre ,e = braintumor(horse_or_human=file_path)
        print(pre)
        print(e)
        if(pre=="normal"):
                return render_template('braiu.html', pred_output = pred, user_image = file_path)
        else:
                return render_template('braini.html', pred_output = pred, user_image = file_path)
        

@app.route("/covidi", methods = ['GET','POST'])
def covidi():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred = covidfu(horse_or_human=file_path)
        pre ,e = covidfu(horse_or_human=file_path)
        print(pre)
        print(e)
        if(pre=="normal"):
                return render_template('covidi.html', pred_output = pred, user_image = file_path)
        else:
                return render_template('covidi.html', pred_output = pred, user_image = file_path)

        


         
#Fo local system
if __name__ == "__main__":
    app.run(debug=True) 
    
# #Fo AWS cloud
# if __name__ == "__main__":
#     app.run(host='0.0.0.0.0', post='8080',threaded=False,) 
    
    
    
    
    
    
    
    