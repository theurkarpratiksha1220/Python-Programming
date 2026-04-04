import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from io import StringIO

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Features for clustering
features = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted']
X = df[features]

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans clustering into 3 groups
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Map clusters to Top, Average, Struggling based on PreviousScore
centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers = pd.DataFrame(centers, columns=features)
sorted_clusters = cluster_centers.sort_values('PreviousScore', ascending=False).index.tolist()
cluster_mapping = {sorted_clusters[0]: 0, sorted_clusters[1]: 1, sorted_clusters[2]: 2}
df['Cluster'] = df['Cluster'].map(cluster_mapping)

# Add simple labels
labels = {0: "Top Performer", 1: "Average Student", 2: "Struggling Student"}
df['Performance Group'] = df['Cluster'].map(labels)

# Show results
print(df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','Performance Group']])