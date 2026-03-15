from sklearn.preprocessing import StandardScaler
import numpy as np

Border = "-"*40

#--------- Dataset ---------#
data = np.array([[25, 20000],
                 [30, 40000],
                 [35, 80000]])

#--------- Initialize StandardScaler ---------#
scaler = StandardScaler()

#--------- Fit and transform the data ---------#
scaled_data = scaler.fit_transform(data)

#--------- Print the scaled dataset ---------#
print(Border)
print("Scaled Dataset is :")
print(scaled_data)
print(Border)