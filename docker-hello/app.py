from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({'status:': 'Healthy'}), 200

@app.route('/')
def home():
    return jsonify({'message': 'THIS IS THE HOMEPAGE! :)'}), 200

@app.route('/names')
def office_names():
    names = ['Michael Scott', 'Jim Halpert', 'Pam Beasely']
    return jsonify({'message': names}), 200

@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello world!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
