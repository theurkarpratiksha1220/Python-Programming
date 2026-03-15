from sklearn.preprocessing import MinMaxScaler
import numpy as np

Border = '-'*40

#------------- Two points -------------#
point1 = np.array([10, 200, 3000])
point2 = np.array([20, 400, 6000])

#-------------  Euclidean distance before scaling -------------#
distance_before = np.linalg.norm(point1 - point2)

print(Border)
print("Distance before scaling is :", distance_before)
print(Border)

#-------------  Min-Max scaling -------------#
scaler = MinMaxScaler()
points_scaled = scaler.fit_transform([point1, point2])

#-------------  Euclidean distance after scaling ------------- #
distance_after = np.linalg.norm(points_scaled[0] - points_scaled[1])

print("Distance after scaling is:", distance_after)
print(Border)