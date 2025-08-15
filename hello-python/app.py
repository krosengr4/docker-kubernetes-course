from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"}), 200

@app.route('/names')
def show_names():
    names = ['Kevin', "Sarah", "Izel", "Michael"]
    return jsonify({'message': names}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
