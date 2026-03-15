import numpy as np
from sklearn.linear_model import LinearRegression

Border = '-'*50

#-------------- Dataset ----------------#
#-------------- StudyHours, SleepHours (Independent variable) --------------#
X = np.array([
    [1,7],
    [2,6],
    [3,7],
    [4,6],
    [5,8]  
])

#--------------  Marks (Dependent variable) --------------#
Y = np.array([50, 55, 60, 65, 70])

print(Border)
print("Values of Independent variables : X - ",X) 
print(Border)
print("Values of Dependent variables : Y - ",Y)
print(Border)

#-------------- Create Linear Regression model --------------#
model = LinearRegression()

#-------------- Train the model --------------#
model.fit(X, Y)

#-------------- Print coefficient and intercept --------------#
print(Border)
print("Coefficient for StudyHours is :", model.coef_[0])
print("Coefficient for SleepHours is :", model.coef_[1])
print(Border)
print("Intercept is :", model.intercept_)
print(Border)

#-------------- Predict marks for 6 study hours --------------#
hours = np.array([[6,7]])   # 6 StudyHours, 7 SleepHours
predicted_marks = model.predict(hours)

print("Predicted marks for 6 study hours :", predicted_marks[0])
print(Border)