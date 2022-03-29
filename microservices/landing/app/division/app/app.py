from flask import Flask,request
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)

class divide(Resource):
    def get(self,x,y):
        try:
            flag = float(x)/float(y)
        except ZeroDivisionError:
            flag = "infinity"
        return flag

api.add_resource(divide,'/divide/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5054,debug=True)