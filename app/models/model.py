import pickle

with open("app/models/grid_search_logistic_model.pkl", "rb") as file:
    model = pickle.load(file)