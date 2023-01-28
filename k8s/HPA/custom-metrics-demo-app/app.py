from flask import Flask
from prometheus_client import Gauge, generate_latest
from time import sleep
from random import randrange

app = Flask(__name__)
number_of_tasks = Gauge('number_of_tasks', 'Number of tasks that is handled in this application instance')

@app.route('/task')
def run_task():
    number_of_tasks.inc(1)
    sleep(randrange(15))
    number_of_tasks.dec(1)
    return "Task finished\n"

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/')
def root():
    return "UP"

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5050)
