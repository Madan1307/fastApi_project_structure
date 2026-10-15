import pandas as pd


def make_prediction(data,model):
    features=pd.DataFrame([data.model_dump()])
    prediction=int(model.predict(features)[0])
    return prediction

