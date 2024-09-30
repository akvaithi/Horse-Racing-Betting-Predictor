import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, LeakyReLU

# Load your data (replace with your actual data loading)
data = pd.read_csv('horses_12.csv')


# Define features (X) and target variables (y)
X = data[['age', 'start', 'rating', 'weight']]
y = data[['first', 'podium', 'place']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the neural network model
model = Sequential()

model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))

model.add(Dense(3, activation='linear'))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.2)


model.save('horse_win_predictor_model.h5')  # Save the model for future use

data2 = pd.read_csv('Book1.csv')
model = load_model('horse_win_predictor_model.h5')  # Load the model

print(model.predict(data2))