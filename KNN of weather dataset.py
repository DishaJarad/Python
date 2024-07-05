import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Generate a synthetic weather dataset
# Features: Temperature and Humidity
# Labels: 0 for 'No Rain' and 1 for 'Rain'
np.random.seed(42)
temperature = np.random.randint(60, 100, 100)
humidity = np.random.randint(30, 80, 100)
labels = np.random.randint(2, size=100)

# Split the dataset into training and testing sets
X = np.column_stack((temperature, humidity))
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Visualize the decision boundary in a 2D graph
# Note: This is a simplified example and may not be suitable for all datasets
plt.figure(figsize=(10, 6))

# Plot data points
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='coolwarm', edgecolor='k', s=50)
plt.xlabel('Temperature')
plt.ylabel('Humidity')

# Plot decision boundary
h = 1  # step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)

plt.title('KNN Decision Boundary for Weather Dataset')
plt.show()
