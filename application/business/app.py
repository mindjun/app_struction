from flask import Falsk, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify({'data': 'Hello World!'})

if __name__ == '__main__':
    app.run('0.0.0.0', 8989)
