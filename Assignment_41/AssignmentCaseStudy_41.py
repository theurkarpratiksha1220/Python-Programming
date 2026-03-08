import math

# -------------------------------------------------------------------#
# ----------------------- Assignment 41 - Point 1 -------------------#
# -------------------------------------------------------------------#

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNeighborsClassifier():

    Border = "-" * 50

    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    print(Border)
    print("Assignment 41.1 - KNN Algorithm")
    print(Border)

    #------------- Accept user input -------------#

    X = float(input("Enter X coordinate: "))
    Y = float(input("Enter Y coordinate: "))

    new_point = {'X': X, 'Y': Y}

    #-------- Calculate Euclidean distance ---------#
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(Border)
    print("Calculated distances are : ")
    print(Border)

    for d in data:
        print(d)

    #--------------- Sort distances -----------------#
    sorted_data = sorted(data, key=lambda item: item['distance'])

    print(Border)
    print("Sorted data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

    #------------- Select K nearest neighbors ------------------#
    k = 3
    nearest = sorted_data[:k]

    print("\nNearest Neighbors:")

    for n in nearest:
        print(f"{n['point']} - Distance: {round(n['distance'],2)}")

    #------------- Majority Voting -------------------#
    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Name : ", d, "number of votes : ", votes[d])

    print(Border)

    predicted_class = max(votes, key=votes.get)

    print("\nPredicted Class:", predicted_class)

# -------------------------------------------------------------------#
# ----------------------- Assignment 41 - Point 2 -------------------#
# -------------------------------------------------------------------#

def KValueDemonstration():

    Border = "-" * 50

    print(Border)
    print("Assignment 41.2 - KNN Algorithm")
    print(Border)

    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    new_point = {'X': 2, 'Y': 2}

    print(Border)
    print("Prediction Results for Different K Values")
    print(Border)

    for k in [1, 3, 5]:

        #---------------- Calculate distance ----------------#
        for d in data:
            d['distance'] = EucDistance(d, new_point)

        #--------------- Sort distances -----------------#
        sorted_data = sorted(data, key=lambda item: item['distance'])

        #------------- Select K nearest neighbors & Majority Voting------------------#
        nearest = sorted_data[:k]
        
        votes = {}

        for neighbour in nearest:
            label = neighbour['label']
            votes[label] = votes.get(label, 0) + 1

        predicted_class = max(votes, key=votes.get)

        print("K =", k, "→", predicted_class)

# When K increases, more nearby points are used to decide the class.
# If many of those points belong to another class, the final prediction can change.


# -------------------------------------------------------------------#
# ----------------------- Assignment 41 - Point 3 -------------------#
# -------------------------------------------------------------------#

def StudentResultPrediction():

    Border = "-" * 50

    print(Border)
    print("Assignment 41.3 - KNN Algorithm")
    print(Border)

    print(Border)
    print("Student Pass/Fail Prediction")
    print(Border)

    data = [
        {'hours':2, 'attendance':60, 'result':'Fail'},
        {'hours':5, 'attendance':80, 'result':'Pass'},
        {'hours':6, 'attendance':85, 'result':'Pass'},
        {'hours':1, 'attendance':50, 'result':'Fail'}
    ]

    hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))

    new_point = {'X':hours, 'Y':attendance}

    #-------------- Calculate distances -------------------#
    for d in data:
        temp = {'X':d['hours'], 'Y':d['attendance']}
        d['distance'] = EucDistance(temp, new_point)

    #-------------- Sort distances -----------------------#
    sorted_data = sorted(data, key=lambda item: item['distance'])

    #------------- Select K nearest neighbors & Majority Voting------------------#
    # K = 3
    k = 3
    nearest = sorted_data[:k]

    votes = {}

    for n in nearest:
        label = n['result']
        votes[label] = votes.get(label,0) + 1

    predicted = max(votes, key=votes.get)

    print("\nPredicted Result:", predicted)


def main():
    MarvellousKNeighborsClassifier()
    print("\n")
    KValueDemonstration()
    print("\n")
    StudentResultPrediction()

if __name__ == "__main__":
    main()