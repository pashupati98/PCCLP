import numpy as np
import pickle
import math

#print(pickle.__version__)
#print (math.__version__)
from sklearn import linear_model


# print('Running..')
#
# model = pickle.load(open("model_v3.0.pkl","rb"))
#
# print (model.predict([[4,0,0,1,0,0,0,0,2,1]]))


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 10)
    loaded_model = pickle.load(open("model_v3.0.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return int(math.floor(result[0]))
