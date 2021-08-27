from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pickle

def load_data():
    
    iris = load_iris()
     
    X = iris.data
    y = np.array([iris.target_names[x] for x in iris.target])

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, x_test, Y_train, y_test


def train_model(x, y):
    
    model = LogisticRegression(max_iter=1000)
    model.fit(x, y)
    
    return model

def save_model(model, filename='final_model.sav'):
    pickle.dump(model, open('models/prediction/'+filename, 'wb'))


def load_model(filename='final_model.sav'):
    loaded_model = pickle.load(open('models/prediction/'+filename, 'rb'))
    return loaded_model