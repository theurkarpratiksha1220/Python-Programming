import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : X - ",X)
    print("Values of Dependent variables : Y - ",Y)

# -------------------------------------------------------------------#
# ----------------------- Assignment 42 - Point 1 -------------------#
# -------------------------------------------------------------------#

    #-------------------- Mean of X (X) and Mean of Y (Y) -------------------#

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is : ",mean_x)  
    print("Y_MEAN is : ",mean_y) 

    n = len(X)

    #-------------------- Slope(m) -------------------#

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    m = numerator / denominator

    print("Slope of line ie m : ",m)

    #-------------------- Intercept(m) -------------------#

    C = mean_y - (m * mean_x)

    print("Y intercept of line ie C : ",C)

    #-------------------- Simple Regression Line -------------------#
    x = np.linspace(1,6,n)
    y = C + m * x

    #------------------ Prediction for X = 6 ------------------------#
    x_new = 6
    y_pred = C + m*x_new
    print("Predicted Y for X=6:", y_pred)
    
# -------------------------------------------------------------------#
# ----------------------- Assignment 42 - Point 2 -------------------#
# -------------------------------------------------------------------#

    #------------------------ Model Performance ----------------------#

    print("\n------------------- Model Performance -----------------")

    #----------- 1. Predict all Y values using regression equation ------#
    Y_pred = []
    for xi in X:
        yi = C + m * xi
        Y_pred.append(yi)
    
    print("Predicted Y values for all X:", Y_pred)

    #-----------  2. Mean Squared Error (MSE) -----------#
    MSE = mean_squared_error(Y, Y_pred)
    print("Mean Squared Error (MSE) =", MSE)

    #-------------------  3. R^2 Score ---------------- #
    R2 = r2_score(Y, Y_pred)
    print("R^2 Score =", R2)

# -------------------------------------------------------------------#
# ----------------------- Assignment 42 - Point 3 -------------------#
# -------------------------------------------------------------------#

    print("\n--------------- Salary Prediction with Train-Test Split -----------------")

    # ---------------- Dataset ---------------- #
    data = {
        'Experience': [1, 2, 3, 4, 5],
        'Salary': [20000, 25000, 30000, 35000, 40000]
    }

    df = pd.DataFrame(data)

    # Split the data into X & Y
    X = df[['Experience']]
    Y = df['Salary']

    print("Independent variables : ", X.shape)
    print("Dependent variables : ", Y.shape)

    # Split the data for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, Y_train)

    # Predict on test data
    Y_pred = model.predict(X_test)

    # ---------------- Predict salary for 6 years experience ---------------- #
    salary_pred = model.predict(pd.DataFrame({'Experience':[6]}))[0]
    print(f"\nPredicted Salary for 6 Years Experience: Rupees {int(salary_pred)}")

    # ---------------- Plot regression line ---------------- #
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    plt.scatter(6, salary_pred, color='green', label='Prediction for 6 Years')
    plt.title("Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary (Rupees)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()