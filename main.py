#importing the libraries
from sklearn import linear_model
import pandas as pd
import numpy as np
from word2number import w2n
import math

#checking the data
df = pd.read_csv('hiring.csv')
df.head()

# Convert all values to string first, then lowercase
def convert_word(word):
    try:
        return w2n.word_to_num(str(word).lower())
    except:
        return 0

df['experience'] = df['experience'].map(convert_word).fillna(0).astype(int)

#filling the nan wiht median value
test_score = math.floor(df['test_score(out of 10)'].median())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(test_score)
df

#creating and traning the model
model = linear_model.LinearRegression()
model.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])

#making predict
model.predict([[5,9,9]])

#model.coef_

#model.intercept_

#Linear Regression Formula: y = mx + b

#2812.95487627*5+1845.70596798*9+2205.24017467*9+17737.263464337688