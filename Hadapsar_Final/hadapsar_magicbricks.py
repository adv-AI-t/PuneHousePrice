from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
import numpy as np

dataset = pd.read_csv("Hadapsar_Final.csv")

rent = dataset.pop("Rent")

model = RandomForestRegressor(n_estimators=100, max_depth=6, random_state=10, max_features='log2', min_samples_split=6, min_samples_leaf=3, bootstrap=True)

model.fit(dataset.drop(["Furnishing"],axis = 1),rent)

test = pd.read_csv("magictest.csv")


print(model.predict(test))
