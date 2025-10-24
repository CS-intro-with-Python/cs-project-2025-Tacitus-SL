from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/hello')
def hello():
	return jsonify({"message": 'Hello, world!'})

@app.route('/user/<username>')
def greeting(username):
    return jsonify({"message": f"Hello, <username>!"})

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return jsonify({
        "query": query,
        "length": len(query),
    })

if __name__ == '__main__':
    app.run(port=8080)