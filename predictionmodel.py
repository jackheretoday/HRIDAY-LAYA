# Import Basic Libraries
import numpy as np
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Data Collection And Preprocessing
heart_data = pd.read_csv('/Users/jaykshirsagar/Desktop/Mini-Project_sem_4/HRIDAY-LAYA-main/heart.csv.xls')

heart_data.head()
heart_data.tail()
heart_data.shape
heart_data.info()
heart_data.isnull().sum()
heart_data.describe()
heart_data['target'].value_counts()

# 1 == defective heart 0 == healthy heart
# Splitting the features and target
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']
print(X)

print(Y)

# Splitting the data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

# Model Training
# Linear Regression Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Model Evaluation
# Predictions
X_train_prediction = model.predict(X_train)
X_test_prediction = model.predict(X_test)

# Mean Squared Error and R-squared
train_mse = mean_squared_error(Y_train, X_train_prediction)
test_mse = mean_squared_error(Y_test, X_test_prediction)

train_r2 = r2_score(Y_train, X_train_prediction)
test_r2 = r2_score(Y_test, X_test_prediction)

print("Training Data MSE:", train_mse)
print("Testing Data MSE:", test_mse)
print("Training Data R-squared:", train_r2)
print("Testing Data R-squared:", test_r2)

# Building a predictive system
input_data = (60, 0, 0, 100, 248, 0, 0, 122, 0, 1, 0, 0, 1)
# Change the input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)
# Reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if prediction[0] < 0.5:
    print("The Person Does Not Have a Heart Disease")
else:
    print("The person Has A Heart Disease")

model_filename = 'heart_disease_model.pkl'
joblib.dump(model, model_filename)

print(f"Model saved to {model_filename}")