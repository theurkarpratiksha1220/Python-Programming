import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y):

    print("\nChecking accuracy for different K values")

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    for k in range(1,6):

        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test, Y_pred)

        print("Accuracy for K =",k," is :",acc*100)


def MarvellousPlayPredictor(datapath):

    border = "-"*40

    # ------------------------------------------ #
    # Step 1 : Load Dataset
    # ------------------------------------------ #

    print(border)
    print("Step 1 : Load Dataset")
    print(border)

    data = pd.read_csv(datapath)

    print(data)

    # ------------------------------------------ #
    # Step 2 : Clean, Prepare and Manipulate data 
    #          Encode String Data
    # ------------------------------------------ #

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data ")
    print(border)

    print("Shape of Data before removing unwanted column : ", data.shape)

    #Data Cleaning - remove unwanted column 
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)                     

    print("Shape of Data after removing unwanted column : ", data.shape)

    print(border)
    print(data)
    print(border)

    # encoding the data
    encoder = LabelEncoder()

    for column in data.columns:
        data[column] = encoder.fit_transform(data[column])

    print("\nEncoded Data : ")
    print(data)

    # ------------------------------------------ #
    # Step 3 : Split Dataset into Independent and Dependent Variables
    # ------------------------------------------ #

    X = data[['Wether','Temperature']]
    Y = data['Play']

    print(border)
    print("Training Model")
    print(border)

    # ------------------------------------------ #
    # Step 4 : Train Model
    # ------------------------------------------ #

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    print(border)
    print("Information of Training and testing Data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train , Y_train)

    # ------------------------------------------ #
    # Step 5 : Test Data
    # ------------------------------------------ #

    print(border)
    print("Testing with new data")
    print(border)

    test = pd.DataFrame([[2,0]], columns=['Wether','Temperature'])
    result = model.predict(test)

    print("Predicted value : ", result)
    
    if result[0] == 1:
        print("Prediction : Yes, Play")
    else:
        print("Prediction : No, Don't Play")

    # ------------------------------------------ #
    # Step 6 : Accuracy
    # ------------------------------------------ #

    CheckAccuracy(X,Y)

def main():
    MarvellousPlayPredictor("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()