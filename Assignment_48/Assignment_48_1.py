import numpy as np

Border = "-"*40

#------------ Dataset ------------#
data = [6, 7, 8, 9, 10, 11, 12]

print(Border)
print("Dataset is : ", data)
print(Border)

#------------ Calculate mean ------------#
mean_value = np.mean(data)

print("Mean of the dataset is :", mean_value)
print(Border)