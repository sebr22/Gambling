
# Load TF-DF
import tensorflow_decision_forests as tfdf
import pandas as pd
import tensorflow as tf

# Load a dataset in a Pandas dataframe.
train_df = pd.read_csv("output/0.csv")
test_df = pd.read_csv("output/1.csv")

# Convert the dataset into a TensorFlow dataset.
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label="Did_YOU_Win")
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_df, label="Did_YOU_Win")

# Train a Random Forest model.
model = tfdf.keras.RandomForestModel()
model.fit(train_ds)

# Summary of the model structure.
model.summary()

# Evaluate the model.
model.evaluate(test_ds)

# Export the model to a SavedModel.
model.save("forrester")

model = tf.keras.models.load_model('forrester')