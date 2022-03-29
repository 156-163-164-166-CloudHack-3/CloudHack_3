from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    flag=0
    if number_1 =='':
        flash(f'Enter number')
        flag=1
    elif number_2 =='':
        flash(f'Enter number')
        flag=1
    if operation == 'add':
        result=requests.get("http://10.14.142.123:5051/add/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'minus':
        result=requests.get("http://10.14.142.123:5052/subtract/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'multiply':
        result=requests.get("http://10.14.142.123:5053/multiply/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'divide':
        result=requests.get("http://10.14.142.123:5054/divide/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'exponent':
        result=requests.get("http://10.14.142.123:5055/expo/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'greater_than':
        result=requests.get("http://10.14.142.123:5056/grt/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'lesser_than':
        result=requests.get("http://10.14.142.123:5057/lrt/"+str(number_1)+"/"+str(number_2)).text

    if flag==0:
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )