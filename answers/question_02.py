import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Andres','James','David','Vin','Steve','David','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)

"""
Write a function that takes df (defined above) as input and returns tuple with 3 values:
   - Most common name (string)
   - Average age (float)
   - IQR of rating (float)

Notes:
   - Average age and IQR must be float not numpy.float64 type
"""


def compute_statistics(df):
    "IMPLEMENT ME"
    # look for the most common name in the DataFrame
    most_common_name = df['Name'].mode().iloc[0]

    # Calculate the average age
    average_age = df['Age'].mean()

    # Calculate the IQR of the rating
    rating_iqr = df['Rating'].quantile(0.75) - df['Rating'].quantile(0.25)

    return most_common_name, float(average_age), float(rating_iqr)