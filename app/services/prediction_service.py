import pandas as pd


def make_prediction(data, model):
    features = pd.DataFrame([{
        "sepal_length": data.sepal_length,
        "sepal_width": data.sepal_width,
        "petal_length": data.petal_length,
        "petal_width": data.petal_width
    }])

    prediction = int(model.predict(features)[0])
    return prediction