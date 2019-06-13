import numpy
import pandas as pd
import sklearn
import csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics  
from pandas import DataFrame

dataset = pd.read_csv("Data\generaldata.csv")
X = dataset[['oil', 'usd']]
y = dataset['gas']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 1/3, random_state=0)  

regressor = LinearRegression()  
regressor.fit(X_train, y_train)  

# coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
# print(coeff_df)

y_pred = regressor.predict(X_test)  
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
# print(df)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', numpy.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()