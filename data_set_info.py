import pandas as pd
import matplotlib.pyplot as plt

train_df = pd.read_csv('Data/training_data.csv')
train_df.info()
print(train_df)
L = train_df.columns.values
print(L)

print("durations min max: ", min(train_df["duration"].values), max(train_df["duration"].values))
print("loudness min max: ", min(train_df["loudness"].values), max(train_df["loudness"].values))
print("tempo min max: ", min(train_df["tempo"].values), max(train_df["tempo"].values))
print("time_signature min max: ", min(train_df["time_signature"].values), max(train_df["time_signature"].values))

print("instrumentalness min max: ", min(train_df["instrumentalness"].values), max(train_df["instrumentalness"].values))
pd.plotting.scatter_matrix(train_df)
plt.show()

plt.hist(train_df["instrumentalness"])
plt.show()

train_df = pd.read_csv('Data/songs_to_classify.csv')
train_df.info()
print(train_df)
L = train_df.columns.values
print(L)

print("durations min max: ", min(train_df["duration"].values), max(train_df["duration"].values))
print("loudness min max: ", min(train_df["loudness"].values), max(train_df["loudness"].values))
print("tempo min max: ", min(train_df["tempo"].values), max(train_df["tempo"].values))
print("time_signature min max: ", min(train_df["time_signature"].values), max(train_df["time_signature"].values))
print("instrumentalness min max: ", min(train_df["instrumentalness"].values), max(train_df["instrumentalness"].values))
pd.plotting.scatter_matrix(train_df)
plt.show()

plt.hist(train_df["instrumentalness"])
plt.show()