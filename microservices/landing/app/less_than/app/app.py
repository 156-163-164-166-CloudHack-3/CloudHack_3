from flask import Flask,request
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)

class lrt(Resource):
    def get(self,x,y):
        if float(x) < float(y):
            return True
        else:
            return False
api.add_resource(lrt,'/lrt/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5057,debug=True)