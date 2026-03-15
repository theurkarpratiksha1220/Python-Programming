import math

Border = "-"*40

#------------ Dataset ------------#
data = [6, 7, 8, 9, 10, 11, 12]

#------------  Number of elements ------------#
n = len(data)

#------------ Mean ------------#
mean = sum(data) / n
print(Border)
print("Mean is :", mean)
print(Border)

#------------ Variance ------------#
variance = sum((x - mean) ** 2 for x in data) / n
print(Border)
print("Variance is :", variance)
print(Border)

#------------ Standard Deviation ------------#
std_deviation = math.sqrt(variance)
print(Border)
print("Standard Deviation is :", std_deviation)
print(Border)
