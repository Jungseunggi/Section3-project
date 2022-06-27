import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
import sqlite3

con = sqlite3.connect('health.db')
cur = con.cursor()

df = pd.read_sql("SELECT * FROM people_check", con, index_col=None)
# 나이, 성별, bmi -> 고혈압 판단 ! 


df = df.drop(['FBS','SBP','DBP','index'],axis=1)


target = 'DIS'


X_train = np.array(df.drop(columns=target))
y_train = df[target]

model = KNeighborsClassifier()
model.fit(X_train,y_train)


#X_test = np.array([[1, 10, 20]])
#y_test = model.predict(X_test)

#print(y_test)
with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)

    