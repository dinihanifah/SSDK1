#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('model2.pkl','rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', quality=0)

@app.route('/predict', methods=['POST'])
def predict():
    fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol = [X for X in request.form.values()]
    
    data = []
    
    data.append(float(fixed_acidity))
    data.append(float(volatile_acidity))
    data.append(float(citric_acid))
    data.append(float(residual_sugar))
    data.append(float(chlorides))
    data.append(float(free_sulfur_dioxide))
    data.append(float(total_sulfur_dioxide))
    data.append(float(density))
    data.append(float(pH))
    data.append(float(sulphates))
    data.append(float(alcohol))
    
    prediction = model.predict([data])
    output = round(float(prediction[0]),2)
    return render_template('index.html', quality=output, fixed_acidity=fixed_acidity,volatile_acidity=volatile_acidity,citric_acid=citric_acid,residual_sugar=residual_sugar,chlorides=chlorides,free_sulfur_dioxide=free_sulfur_dioxide,total_sulfur_dioxide=total_sulfur_dioxide,density=density,pH=pH,sulphates=sulphates,alcohol=alcohol)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




