import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn import tree

# Create a hypothetical dataset
data = {
    'Age': [25, 35, 45, 22, 32, 55, 28, 48, 65, 40],
    'Experience': [3, 7, 15, 1, 5, 20, 2, 12, 25, 10],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Masters'],
    'Profession': ['Engineer', 'Engineer', 'Engineer', 'Technician', 'Technician', 'Manager', 'Technician', 'Manager', 'Manager', 'Engineer']
}

df = pd.DataFrame(data)

# Convert categorical variable into dummy/indicator variables
df = pd.get_dummies(df, columns=['Education'])

# Separate features and target
X = df.drop('Profession', axis=1)
y = df['Profession']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Display classification report
print(classification_report(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(15,10))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=df['Profession'].unique())
plt.show()
