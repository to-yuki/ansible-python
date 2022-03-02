from flask import Flask, make_response ,request
from waitress import serve

api = Flask(__name__)

@api.route('/', methods=['GET'])
def function():
     print("function")
     return make_response('success')
 
if __name__ == '__main__':
     serve(api, host='0.0.0.0', port=3000)
     