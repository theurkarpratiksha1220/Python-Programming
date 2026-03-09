import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousAdvertise(DataPath):

    Border = "-"*50

    # ------------------------------------------ #
    # Step 1: Load Dataset
    # ------------------------------------------ #

    print(Border)
    print("Step 1: Load Dataset")
    print(Border)

    df = pd.read_csv(DataPath)
    print("First 5 records:\n", df.head())

    # ------------------------------------------ #
    # Step 2: Clean Dataset (remove unwanted columns)
    # ------------------------------------------ #

    print(Border)
    print("Step 2: Clean Dataset")
    print(Border)

    print("Shape before cleaning:", df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape after cleaning:", df.shape)

    # ------------------------------------------ #
    # Step 3: Check missing values
    # ------------------------------------------ #

    print(Border)
    print("Step 3: Check missing values")
    print(Border)

    print(df.isnull().sum())

    # Optionally fill missing numeric values with column mean

    df.fillna(df.mean(), inplace=True)

    # ------------------------------------------ #
    # Step 4: Display statistical summary
    # ------------------------------------------ #

    print(Border)
    print("Step 4: Statistical Summary")
    print(Border)

    print(df.describe())

    # ------------------------------------------ #
    # Step 5: Correlation matrix
    # ------------------------------------------ #

    print(Border)
    print("Step 5: Correlation Matrix")
    print(Border)

    print(df.corr())

    # ------------------------------------------ #
    # Step 6: Split Dataset into Independent and Dependent Variables
    # ------------------------------------------ #

    print(Border)
    print("Step 6: Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    # ------------------------------------------ #
    # Step 7: Split Dataset into Training and Testing sets
    # ------------------------------------------ #

    print(Border)
    print("Step 7: Train/Test Split")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    print(Border)
    print("Information of Training and testing Data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    # ------------------------------------------ #
    # Step 8: Create and train Linear Regression model
    # ------------------------------------------ #

    print(Border)
    print("Step 8: Train Linear Regression Model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # ------------------------------------------ #
    # Step 9: Test the model
    # ------------------------------------------ #

    print(Border)
    print("Step 9: Predict on Test Data")
    print(Border)

    Y_pred = model.predict(X_test)

    # ------------------------------------------ #
    # Step 10: Compare actual vs predicted
    # ------------------------------------------ #

    print(Border)
    print("Step 10: Actual vs Predicted Sales")
    print(Border)

    comparison = pd.DataFrame({
        "Actual Sales": Y_test.values,
        "Predicted Sales": Y_pred
    })
    print(comparison)

    # ------------------------------------------ #
    # Step  11: Evaluate Model
    # ------------------------------------------ #

    print(Border)
    print("Step 11: Model Evaluation")
    print(Border)

    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R2 Score: {r2:.2f}")

def main():
    MarvellousAdvertise("MarvellousAdvertising.csv")

if __name__ == "__main__":
    main()