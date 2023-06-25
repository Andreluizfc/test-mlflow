import pickle
import pandas as pd
import os

def predict(data):
    print(os.getcwd())
    pickled_model = pickle.load(
        open(
            "../../models/model_v1/model.pkl",
            "rb",
        )
    )
    final_features = pd.DataFrame(
        {
            "fixed acidity": data[0],
            "volatile acidity": data[1],
            "citric acid": data[2],
            "residual sugar": data[3],
            "chlorides": data[4],
            "free sulfur dioxide": data[5],
            "total sulfur dioxide": data[6],
            "density": data[7],
            "pH": data[8],
            "sulphates": data[9],
            "alcohol": data[10],
        },
        index=[0],
    )

    result = pickled_model.predict(final_features)

    return result

#curl -X POST -H "Content-Type: application/json" -d '{"data":[7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8]}' http://127.0.0.1:8080/predict