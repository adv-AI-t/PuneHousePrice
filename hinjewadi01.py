from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error,mean_absolute_error

# import xgboost as xgb
# import csv

from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_percentage_error, f1_score,roc_auc_score, r2_score, mean_absolute_error

dataset = pd.read_csv("hinjewadi_dataset_processed01.csv")

rent = dataset.pop("rent")

X_train,X_test,y_train, y_test = train_test_split(dataset.drop(["floor_number","gate_community","deposit_amt"],axis=1),rent,test_size=0.2,random_state=10)

model = RandomForestRegressor(n_estimators=75, max_depth=20, random_state=10)

model.fit(X_train,y_train)
















