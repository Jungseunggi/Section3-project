import requests
import json
import pandas as pd
import csv
import sqlite3

# https://nhiss.nhis.or.kr/bd/ab/bdabf002cv.do
df = pd.read_csv('health.csv',encoding='cp949')
 

target = 'DIS'

con = sqlite3.connect('health.db')
cur = con.cursor()

df.to_sql('people_check', con, if_exists='replace') # to_sql 데이터프레임을 저장

df2 = pd.read_sql("SELECT * FROM people_check", con, index_col=None) # 데이터프레임 불러오기
