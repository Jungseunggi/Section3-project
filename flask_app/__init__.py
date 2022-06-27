from flask import Flask, render_template, request
import pickle
import numpy as np

def create_app():
    model = None
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)

    app = Flask(__name__)

    @app.route('/')
    def main():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def home():
        data1 = request.form['a']
        data2 = request.form['b']
        if 20<= float(data2) <=24:
            data2_1 = 1
        elif 25<= float(data2) <=26:
            data2_1 = 2
        elif 27<= float(data2) <=28:
            data2_1 = 3
        elif 29<= float(data2) <=30:
            data2_1 = 4
        elif 31<= float(data2) <=32:
            data2_1 = 5 
        elif 33<= float(data2) <=34:
            data2_1 = 6
        elif 35<= float(data2) <=36:
            data2_1 = 7
        elif 37<= float(data2) <=38:
            data2_1 = 8
        elif 39<= float(data2) <=40:
            data2_1 = 9
        elif 41<= float(data2) <=42:
            data2_1 = 10
        elif 43<= float(data2) <=44:
            data2_1 = 11
        elif 45<= float(data2) <=46:
            data2_1 = 12
        elif 47<= float(data2) <=48:
            data2_1 = 13
        elif 49<= float(data2) <=50:
            data2_1 = 14
        elif 51<= float(data2) <=52:
            data2_1 = 15
        elif 53<= float(data2) <=54:
            data2_1 = 16
        elif 55<= float(data2) <=56:
            data2_1 = 17
        elif 57<= float(data2) <=58:
            data2_1 = 18
        elif 59<= float(data2) <=60:
            data2_1 = 19
        elif 61<= float(data2) <=62:
            data2_1 = 20
        elif 63<= float(data2) <=64:
            data2_1 = 21
        elif 65<= float(data2) <=66:
            data2_1 = 22
        elif 67<= float(data2) <=68:
            data2_1 = 23
        elif 69<= float(data2) <=70:
            data2_1 = 24
        elif 71<= float(data2) <=72:
            data2_1 = 25
        elif 73<= float(data2) <=74:
            data2_1 = 26
        elif 75<= float(data2) :
            data2_1 = 27                           

        data3 = request.form['c']
        data4 = request.form['d']
        data5 = round(float(data4)/(float(data3)**2)*10000,2)
        if float(data5) < 18.5:
            text2 = '저체중'
        elif 18.5<= float(data5) < 23:
            text2 = '정상'
        elif 23<= float(data5) < 25:
            text2 = '과체중'
        elif 25<= float(data5):
            text2 = '비만'        
        arr = [[float(data1), float(data2_1), float(data5)]]
        pred = model.predict(arr)
        if pred == 4:
            text = '고혈압, 당뇨병 의심이 없습니다.' 
        elif pred == 3:
            text = '당뇨병환자거나 의심이 됩니다.'
        elif pred == 2:
            text = '고혈압환자거나 의심이 됩니다.'
        elif pred == 1:
            text = '고혈압, 당뇨병 환자거나 의심이 됩니다.'
        
        return render_template('index.html', prediction_text = '당신의 BMI는 {}% {}입니다. 그리고 {}'.format(data5,text2,text))


    return app
    