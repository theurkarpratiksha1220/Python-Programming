import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

Border = "*"*80
Border1 = "-"*80
print(Border)

#----------------------- 1 ------------------------#
# Display first 5 records
print("First 5 Records: ")
print(df.head())
print(Border1)

# Display last 5 records
print("\nLast 5 Records: ")
print(df.tail())
print(Border1)

# Display total number of rows and columns
print("\nTotal Rows and Columns: ")
print(df.shape)
print(Border1)

# Display list of column names
print("\nColumn Names: ")
print(df.columns.tolist())
print(Border1)

# Display data types of each column
print("\nData Types: ")
print(df.dtypes)

print(Border)

#----------------------- 2 ------------------------#

# Total number of students
Total_Students = len(df)
print("\nTotal Number of Students:", Total_Students)
print(Border1)

# Count how many students Passed (FinalResult = 1)
Passed_Students = (df['FinalResult'] == 1).sum()
print("Number of Students Passed:", Passed_Students)
print(Border1)

# Count how many students Failed (FinalResult = 0)
Failed_Students = (df['FinalResult'] == 0).sum()
print("Number of Students Failed:", Failed_Students)

print(Border)
#----------------------- 3 ------------------------#

# Average StudyHours
Avg_StudyHours = df['StudyHours'].mean()
print("\nAverage Study Hours:", Avg_StudyHours)
print(Border1)

# Average Attendance
Avg_Attendance = df['Attendance'].mean()
print("Average Attendance:", Avg_Attendance)
print(Border1)

# Maximum PreviousScore
Max_PreviousScore = df['PreviousScore'].max()
print("Maximum Previous Score:", Max_PreviousScore)
print(Border1)

# Minimum SleepHours
Min_SleepHours = df['SleepHours'].min()
print("Minimum Sleep Hours:", Min_SleepHours)

print(Border)
#----------------------- 4 ------------------------#

# Count distribution
Result_Counts = df['FinalResult'].value_counts()
print("\nDistribution of FinalResult:")
print(Result_Counts)

# Calculate total students
total_students = len(df)

# Calculate percentage manually
pass_count = Result_Counts[1]
fail_count = Result_Counts[0]

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("\nPass Percentage: {:.2f}%".format(pass_percentage))
print("Fail Percentage: {:.2f}%".format(fail_percentage))

# Check balance condition
print("\nDataset Balance Analysis:")

difference = abs(pass_percentage - fail_percentage)

if difference < 10:
    print("The dataset is balanced (Pass and Fail percentages are close).")
else:
    print("The dataset is imbalanced (One class significantly dominates).")

print(Border)
#----------------------- 5 ------------------------#

# Compare average StudyHours for Pass and Fail students
Study_Analysis = df.groupby('FinalResult')['StudyHours'].mean()
print("\nAverage Study Hours by Final Result:")
print(Study_Analysis)

print(Border1)

# Compare average Attendance for Pass and Fail students
Attendance_Analysis = df.groupby('FinalResult')['Attendance'].mean()
print("\nAverage Attendance by Final Result:")
print(Attendance_Analysis)

#Observation of point 5
#Students who passed (FinalResult = 1) generally have higher average StudyHours compared to students who failed. 
#Similarly, the average Attendance of passed students is higher than that of failed students. 
#Both higher StudyHours and higher Attendance improve the chances of passing.

print(Border)

#----------------------- 6 ------------------------#

plt.figure(figsize=(8,5))
plt.hist(df['StudyHours'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours per Day")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Observation of point 6
#This helps us understand the common study pattern in the dataset. If higher study hours are more frequent among passing students,
#it suggests studying more improves performance.

print(Border)

#----------------------- 7 ------------------------#

plt.figure(figsize=(8,6))

# Scatter plot with color by FinalResult
sns.scatterplot(
    data=df,
    x='StudyHours',
    y='PreviousScore',
    hue='FinalResult',         # Color by Pass/Fail
    palette={0: 'red', 1: 'green'},
    alpha=0.7
)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend(title='Final Result', labels=['Fail', 'Pass'])
plt.grid(True)
plt.show()

#Observation of point 7
#Students with higher previous scores and more study hours tend to pass.

print(Border)

#----------------------- 8 ------------------------#

plt.figure(figsize=(6,5))

sns.boxplot(y=df['Attendance'], color='skyblue')

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Observation of point 8
#Check for outliers (points outside whiskers). Some students may have unusually low or high attendance.

print(Border)

#----------------------- 9 ------------------------#

plt.figure(figsize=(8,6))

# Use boxplot to see distribution of assignments for Pass/Fail
sns.boxplot(x='FinalResult', 
            y='AssignmentsCompleted', 
            hue='FinalResult', 
            data=df,
            palette={0:'red', 1:'green'},
            legend=False)

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Observation of point 9
#The boxplot shows the number of assignments completed for Pass (green) and Fail (red) students.
#Students who passed generally completed more assignments, while students who failed completed fewer.

print(Border)

#----------------------- 10 ------------------------#

plt.figure(figsize=(8,6))

sns.boxplot(x='FinalResult', 
            y='SleepHours',
            hue='FinalResult',
            data=df,
            palette={0:'red', 1:'green'},
            legend=False)

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours per Day")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Observation of point 10
#The boxplot shows the distribution of sleep hours for Pass (green) and Fail (red) students.
#While students who passed may have slightly higher average sleep, there is considerable overlap between Pass and Fail students.
#Sleeping more does not guarantee success, but extremely low sleep might negatively affect performance.
#Success depends on a combination of factors like StudyHours, Attendance, AssignmentsCompleted, not just SleepHours.

print(Border)

