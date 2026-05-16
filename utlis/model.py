import joblib
import numpy 
from sklearn.preprocessing import PolynomialFeatures
import os



loaded_model = joblib.load('models/student_mark_model.pkl')


def Prediction(user_input=1):
    try:
        x_user_input_value = float(user_input)

        
        x_input = numpy.array(x_user_input_value).reshape(-1,1)
        poly = PolynomialFeatures(degree=2)

        x = poly.fit_transform(x_input)

        predicted_value = loaded_model.predict(x)
        value = predicted_value[0][0]

        return value
    
    except Exception as e:
        return str(e)
    


