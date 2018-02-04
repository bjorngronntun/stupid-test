from flask import Flask, jsonify, render_template
app = Flask(__name__)
import json

with open('data/graph.json') as f:
    graph = json.load(f)

@app.route('/')
def home():
    return render_template('axiostest.html')

@app.route('/graph')
def draw_graph():
    return jsonify(graph)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
