# importing necessary librairies
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Defining the data to be divided for clustering.
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
        }

# Converting the data into pandas Dataframe
df = pd.DataFrame(Data, columns=['x', 'y'])

# Using the model to classify the data into three clusters.
kmeans = KMeans(n_clusters=3).fit(df)

# Graphically representing the clustering using matplotlib library.
plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float))
plt.show()
