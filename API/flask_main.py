from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def get_data():
    data = {'message': 'Hello, this is flask bitch!'}
    return jsonify(data)




@app.route('/message', methods = ['GET'])
def get_msg():
    d = {}
    input_msg = str(request.args['query'])
    d['output'] = input_msg
    return jsonify(d)




if __name__ == "__main__":
    app.run(debug=True)





