import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(datapath):
    border = "-"*40

    #----------------------------------------------#
    #Step 1 : Load the dataset from CSV file
    #----------------------------------------------#

    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(datapath)

    print(border)
    print("Some entries from the dataase")
    print(df.head())
    print(border)

    #------------------------------------------------------#
    # Step 2 : Clean the dataset by removing empty fields
    #------------------------------------------------------#

    print(border)
    print("Step 2 : Clean the dataset by removing empty fields ")
    print(border)

    df.dropna(inplace=True)
    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])
    print(border)

    #------------------------------------------------------#
    # Step 3 : Separate Idependent and Dependent Variables
    #------------------------------------------------------#

    print(border)
    print("Step 3 : Separate Idependent and Dependent Variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :", X.shape)
    print("Shape of Y : ", Y.shape)

    print(border)
    print("Input columns : ", X.columns.tolist)
    print("Output Column : Class")
    
    #------------------------------------------------------#
    # Step 4 : Split the dataset for Training and Testing 
    #------------------------------------------------------#

    print(border)
    print("Step 4 : Split the dataset for Training and Testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Information of Training and testing Data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #------------------------------------------------------#
    # Step 5 : Feature Scaling
    #------------------------------------------------------#

    print(border)
    print("Step 5 : Feature Scaling")
    print(border)    

    Scalar = StandardScaler()
    
    #Independent Variables scalling
    X_train_scaled = Scalar.fit_transform(X_train)
    X_test_scaled = Scalar.fit_transform(X_test)

    print("Feature scaling is done")

    #------------------------------------------------------#
    # Step 6 : Explore the multiple values of K
    #------------------------------------------------------#

    print(border)
    print("Step 6 : Explore the multiple values of K")
    print(border) 

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(border)

    #------------------------------------------------------#
    # Step 7 : Find best value of K
    #------------------------------------------------------#

    print(border)
    print("Step 7 : Find best value of K")
    print(border) 

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ", best_k)

    #------------------------------------------------------#
    # Step 8 : Build final model using best value k 
    #------------------------------------------------------#

    print(border)
    print("Step 8 : Build final model using best value k ")
    print(border) 

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled, Y_train)
    Y_pred = final_model.predict(X_test_scaled)

    #------------------------------------------------------#
    # Step 9 : Calculate Final accuracy
    #------------------------------------------------------#

    print(border)
    print("Step 9 : Calculate Final accuracy ")
    print(border) 

    accuracy = accuracy_score(Y_test, Y_pred) 
    print("Accuracy of model is : ", accuracy*100)

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()