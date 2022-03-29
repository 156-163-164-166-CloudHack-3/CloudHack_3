from flask import Flask,request
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)

class subtract(Resource):
    def get(self,x,y):
        res = float(x)-float(y)
        return res

api.add_resource(subtract,'/subtract/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5052,debug=True)