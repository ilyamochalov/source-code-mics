from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "UP"


@app.route('/cpu')
def cpu_intensive_task():
    result = 1
    for i in range(1, 1000):
        result = result * i

    return str(result)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000)
