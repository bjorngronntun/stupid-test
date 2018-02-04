from flask import Flask
import numpy as np

app = Flask(__name__)

x = np.linspace(0,1,100)

@app.route('/')
def home():
    return str(np.sin(x))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
