import pandas as pd

df=pd.read_csv('resources/final_data.csv')

## Import ML libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

import pickle

# Define our X and y features and split into training/test sets
df = pd.get_dummies(df,dtype=float)
df.head()

X = df.drop(['readmitted'], axis=1)
y = df['readmitted']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

X_train.head()

# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


lg = LogisticRegression(max_iter=1000)
lg.fit(X_train,y_train)

y_pred = lg.predict(X_test)
y_pred

# Saving model to disk
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(lg, open('logreg_model.pkl','wb'))